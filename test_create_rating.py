import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"


# Base choice: 3 stars as a whole number, a real pizza, the user's token.
def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id


# C1: a number of stars below 1 or above 5 is refused with a message.
@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}


# C2: a decimal or text stars value is refused with a type error.
@pytest.mark.parametrize(
    "stars, error",
    [
        (3.5, "json: cannot unmarshal number 3.5 into Go struct field Rating.stars of type int"),
        ("3", "json: cannot unmarshal string into Go struct field Rating.stars of type int"),
    ],
    ids=["decimal", "text"],
)
def test_stars_wrong_type_is_refused(api, auth, pizza_id, stars, error):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id, "stars": stars}, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": error}


# C2: a missing stars field is refused.
def test_missing_stars_is_refused(api, auth, pizza_id):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id}, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}


# C3: a pizza id that does not exist is refused.
def test_unknown_pizza_is_refused(api, auth):
    res = api.post("/api/ratings", json={"pizza_id": 999999999, "stars": 3}, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": "pizza ID 999999999 not found"}


# C4: a missing or short token is refused.
@pytest.mark.parametrize(
    "headers",
    [None, {"Authorization": "token short"}],
    ids=["no-token", "short-token"],
)
def test_token_is_refused(api, auth, pizza_id, headers):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id, "stars": 3}, headers=headers)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}

# API lab results

## Part 0

- Step 0.1, number of pizza names from `GET /api/names`: 18.
- Step 0.2, `curl -i https://quickpizza.grafana.com/api/names`: `HTTP/1.1 200 OK`, `Content-Type: application/json`, and a `Set-Cookie: AWSALB=...` header were returned. The body contained the same 18 pizza names as Step 0.1. The observed protocol was HTTP/1.1 (the handout shows HTTP/2).
- Step 0.3, `GET /api/tools` without a token returned `401 Unauthorized` and `{"error":"authentication failed"}`. With the public token in `auth.txt`, it returned Knife, Pizza cutter, and Scissors.
- Step 0.4, `POST /api/pizza` with `veg.json` returned **A Tall Funghi**. The response marked the pizza and every ingredient as vegetarian.
- Step 0.5, Python `requests`: `GET /api/names` returned `200`, `Content-Type: application/json`, a `dict` body, and first name `Americana`; `GET /api/tools` with the token returned `200` and Knife, Pizza cutter, Scissors; `POST /api/pizza` with `{"mustBeVegetarian": true}` returned `200` and **An Orange Romana**.
- Step 0.6, `pytest -v`: the `Margherita` test passed (1 passed). Changing the expected name to `Pineapple Supreme` produced the expected `AssertionError` (1 failed). After restoring `Margherita`, the test passed again (1 passed).
- Step 0.7, `pytest -v`: both `test_names_are_listed` and `test_tools_are_listed` passed (2 passed). The tools test read the token from the local, Git-ignored `auth.txt`.
- Step 0.8, `pytest -v`: after adding the vegetarian pizza test, 3 passed; after adding the no-token rejection test, 4 passed. The vegetarian response had a nonempty name and vegetarian ingredients, and the no-token request returned `401` with `{"error":"authentication failed"}`.
- Step 0.9, created test user `lab-40933d066aaf` with a `requests.Session` (`201 Created`, id `48`), logged in (`200`), and read that user's ratings with its own token (`200`, `{"ratings":[]}`). The session kept the `AWSALB` and `AWSALBCORS` cookies. The token was not saved in the repository.
- Step 0.10, added the session-scoped `api` fixture in `conftest.py`; `pytest -v` still reported 4 passed.
- Step 0.11, added `log_in_new_user` and the per-test `auth` fixture. The new user had no ratings; `pytest -v` reported 5 passed. User tokens remained only in memory.
- Step 0.12 (optional), ran `pytest -v test_no_session.py` three times without a session: run 1 failed (login `401`), run 2 failed (login `401`), run 3 failed (login `401`), despite user creation returning `201` each time. Deleted the temporary flaky test afterward.
- Step 0.13, added the `pizza_id` fixture and a test that creates a 5-star rating with a freshly created user's token. The rating response had `201`, the expected stars and pizza id, and an integer rating id; `pytest -v` reported 6 passed.
- Step 0.14, added a 3-star `rating` fixture with teardown plus read, update, and delete tests. All rating changes used each test user's token. `pytest -v` reported 9 passed; `pytest -v test_ratings.py::test_delete_rating` also passed alone (1 passed).
- Step 0.15, duplicate username returned `400` with `{"error":"username already taken"}`; wrong password returned `401` with `{"error":"authentication failed"}`; empty username returned `400` with `{"error":"username field is empty"}`. `pytest -v` reported 12 passed.
- Step 0.16, the characteristic **number of the three tools excluded** has four blocks: 0, 1, 2, or 3. The original tests covered only block 1 (`["Knife"]`, `["Scissors"]`). Added `[]` for block 0, `["Knife", "Scissors"]` for block 2, and all three tools for block 3. The first four inputs passed; the all-tools input failed because the API returned `500`.

### Defect 1: Excluding all tools causes a server error

- Request: `POST /api/pizza` with `{"excludedTools":["Knife","Pizza cutter","Scissors"]}` and an Authorization token. Confirmed with `curl -i -H "@auth.txt" -d "@all-tools-excluded.json" https://quickpizza.grafana.com/api/pizza`.
- Expected: `400 Bad Request` with a nonempty JSON error message because no pizza can use an available tool.
- Actual: `500 Internal Server Error`, `Content-Length: 0`, and an empty body (confirmed by both pytest and curl).
- Severity: medium. A valid customer restriction causes a server error instead of a clear input error, so clients cannot explain the problem to the customer.
- Final Step 0.16 run: `pytest -v` reported **16 passed, 1 xfailed**. The defect test uses strict xfail so a future fix will be visible.

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

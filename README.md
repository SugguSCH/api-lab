# api-lab

QuickPizza API lab using Python, requests, and pytest.

## Install and run

From this repository folder, create a virtual environment and install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create a local `auth.txt` with the public practice token from the lab handout in the form `Authorization: token <practice-token>`. Git ignores this file. Then run:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe -m pytest -v --html=report.html --self-contained-html
```

Tests that create or change ratings generate their own users and tokens. One excluded-tools test is marked `xfail` for the confirmed API defect. See `RESULTS.md` for observations and Part B answers.

For Part B question 7, create `madeup.txt` locally with the exact sample line from the handout and use it only for the read-only request. This file is also Git-ignored because the API accepts that value for reading ratings.

## Part A: Input domain model for `POST /api/ratings`

The base choice is 3 whole-number stars, an existing pizza, and the new test user's own token. Each additional test changes one characteristic while keeping the others at the base choice.

| Characteristic | Block | Value | Covering test |
| --- | --- | --- | --- |
| C1 Value of stars | Below 1 | `0` | `test_stars_out_of_range[0]` |
| C1 Value of stars | 1 to 5 (base) | `3` | `test_base_choice_is_saved` |
| C1 Value of stars | Above 5 | `6` | `test_stars_out_of_range[6]` |
| C2 Type of stars | Whole number (base) | `3` | `test_base_choice_is_saved` |
| C2 Type of stars | Decimal | `3.5` | `test_stars_wrong_type_is_refused[decimal]` |
| C2 Type of stars | Text | `"3"` | `test_stars_wrong_type_is_refused[text]` |
| C2 Type of stars | Missing | No `stars` field | `test_missing_stars_is_refused` |
| C3 Pizza | Exists (base) | A new pizza | `test_base_choice_is_saved` |
| C3 Pizza | Does not exist | `999999999` | `test_unknown_pizza_is_refused` |
| C4 Token | User's own (base) | Own token | `test_base_choice_is_saved` |
| C4 Token | None | No header | `test_token_is_refused[no-token]` |
| C4 Token | Wrong length | Short token | `test_token_is_refused[short-token]` |

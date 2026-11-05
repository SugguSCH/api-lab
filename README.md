# api-lab

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

# api-lab

## Part A: Input domain model for `POST /api/ratings`

The base choice is 3 whole-number stars, an existing pizza, and the new test user's own token. Each additional test changes one characteristic while keeping the others at the base choice.

| Characteristic | Blocks | Values in tests |
| --- | --- | --- |
| C1 Value of stars | Below 1; 1 to 5 (base); above 5 | `0`; `3`; `6` |
| C2 Type of stars | Whole number (base); decimal; text; missing | `3`; `3.5`; `"3"`; no `stars` field |
| C3 Pizza | Exists (base); does not exist | A new pizza; `999999999` |
| C4 Token | User's own (base); none; wrong length | Own token; no header; short token |

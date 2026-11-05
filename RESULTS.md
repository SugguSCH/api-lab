# API lab results

## Part 0

- Step 0.1, number of pizza names from `GET /api/names`: 18.
- Step 0.2, `curl -i https://quickpizza.grafana.com/api/names`: `HTTP/1.1 200 OK`, `Content-Type: application/json`, and a `Set-Cookie: AWSALB=...` header were returned. The body contained the same 18 pizza names as Step 0.1. The observed protocol was HTTP/1.1 (the handout shows HTTP/2).
- Step 0.3, `GET /api/tools` without a token returned `401 Unauthorized` and `{"error":"authentication failed"}`. With the public token in `auth.txt`, it returned Knife, Pizza cutter, and Scissors.
- Step 0.4, `POST /api/pizza` with `veg.json` returned **A Tall Funghi**. The response marked the pizza and every ingredient as vegetarian.

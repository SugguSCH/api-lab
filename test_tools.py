from pathlib import Path

import requests

SITE = "https://quickpizza.grafana.com"
AUTH = {"Authorization": Path("auth.txt").read_text(encoding="utf-8").strip().split(": ", 1)[1]}


# The list of tools answers 200 and names the three tools.
def test_tools_are_listed():
    res = requests.get(SITE + "/api/tools", headers=AUTH)
    assert res.status_code == 200
    assert res.json() == {"tools": ["Knife", "Pizza cutter", "Scissors"]}

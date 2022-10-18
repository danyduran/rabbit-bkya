import json

import requests

from app.services.constants import QUERY, URL_API


def get_pokemons(locations, region="kanto"):
    headers = {"Content-Type": "application/json"}
    query_variables = {"region": region, "locations": locations}
    req = requests.request(
        "POST",
        url=URL_API,
        data=json.dumps({"query": QUERY, "variables": query_variables}),
        headers=headers,
    )

    return json.loads(req.content)

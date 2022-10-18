import json

from app.services import pokemon_services as service_pokemon


def load_success_query(locations):
    with open("./src/test_json_files/success_query.json", "r") as file:
        return json.load(file)


def load_failed_query(locations):
    with open("./src/test_json_files/failed_query.json", "r") as file:
        return json.load(file)


def test_success_get_pokemons(monkeypatch):
    monkeypatch.setattr(service_pokemon, "get_pokemons", load_success_query)
    result = service_pokemon.get_pokemon_by_locations(
        ["pallet-town", "kanto-route-22", "viridian-forest"]
    )
    assert len(result.get("found", [])) == 3
    assert result.get("bestArea", {}).get("location", "") == "pallet-town"
    assert result.get("areas")


def test_no_valid_locations(monkeypatch):
    monkeypatch.setattr(service_pokemon, "get_pokemons", load_failed_query)

    result = service_pokemon.get_pokemons(["veracruz", "Palenque"])
    result = service_pokemon.get_pokemon_by_locations(result)
    assert len(result.get("found", [])) == 0
    assert result.get("bestArea", {}) is None
    assert result.get("areas", []) == []

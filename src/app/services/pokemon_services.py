from typing import List

from app.services.api_pokemons import get_pokemons


def get_pokemon_by_locations(locations: List[str]):
    results = get_pokemons(locations)
    results = results.get("data", {})
    found = results.get("found_locations", [])
    found_areas = results.get("areas", [])
    best_area = None
    response = {"found": [location["name"] for location in found]}
    areas = []

    for item in found_areas:
        area = {"location": item["location"]["name"], "name": item["name"]}
        pokemons = item.get("pokemons", [])
        found_pokemons = []

        for pokemon in pokemons:
            new_pokemon = {**pokemon["pokemon"]}
            del new_pokemon["abilities"]
            new_pokemon["abilities"] = []
            abilities = pokemon.get("pokemon", {}).get("abilities", [])

            for abilitie in abilities:
                pokemon_abilitie = abilitie["pokemon_v2_ability"]
                generation = pokemon_abilitie.get("generation").get("name", "")
                del pokemon_abilitie["generation"]
                pokemon_abilitie["generation"] = generation
                new_pokemon["abilities"].append(pokemon_abilitie)

            found_pokemons.append(new_pokemon)
        area["pokemons"] = found_pokemons

        if best_area:
            best_area = (
                area
                if len(area.get("pokemons", [])) > len(best_area.get("pokemons", []))
                else best_area
            )
        else:
            best_area = area
        areas.append(area)

    response["areas"] = areas
    response["bestArea"] = best_area

    return response

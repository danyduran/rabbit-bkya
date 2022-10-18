URL_API = "https://beta.pokeapi.co/graphql/v1beta"

QUERY = """
        query GetPokemons($region: String!, $locations: [String!]!) {
            found_locations: pokemon_v2_location(where: {name: {_in: $locations}, pokemon_v2_region: {name: {_eq: $region}}}) {
                name
            }
            areas: pokemon_v2_locationarea(where: {pokemon_v2_location: {name: {_in: $locations}, pokemon_v2_region: {name: {_eq: $region}}}}) {
                location: pokemon_v2_location {
                    name
                }
                name
                pokemons: pokemon_v2_encounters(distinct_on: pokemon_id) {
                pokemon: pokemon_v2_pokemon {
                    name
                    height
                    weight
                    abilities: pokemon_v2_pokemonabilities {
                    pokemon_v2_ability {
                        name
                        generation: pokemon_v2_generation {
                        name
                        }
                    }
                    }
                }
                }
            }
        }
    """

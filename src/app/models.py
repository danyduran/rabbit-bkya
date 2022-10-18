from typing import List

from pydantic import BaseModel


class Ability(BaseModel):
    name: str
    generation: str


class Pokemon(BaseModel):
    name: str
    height: int
    weight: int
    abilities: List[Ability] = []


class Area(BaseModel):
    location: str
    pokemons: List[Pokemon] = []


class Response(BaseModel):
    found: List[str]
    areas: List[Area] = []
    bestArea: Area = None


class Locations(BaseModel):
    locations: List[str]

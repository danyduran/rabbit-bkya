from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.models import Locations, Response
from app.services.pokemon_services import get_pokemon_by_locations

app = FastAPI()


@app.get("/")
def home():
    return RedirectResponse(url="/docs/")


@app.post("/api/pokemon-in-location/", response_model=Response)
def get_pokemon_by_location(locations: Locations):
    return get_pokemon_by_locations(locations.locations)

from ports.RickMortyAPI_Port import RickAPI
import requests
from domain.RickMortyData import RickMorty as rick
import json


class Rick_Adapter(RickAPI):
    API_URL = "https://rickandmortyapi.com/api/character"

    def __init__(self, api):
        self.api = api

    def get_characters_info(self, page):
        params = {
            "page": page
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            return "Hubo un problema con la api"

        data = response.json()
        ricks = []
        for i in data["results"]:
            name = i["name"]
            status = i["status"]
            location = i["location"]["name"]
            image = i["image"]
            ricks.append(rick(name, status, location, image=image).__dict__)

        return json.dumps(ricks)

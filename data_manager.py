import os

import dotenv
import requests as req

dotenv.load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self._API_ENDPOINT = str(os.getenv("SHEETY_ENDPOINT"))
        self._API_TOKEN = str(os.getenv("SHEETY_TOKEN"))

        self._headers = {"Authorization": f"Bearer {self._API_TOKEN}"}

    def get_sheet(self):
        r = req.get(self._API_ENDPOINT, headers=self._headers)
        r.raise_for_status()
        return r.json()["prices"]

    def put_sheet(self, new_data):
        for data in new_data:
            id = data["id"]
            iataCode = data["iataCode"]
            r = req.put(
                f"{self._API_ENDPOINT}/{id}",
                headers=self._headers,
                json={"price": {"iataCode": iataCode}},
            )
            r.raise_for_status()

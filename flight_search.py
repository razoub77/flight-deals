import os

import dotenv
import requests as req

dotenv.load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    _API_ENDPOINT = "https://test.api.amadeus.com/v1"
    _API_KEY = str(os.getenv("AMADEUS_API_KEY"))
    _API_SECRET = str(os.getenv("AMADEUS_API_SECRET"))

    def __init__(self) -> None:
        self._token = self._get_new_token()

    def _get_new_token(self):
        r = req.post(
            f"{self._API_ENDPOINT}/security/oauth2/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": self._API_KEY,
                "client_secret": self._API_SECRET,
            },
        )
        json = r.json()
        return json["access_token"]

    def update_iata(self, empty_iata):
        for item in empty_iata:
            city = item["city"]

            r = req.get(
                f"{self._API_ENDPOINT}/reference-data/locations/cities",
                headers={"Authorization": f"Bearer {self._token}"},
                params={"keyword": city},
            )
            r.raise_for_status()
            data = r.json()["data"]
            iataCode = data[0]["iataCode"]

            item["iataCode"] = iataCode

        return empty_iata

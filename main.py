from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_sheet()
empty_iata = [data for data in sheet_data if not data["iataCode"]]

flight_search = FlightSearch()
updated_iata = flight_search.update_iata(empty_iata)

data_manager.put_sheet(updated_iata)

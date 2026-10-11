import requests
from config import SERVER_URL


def request_last_reserve(search_type: str, search_value) -> dict:
    if search_type == "id":
        params = {"animal_id": search_value}
    else:
        params = {"collar_code": search_value}

    response = requests.get(
        f"{SERVER_URL}/animals/last-reserve",
        params=params
    )

    return response.json()
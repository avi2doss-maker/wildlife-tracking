from animal_search import choose_search_type, read_animal_id, read_collar_code
from http_client import request_last_reserve
from output import show_last_reserve


def main() -> None:
    search_type = choose_search_type()

    if search_type == "id":
        search_value = read_animal_id()
    else:
        search_value = read_collar_code()

    result = request_last_reserve(search_type, search_value)

    show_last_reserve(result)


main()
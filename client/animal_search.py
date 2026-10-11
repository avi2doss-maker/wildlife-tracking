def choose_search_type() -> str:
    while True:
        print("1. Search by ID")
        print("2. Search by collar code")

        choice = input("Choose search type: ").strip()

        if choice == "1":
            return "id"

        if choice == "2":
            return "collar_code"

        print("Invalid choice. Try again.")


def read_animal_id() -> int:
    while True:
        animal_id = input("Animal ID: ").strip()

        if animal_id.isdigit() and int(animal_id) > 0:
            return int(animal_id)

        print("Invalid ID. Enter a positive integer.")


def read_collar_code() -> str:
    while True:
        collar_code = input("Collar code: ").strip()

        if collar_code.startswith("COL-"):
            return collar_code

        print("Invalid collar code. It must start with COL-.")













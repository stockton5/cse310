import database


def display_menu():
    print("\nHunting Trip Database")
    print("1. Add hunting trip")
    print("2. View all trips")
    print("3. Update trip result")
    print("4. Delete trip")
    print("5. View animal report")
    print("6. Exit")


def add_trip():
    print("\nAdd Hunting Trip")
    location = input("Location: ").strip()
    animal = input("Animal hunted: ").strip()
    trip_date = input("Date (YYYY-MM-DD): ").strip()
    result = input("Result: ").strip()

    if not location or not animal or not trip_date or not result:
        print("All fields are required.")
        return

    database.add_trip(location, animal, trip_date, result)
    print("Trip added successfully.")


def view_trips():
    trips = database.get_all_trips()

    print("\nAll Hunting Trips")

    if not trips:
        print("No trips have been entered.")
        return

    for trip in trips:
        print("-" * 35)
        print(f"ID:       {trip[0]}")
        print(f"Location: {trip[1]}")
        print(f"Animal:   {trip[2]}")
        print(f"Date:     {trip[3]}")
        print(f"Result:   {trip[4]}")


def update_trip():
    view_trips()

    try:
        trip_id = int(input("\nEnter the trip ID to update: "))
    except ValueError:
        print("The trip ID must be a number.")
        return

    new_result = input("Enter the new result: ").strip()

    if not new_result:
        print("The result cannot be empty.")
        return

    changed_rows = database.update_trip_result(trip_id, new_result)

    if changed_rows == 0:
        print("Trip ID was not found.")
    else:
        print("Trip updated successfully.")


def delete_trip():
    view_trips()

    try:
        trip_id = int(input("\nEnter the trip ID to delete: "))
    except ValueError:
        print("The trip ID must be a number.")
        return

    deleted_rows = database.delete_trip(trip_id)

    if deleted_rows == 0:
        print("Trip ID was not found.")
    else:
        print("Trip deleted successfully.")


def view_report():
    report = database.get_animal_report()

    print("\nTrips by Animal")

    if not report:
        print("There is no data for the report.")
        return

    for animal, total in report:
        print(f"{animal}: {total} trip(s)")


def main():
    database.create_table()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_trip()
        elif choice == "2":
            view_trips()
        elif choice == "3":
            update_trip()
        elif choice == "4":
            delete_trip()
        elif choice == "5":
            view_report()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Please choose a number from 1 through 6.")


if __name__ == "__main__":
    main()
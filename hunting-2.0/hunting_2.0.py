
from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter


COLLECTION = "trucks"
KEY_FILE = "serviceAccountKey.json"


def connect_db():
    """Connect to Firestore using a Firebase service account file."""
    if not Path(KEY_FILE).exists():
        print("Missing serviceAccountKey.json")
        print("Download it from Firebase and place it in this folder.")
        raise SystemExit

    if not firebase_admin._apps:
        cred = credentials.Certificate(KEY_FILE)
        firebase_admin.initialize_app(cred)

    return firestore.client()


def get_text(prompt):
    """Get required text input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def get_int(prompt):
    """Get required number input."""
    while True:
        try:
            return int(input(prompt).strip().replace(",", ""))
        except ValueError:
            print("Please enter a whole number.")


def get_optional(prompt):
    """Get optional input for updates."""
    value = input(prompt).strip()
    if value == "":
        return None
    return value


def print_truck(doc):
    """Print one truck document."""
    truck = doc.to_dict()
    print("-" * 50)
    print(f"ID: {doc.id}")
    print(f"Truck: {truck['year']} {truck['make']} {truck['model']}")
    print(f"Engine: {truck['engine']}")
    print(f"Mileage: {truck['mileage']:,}")
    print(f"Price: ${truck['price']:,}")
    print(f"Drivetrain: {truck['drivetrain']}")
    print(f"Title: {truck['title_status']}")
    print(f"Notes: {truck['notes']}")


def add_truck(db):
    """Insert a new truck record into Firestore."""
    print("\nAdd Truck")

    make = get_text("Make: ")
    truck = {
        "make": make,
        "make_lower": make.lower(),
        "model": get_text("Model: "),
        "year": get_int("Year: "),
        "mileage": get_int("Mileage: "),
        "price": get_int("Price: "),
        "engine": get_text("Engine: "),
        "drivetrain": get_text("Drivetrain: "),
        "title_status": get_text("Title status: "),
        "notes": get_text("Notes: "),
        "created_at": firestore.SERVER_TIMESTAMP,
        "updated_at": firestore.SERVER_TIMESTAMP,
    }

    db.collection(COLLECTION).add(truck)
    print("Truck added successfully.")


def seed_data(db):
    """Add sample truck records for demonstration."""
    print("\nSeed Sample Data")

    if list(db.collection(COLLECTION).limit(1).stream()):
        print("Sample data was not added because records already exist.")
        return

    trucks = [
        {
            "make": "Chevrolet",
            "model": "Silverado 2500HD",
            "year": 2006,
            "mileage": 178000,
            "price": 22500,
            "engine": "6.6L Duramax LBZ",
            "drivetrain": "4WD",
            "title_status": "Clean",
            "notes": "Older diesel truck with strong resale value.",
        },
        {
            "make": "GMC",
            "model": "Sierra 1500 Z71",
            "year": 2009,
            "mileage": 142000,
            "price": 13900,
            "engine": "5.3L V8",
            "drivetrain": "4WD",
            "title_status": "Clean",
            "notes": "Gas truck with off-road package.",
        },
        {
            "make": "Ford",
            "model": "F-250 Super Duty",
            "year": 2002,
            "mileage": 210000,
            "price": 18500,
            "engine": "7.3L Power Stroke",
            "drivetrain": "4WD",
            "title_status": "Clean",
            "notes": "High-mile diesel with desirable engine.",
        },
    ]

    for truck in trucks:
        truck["make_lower"] = truck["make"].lower()
        truck["created_at"] = firestore.SERVER_TIMESTAMP
        truck["updated_at"] = firestore.SERVER_TIMESTAMP
        db.collection(COLLECTION).add(truck)

    print("Sample trucks added.")


def view_all(db):
    """Retrieve and display all truck records."""
    print("\nAll Trucks")
    docs = db.collection(COLLECTION).stream()
    found = False

    for doc in docs:
        print_truck(doc)
        found = True

    if not found:
        print("No trucks found.")


def query_by_make(db):
    """Query trucks by make."""
    print("\nQuery by Make")
    make = get_text("Enter make: ")

    docs = db.collection(COLLECTION).where(
        filter=FieldFilter("make_lower", "==", make.lower())
    ).stream()

    found = False
    for doc in docs:
        print_truck(doc)
        found = True

    if not found:
        print("No matching trucks found.")


def query_by_price(db):
    """Query trucks below a maximum price."""
    print("\nQuery by Max Price")
    max_price = get_int("Maximum price: ")

    docs = db.collection(COLLECTION).where(
        filter=FieldFilter("price", "<=", max_price)
    ).stream()

    found = False
    for doc in docs:
        print_truck(doc)
        found = True

    if not found:
        print("No matching trucks found.")


def update_truck(db):
    """Modify an existing truck record."""
    print("\nUpdate Truck")
    doc_id = get_text("Enter truck ID: ")

    ref = db.collection(COLLECTION).document(doc_id)
    doc = ref.get()

    if not doc.exists:
        print("Truck not found.")
        return

    print("Current record:")
    print_truck(doc)
    print("\nPress Enter to keep a field unchanged.")

    updates = {}

    price = get_optional("New price: ")
    mileage = get_optional("New mileage: ")
    notes = get_optional("New notes: ")

    if price:
        updates["price"] = int(price.replace(",", ""))
    if mileage:
        updates["mileage"] = int(mileage.replace(",", ""))
    if notes:
        updates["notes"] = notes

    if updates:
        updates["updated_at"] = firestore.SERVER_TIMESTAMP
        ref.update(updates)
        print("Truck updated.")
    else:
        print("No changes made.")


def delete_truck(db):
    """Delete a truck record from Firestore."""
    print("\nDelete Truck")
    doc_id = get_text("Enter truck ID: ")

    ref = db.collection(COLLECTION).document(doc_id)
    doc = ref.get()

    if not doc.exists:
        print("Truck not found.")
        return

    print_truck(doc)
    confirm = input("Type DELETE to confirm: ")

    if confirm == "DELETE":
        ref.delete()
        print("Truck deleted.")
    else:
        print("Delete canceled.")


def menu():
    """Show menu options."""
    print("\nTruck Cloud Database")
    print("1. Seed sample data")
    print("2. Add truck")
    print("3. View all trucks")
    print("4. Query by make")
    print("5. Query by max price")
    print("6. Update truck")
    print("7. Delete truck")
    print("8. Exit")


def main():
    """Run the menu program."""
    db = connect_db()

    while True:
        menu()
        choice = input("Choose 1-8: ").strip()

        if choice == "1":
            seed_data(db)
        elif choice == "2":
            add_truck(db)
        elif choice == "3":
            view_all(db)
        elif choice == "4":
            query_by_make(db)
        elif choice == "5":
            query_by_price(db)
        elif choice == "6":
            update_truck(db)
        elif choice == "7":
            delete_truck(db)
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
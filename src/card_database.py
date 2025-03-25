import csv
import os

CSV_FILE = os.path.join(os.path.dirname(__file__), "../database/cards.csv")


def initialize_csv():
    """Creates the CSV file if it doesn't exist or Deletes old CSV file and creates a new one with headers."""
    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)
        print("Old inventory removed. New CSV initialized.")

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Price", "Image Path", "Status", "Claimed By (Phone Number)"])

def get_next_id():
    """Finds the next available ID for a new card."""
    if not os.path.exists(CSV_FILE):
        return 1

    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        rows = list(reader)

        if not rows:
            return 1

        last_id = int(rows[-1][0])  # Get the last ID in the file
        return last_id + 1


def add_card(card_number: int, name: str, price: float, image_path: str):
    """Adds a new card to the inventory with a unique card ID and other details."""
    card_id = card_number
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([card_id, name, price, image_path, "unsold", ""])
    print(f"Card '{name}' added successfully with ID {card_id}. Price: {price} and Image Path: {image_path}")


def get_available_cards():
    """Retrieves all unsold cards."""
    available_cards = []
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Status"] == "unsold":
                available_cards.append(row)
    return available_cards


def mark_card_as_sold(card_id: int, phone_number: str):
    """Marks a card as sold and assigns it to the buyer."""
    updated_rows = []
    card_found = False

    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["ID"]) == card_id and row["Status"] == "unsold":
                row["Status"] = "claimed"
                row["Claimed By"] = phone_number
                card_found = True
            updated_rows.append(row)

    if not card_found:
        print(f"Card with ID {card_id} not found or already sold.")
        return False

    # Write back to the file
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Price", "Image Path", "Status", "Claimed By"])
        writer.writeheader()
        writer.writerows(updated_rows)

    print(f"Card ID {card_id} marked as sold to {phone_number}.")
    return True


def remove_old_inventory():
    """Removes all sold cards from the inventory."""
    updated_rows = []
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Status"] != "claimed":
                updated_rows.append(row)

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Price", "Image Path", "Status", "Claimed By"])
        writer.writeheader()
        writer.writerows(updated_rows)

    print("Removed all sold cards from inventory.")


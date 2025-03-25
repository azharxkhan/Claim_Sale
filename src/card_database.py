def add_card(name: str, price: float, image_path: str) -> None:
    """Add a new card to the inventory (cards.csv)."""

def get_available_cards() -> list:
    """Fetch all available (unsold) cards from the inventory."""

def mark_card_as_sold(card_id: int, phone_number: str) -> bool:
    """Mark a card as sold and store the buyer's phone number."""

def remove_old_inventory() -> None:
    """Remove all sold cards from the inventory."""

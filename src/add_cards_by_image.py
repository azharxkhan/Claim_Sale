import os
from tkinter import Tk, filedialog
import shutil

from card_database import get_next_id, initialize_csv, add_card


def select_image():
    """Uses Tkinter to open a file dialog and select an image file."""
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.png;*.jpeg;*.gif")])
    return file_path

def add_card_interactively():
    """Interactively adds a new card by asking the user for input, including selecting an image."""
    card_id = get_next_id()  
    print(f"Adding a new card with ID: {card_id}")

    # Select the image file
    image_path = select_image()
    if not image_path:
        print("No image selected, exiting.")
        return
    
    name = input("Enter the card name: ")
    price = float(input("Enter the card price: "))

    images_dir = os.path.join(os.path.dirname(__file__), "images")
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    image_name = os.path.basename(image_path)
    new_image_path = os.path.join(images_dir, image_name)
    
    shutil.copy(image_path, new_image_path)

    add_card(card_id, name, price, new_image_path)
    print(f"Card '{name}' added successfully with ID {card_id}. Price: {price} and Image Path: {new_image_path}")

if __name__ == "__main__":
    initialize_csv() 
    add_card_interactively()  

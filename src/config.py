import os

# Database configuration
DATABASE_PATH = os.path.join(os.getcwd(), "database", "claim_sale.db")

# Image storage settings
IMAGE_FOLDER = os.path.join(os.getcwd(), "images")

# Invoice storage settings
INVOICE_FOLDER = os.path.join(os.getcwd(), "invoices")

# WhatsApp Web settings
WHATSAPP_GROUP_NAME = "Pokémon Card Claims"  # Change this to your group/chat name

# Selenium WebDriver settings
CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "chromedriver")  
WHATSAPP_WEB_URL = "https://web.whatsapp.com"

# Claim settings
CLAIM_KEYWORD = "Claim"  
CLAIM_TIMEOUT = 5  # Time in seconds to detect the first claim

# Invoice settings
CURRENCY_SYMBOL = "ZAR"  

# Debugging
DEBUG_MODE = True  # Set to False in production

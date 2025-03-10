import logging
import os
from datetime import datetime

# Tworzenie katalogu na logi, jeśli nie istnieje
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Nazwa pliku logu z datą
log_filename = os.path.join(log_dir, f"autoclicker_{datetime.now().strftime('%Y-%m-%d')}.log")

# Konfiguracja loggera
def setup_logger():
    logger = logging.getLogger("autoclicker")
    logger.setLevel(logging.INFO)
    
    # Handler do pliku
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # Handler do konsoli
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Format logów
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(log_format)
    console_handler.setFormatter(log_format)
    
    # Dodanie handlerów do loggera
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Kolorowe logi w konsoli
def info(message):
    logger = logging.getLogger("autoclicker")
    logger.info(message)
    print(f"\033[1;33m{message}\033[0m")  # Żółty kolor w konsoli

def warning(message):
    logger = logging.getLogger("autoclicker")
    logger.warning(message)
    print(f"\033[1;31m{message}\033[0m")  # Czerwony kolor w konsoli

def error(message):
    logger = logging.getLogger("autoclicker")
    logger.error(message)
    print(f"\033[1;31m{message}\033[0m")  # Czerwony kolor w konsoli

def debug(message):
    logger = logging.getLogger("autoclicker")
    logger.debug(message)
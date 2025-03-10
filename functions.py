import subprocess
import time
import random
import logger

DEVICE_ID = "0A62414I29101934"

def visit_website_domodeo(url="www.domodeo24.pl"):
    """
    Otwiera przeglądarkę Chrome w trybie incognito i odwiedza podany adres URL.
    """
    try:
        # Krok 1: Uruchomienie Chrome
        subprocess.run([
            "adb", "-s", DEVICE_ID, "shell", "am", "start",
            "-n", "com.android.chrome/com.google.android.apps.chrome.Main",
        ], check=True)
        time.sleep(2)  # odczekaj, aż przeglądarka się załaduje

        # Krok 2: Wywołanie menu (keyevent 82)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "keyevent", "82"], check=True)

        # Krok 3: Symulacja kliknięcia w opcję "Nowa karta incognito"
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "450", "310"], check=True)

        # Krok 4: Kliknięcie w pasek adresu 
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "308", "113"], check=True)

        # Krok 5: Wpisanie URL
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "text", url], check=True)

        # Krok 6: Naciśnięcie Enter (keyevent 66)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "keyevent", "66"], check=True)
        time.sleep(3)

        # Krok 7: Zamknięcie komunikatu o cookie
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "157", "1410"], check=True)

        return True

    except subprocess.CalledProcessError as error:
        logger.error(f"Błąd podczas wykonywania komendy: {error}")
        return False

def website_session_domodeo():
    """
    Symuluje interakcję ze stroną internetową poprzez symulację kliknięć i przewijania
    używając adb (Android Debug Bridge)
    """
    x = 720
    y = 1600

    try:
        # Losowo wybieramy jedną z dwóch opcji kliknięcia
        if random.choice([True, False]):
            subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", str(x * 0.25), str(y * 0.75)], check=True)
            time.sleep(random.uniform(2, 5))
        else:
            subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", str(x * 0.75), str(y * 0.75)], check=True)
            time.sleep(random.uniform(2, 5))

        # Pętla symulująca przewijanie strony oraz dodatkowe kliknięcia
        for j in range(5):
            # Trzykrotne przewinięcie strony
            for i in range(3):
                subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "swipe", "300", "800", "300", "250"], check=True)
            time.sleep(random.uniform(2, 5))

            # Dwa kliknięcia w określonych współrzędnych
            for i in range(2):
                subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", str(x * 0.5), str(y * (0.5 + i * 0.2))], check=True)
            time.sleep(random.uniform(2, 5))
            
        return True
    except Exception as e:
        logger.error(f"Wystąpił błąd: {e}")
        return False
    
def visit_website_rattanart(url="www.rattanart.pl/products/maty-i-oslony-balkonowe/"):
    """
    Otwiera przeglądarkę Chrome w trybie incognito i odwiedza podany adres URL.

    """
    try:
        # Krok 1: Uruchomienie Chrome
        subprocess.run([
            "adb", "-s", DEVICE_ID, "shell", "am", "start",
            "-n", "com.android.chrome/com.google.android.apps.chrome.Main",
        ], check=True)
        time.sleep(2)  # odczekaj, aż przeglądarka się załaduje

        # Krok 2: Wywołanie menu (keyevent 82)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "keyevent", "82"], check=True)

        # Krok 3: Symulacja kliknięcia w opcję "Nowa karta incognito"
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "450", "310"], check=True)

        # Krok 4: Kliknięcie w pasek adresu 
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "308", "113"], check=True)

        # Krok 5: Wpisanie URL
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "text", url], check=True)

        # Krok 6: Naciśnięcie Enter (keyevent 66)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "keyevent", "66"], check=True)
        time.sleep(3)

        # Krok 7: Zamknięcie komunikatu o cookie
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "415", "1465"], check=True)

        return True

    except subprocess.CalledProcessError as error:
        logger.error(f"Błąd podczas wykonywania komendy: {error}")
        return False

def website_session_rattanart():
    """
    Symuluje interakcję ze stroną internetową poprzez symulację kliknięć i przewijania
    używając adb (Android Debug Bridge).
    """
 
    y_coords = [1193, 1288, 1395, 1490]
    random_y = random.choice(y_coords)

    try:
        # Pętla symulująca przewijanie strony oraz dodatkowe kliknięcia
        for j in range(3):

            for i in range(8):
            # Przewinięcie strony
                subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "swipe", "300", "1200", "300", "250"], check=True)
                time.sleep(random.uniform(1, 2))

            
            # Do góry strony    
            subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "350", "1410"], check=True)
            time.sleep(random.uniform(1, 2))

            # Produkty
            subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "350", "962"], check=True)
            time.sleep(random.uniform(3, 5))
            subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "350", str(random_y)], check=True)
            time.sleep(random.uniform(3, 5))

        return True
    except Exception as e:
        logger.error(f"Wystąpił błąd: {e}")
        return False
    
def visit_website_matanalata(url="www.matanalata.pl"):
    """
    Otwiera przeglądarkę Chrome w trybie incognito i odwiedza podany adres URL.

    """
    try:
        # Krok 1: Uruchomienie Chrome
        subprocess.run([
            "adb", "-s", DEVICE_ID, "shell", "am", "start",
            "-n", "com.android.chrome/com.google.android.apps.chrome.Main",
        ], check=True)
        time.sleep(2)  # odczekaj, aż przeglądarka się załaduje

        # Krok 2: Wywołanie menu (keyevent 82)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "keyevent", "82"], check=True)

        # Krok 3: Symulacja kliknięcia w opcję "Nowa karta incognito"
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "450", "310"], check=True)

        # Krok 4: Kliknięcie w pasek adresu 
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "308", "113"], check=True)

        # Krok 5: Wpisanie URL
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "text", url], check=True)

        # Krok 6: Naciśnięcie Enter (keyevent 66)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "keyevent", "66"], check=True)
        time.sleep(3)

        # Krok 7: Zamknięcie komunikatu o cookie
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "96", "1424"], check=True)

        return True

    except subprocess.CalledProcessError as error:
        logger.error(f"Błąd podczas wykonywania komendy: {error}")
        return False

def website_session_matanalata():
    """
    Symuluje interakcję ze stroną internetową poprzez symulację kliknięć i przewijania
    używając adb (Android Debug Bridge).
    """
    # Lista współrzędnych (x, y)
    coordinates_main = [
        (170, 1090),
        (540, 1100),
        (160, 1300),
        (525, 1285),
        (170, 1455)
    ]

    coordinates_sub = [
        (160, 925),
        (515, 945),
        (150, 1200),
    ]

    try:
        # Pętla sesji
        for j in range(5):

            # Losowy wybór jednej pary współrzędnych
            x1, y1 = random.choice(coordinates_main)
            x2, y2 = random.choice(coordinates_sub)

            # Klik w produkty główny
            subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", str(x1), str(y1)], check=True)
            time.sleep(random.uniform(3, 5))

            # Klik w sub produkt
            subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", str(x2), str(y2)], check=True)
            time.sleep(random.uniform(3, 5))

            #Strona główna
            subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "350", "305"], check=True)
            time.sleep(random.uniform(3, 5))

        return True
    except Exception as e:
        logger.error(f"Wystąpił błąd: {e}")
        return False

def close_all_incognito_tabs():
    """
    Rozwija górne menu poprzez przytrzymanie (long press)
    i klika opcję "Zamknij wszystkie karty incognito".

    Zwraca:
        bool: True, jeżeli operacja przebiegła pomyślnie, False w przypadku wystąpienia błędu.
    """
    try:
        # Krok 1: Przytrzymaj górne menu, aby je rozwinąć (używając long press)
        # Używamy komendy "swipe" z tą samą pozycją startową i końcową oraz z określonym czasem trwania (ms)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "swipe", "310", "22", "385", "1138", "1000"], check=True)
        time.sleep(1)
        
        # Krok 2: Kliknięcie opcji "Zamknij wszystkie karty incognito" (przykładowe współrzędne)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "370", "1080"], check=True)
        time.sleep(1)

        # Krok 3: Zamknięcie przeglądarki tak, aby był tylko ekran startowy
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "539", "1550"], check=True)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "tap", "366", "1280"], check=True)
        
        return True
    except subprocess.CalledProcessError as error:
        logger.error(f"Błąd podczas wykonywania komendy: {error}")
        return False

def wake_up_device():
    try:
        # Wybudzanie telefonu:
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "keyevent", "26"], check=True)
        subprocess.run(["adb", "-s", DEVICE_ID, "shell", "input", "swipe", "300", "1000", "300", "500"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False
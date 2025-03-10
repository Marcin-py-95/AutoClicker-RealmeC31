# import subprocess
# import time
# import random
# import functions as f
# # -----------------------------TO DZIALA CALY CZAS - dopisz device_id------------------------------
# iteration = 0
# DEVICE_ID = "0A62414I29101934"
# # while True:
# iteration += 1
# # Włączenie trybu samolotowego
# subprocess.run(["adb", "-s", DEVICE_ID, "shell", "settings", "put", "global", "airplane_mode_on", "1"])
# subprocess.run(["adb", "-s", DEVICE_ID, "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "true"])
# time.sleep(2)

#     # otworz karte incognito - ruch na stronie - zamknij karte incognito
#     # f.visit_website()
#     # f.website_session()
#     # f.close_all_incognito_tabs()

# # Wyłączenie trybu samolotowego:
# # subprocess.run(["adb", "-s", DEVICE_ID, "shell", "settings", "put", "global", "airplane_mode_on", "0"])
# # subprocess.run(["adb", "-s", DEVICE_ID, "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "false"])
# # time.sleep(3)
#     # print(f'\033[1;33m*** Zakończono pętlę nr {iteration}. Następna iteracja za chwilę. ***\033[0m')

import subprocess
import time
import datetime
import random
import functions as f
import logger

# Inicjalizacja loggera
logger.setup_logger()

DEVICE_ID = "0A62414I29101934"

# Liczba wejść na każdą stronę
DOMODEO_VISITS = 400
RATANART_VISITS = 60
MATANALATA_VISITS = 100
DAILY_GROWTH = 0.05  # 5% wzrost dziennie

def run_iteration(site):
    """Wykonuje wizytę na określonej stronie."""
    logger.info(f"*** Odwiedzanie strony {site} ***")
    
    # Wyłączenie trybu samolotowego
    subprocess.run(["adb", "-s", DEVICE_ID, "shell", "cmd", "connectivity", "airplane-mode", "disable"])
    time.sleep(3)

    # Wybudz urządzenie
    f.wake_up_device()
    
    # Akcje w przeglądarce dla odpowiedniej strony
    if site == "domodeo":
        f.visit_website_domodeo()
        f.website_session_domodeo()
    elif site == "ratanart":
        f.visit_website_rattanart()
        f.website_session_rattanart()
    elif site == "matanalata":
        f.visit_website_matanalata()
        f.website_session_matanalata()
        
    f.close_all_incognito_tabs()
    
    # Włączenie trybu samolotowego
    subprocess.run(["adb", "-s", DEVICE_ID, "shell", "cmd", "connectivity", "airplane-mode", "enable"])
    
    logger.info(f"*** Zakończono odwiedzanie strony {site} ***")

def run_continuous_mode():
    """Tryb ciągły: od 7:00 do 18:00."""
    # Liczniki odwiedzin
    domodeo_count = 0
    ratanart_count = 0
    matanalata_count = 0
    
    logger.info("Tryb ciągły: działanie od 7:00 do 18:00")
    logger.info(f"Cele na dziś: domodeo={DOMODEO_VISITS}, ratanart={RATANART_VISITS}, matanalata={MATANALATA_VISITS}")
    
    # Całkowita liczba wejść
    total_visits = DOMODEO_VISITS + RATANART_VISITS + MATANALATA_VISITS
    
    # Liczba sekund pracy (11 godzin)
    work_seconds = 11 * 3600
    
    # Średni czas pomiędzy wizytami
    avg_time_between_visits = work_seconds / total_visits
    
    # Utwórz listę wizyt w odpowiednich proporcjach
    visit_schedule = []
    for _ in range(DOMODEO_VISITS):
        visit_schedule.append("domodeo")
    for _ in range(RATANART_VISITS):
        visit_schedule.append("ratanart")
    for _ in range(MATANALATA_VISITS):
        visit_schedule.append("matanalata")
    
    # Pomieszaj listę, aby wizyty były rozłożone w czasie
    random.shuffle(visit_schedule)
    
    # Wykonuj wizyty według harmonogramu
    for site in visit_schedule:
        now = datetime.datetime.now().time()
        
        # Jeśli czas się zmienił poza zakres, przerywamy tryb ciągły
        if now < datetime.time(7, 0) or now >= datetime.time(18, 0):
            break
            
        # Odwiedź stronę
        run_iteration(site)
        
        # Aktualizacja liczników
        if site == "domodeo":
            domodeo_count += 1
            logger.info(f"Domodeo: {domodeo_count}/{DOMODEO_VISITS}")
        elif site == "ratanart":
            ratanart_count += 1
            logger.info(f"Ratanart: {ratanart_count}/{RATANART_VISITS}")
        elif site == "matanalata":
            matanalata_count += 1
            logger.info(f"Matanalata: {matanalata_count}/{MATANALATA_VISITS}")
            
        # Czas oczekiwania z lekką wariancją (±20%)
        sleep_time = avg_time_between_visits * random.uniform(0.8, 1.2)
        logger.info(f"Oczekiwanie {sleep_time:.2f} sekund przed następną wizytą")
        time.sleep(sleep_time)
        
    logger.info("Zakończono wszystkie zaplanowane wizyty na dziś")

def sleep_until(target_time):
    """Usypia program do podanego target_time (datetime.datetime) i wybudza telefon po przebudzeniu."""
    now = datetime.datetime.now()
    sleep_duration = (target_time - now).total_seconds()
    
    if sleep_duration > 0:
        logger.info(f"Usypianie programu na {int(sleep_duration)} sekund...")
        time.sleep(sleep_duration)
        f.wake_up_device()

def update_daily_targets():
    """Aktualizuje dzienne cele o 5%."""
    global DOMODEO_VISITS, RATANART_VISITS, MATANALATA_VISITS
    
    DOMODEO_VISITS = int(DOMODEO_VISITS * (1 + DAILY_GROWTH))
    RATANART_VISITS = int(RATANART_VISITS * (1 + DAILY_GROWTH))
    MATANALATA_VISITS = int(MATANALATA_VISITS * (1 + DAILY_GROWTH))
    
    logger.info(f"Zaktualizowano dzienne cele: domodeo={DOMODEO_VISITS}, ratanart={RATANART_VISITS}, matanalata={MATANALATA_VISITS}")

if __name__ == '__main__':
    last_date = datetime.datetime.now().date()
    
    while True:
        try:
            now = datetime.datetime.now()
            current_time = now.time()
            
            # Sprawdź, czy jest nowy dzień, jeśli tak, zaktualizuj cele
            if now.date() > last_date:
                update_daily_targets()
                last_date = now.date()
            
            # Tryb ciągły: od 7:00 do 18:00
            if datetime.time(7, 0) <= current_time < datetime.time(18, 0):
                run_continuous_mode()
                continue
                
            # Po 18:00 do 7:00 - program nie wykonuje operacji, czeka do kolejnego dnia
            else:
                next_run = datetime.datetime.combine(now.date(), datetime.time(7, 0))
                if current_time >= datetime.time(18, 0):
                    next_run += datetime.timedelta(days=1)
                sleep_until(next_run)
                continue
                
        except Exception as e:
            logger.error(f"Wystąpił błąd w głównej pętli: {e}")
            # Dodaj krótki czas oczekiwania przed ponowną próbą
            time.sleep(60)
            continue
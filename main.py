import time
import requests

TOKEN = "ISI_TELEGRAM_BOT_TOKEN"
CHAT_ID = "ISI_CHAT_ID"

seen = set()

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_bounties():
    try:
        r = requests.get("https://pump.fun/api/bounties", timeout=10)
        return r.json().get("bounties", [])
    except:
        return []

while True:
    bounties = get_bounties()

    for b in bounties:
        bid = b.get("id")

        if bid and bid not in seen:
            seen.add(bid)

            msg = f"NEW BOUNTY\n{b.get('title')}\nReward: {b.get('reward')}"
            send(msg)

            print("sent:", bid)

    time.sleep(10)

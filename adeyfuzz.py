import requests
import time
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6"
}
time_now = datetime.now().strftime("%H:%M:%S")


def adeyfuzz(url):
    with open("adeyfuzz.txt", "r", encoding="UTF-8") as fuzz:
        for i in fuzz.readlines():
            i = i.strip()
            try:
                url1 = url + i
                print(f"[{time_now}] ", url1, end="\n\n")
                r = requests.get(url=url1, headers=headers).status_code
                print(r)
            except:
                continue

import requests
import time
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6"
}
time_now = datetime.now().strftime("%H:%M:%S")


def Dirscan(url, dicto):
    with open(dicto, "r", encoding="UTF-8") as f:
        for i in f.readlines():
            i = i.strip()
            try:
                r = requests.get(url=url + i, headers=headers)
                if r.status_code == 200:
                    print(f"[{time_now}]" + "[url]:", r.url)
            except:
                continue

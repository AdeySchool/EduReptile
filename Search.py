import requests
from lxml import etree
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6"
}
time_now = datetime.now().strftime("%H:%M:%S")


def search(url, eduname):
    html = requests.get(url=url, headers=headers).text.encode("UTF-8")
    io = etree.HTML(html)
    serchedu = io.xpath("//cite/text()")
    listeduwz = list(serchedu)
    print(f"[{time_now}] 官网：" , listeduwz[0])

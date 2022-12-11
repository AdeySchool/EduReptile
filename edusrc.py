import requests
from lxml import etree
import time
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6"
}
time_now = datetime.now().strftime("%H:%M:%S")


def main0(url):
    html = requests.get(url=url, headers=headers).text.encode("UTF-8")
    ao = etree.HTML(html)
    edusrcwz = ao.xpath("//td[2]/a/text()")
    edulist = list(edusrcwz)
    for i in edulist:
        print(f"[{time_now}]", i.strip())

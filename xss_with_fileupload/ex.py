import requests as req

url = "https://f242-118-34-210-41.ngrok-free.app/"
header = {"ngrok-skip-browser-warning": "ANY_VALUE"}

res = req.get(url=url, headers=header)

print(res.text)

# from datetime import datetime
# from time import sleep
# print(datetime.now())
# sleep(10)
# print(datetime.now())

from datetime import datetime
import requests
from time import sleep
response = requests.get("https://github.com")
if response.status_code == 200:
    print("github is ok")
print(datetime.now())
sleep(10)
print(datetime.now())
print("check it updates, adding for 261221")
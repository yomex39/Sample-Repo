import requests
import os

print("Yomi is good")

r = requests.get("https://jw.org")
print(r.status_code)

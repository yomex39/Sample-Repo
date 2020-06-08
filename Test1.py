import os
import sys

import requests

print(sys.executable)

r = requests.get("https://jw.org")
print(r.status_code)

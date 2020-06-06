import math
import os
import sys
from os import times

import requests

print("Yomi is good")

r = requests.get("https://jw.org")
print(r.status_code)

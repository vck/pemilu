import sqlite3 as sql
from requests import get
from bs4 import BeautifulSoup
import re

URL = "http://wikidpr.org/anggota/{}"

error = False

N_CANDIDAT = 1

while not error:
   req = get(URL)
   
   if req.status == 200:
      print(f"candidate: {N_CANDIDAT} status: OK")
   else:
      print(f"candidate: {N_CANDIDAT} status: error not found")


from requests import get
from bs4 import BeautifulSoup as bs

URL = "http://wikidpr.org/anggota/{}"

def get_candidate_data(candidate_id: str):
   req = get(URL.format(candidate_id))
   html = req.text
   soup = bs(html, "html.parser")
   text = soup.text
   parsed_text = [text for text in soup.text.split()]
   return parsed_text

def main():
   for i in range(1000):
      print(get_candidate_data(i))

if __name__ == "__main__":
   main()


   
   
   

 

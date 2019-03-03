from requests import get
from bs4 import BeautifulSoup as bs
from config import engine
from model import Base, CandidateRawData, Session

session = Session()

Base.metadata.create_all(engine)

URL = "http://wikidpr.org/anggota/{}"

def get_candidate_data(candidate_id: int):
   req = get(URL.format(candidate_id))
   html = req.text
   soup = bs(html, "html.parser")
   text = soup.text
   parsed_text = [text for text in soup.text.split()]
   return " ".join(parsed_text)

def test(candidate_id: int):
   isinstance(get_candidate_data(candidate_id), list) == True 

def scrap_candidate_page():

	n = 1
	while True:
		print(f"scrapping candidate_id={n}")
		raw1 = CandidateRawData(raw_data=get_candidate_data(n))
		session.add(raw1)
		session.commit()
		n += 1
		print("done...")
		print()

if __name__ == "__main__":
	scrap_candidate_page()

   
   
   

 

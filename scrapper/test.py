from config import engine
from model import Base, CandidateRawData, Session

session = Session()

Base.metadata.create_all(engine)

raw1 = CandidateRawData(raw_data="testttttt")
session.add(raw1)
session.commit()

for item in session.query(CandidateRawData).all():
	print(item.candidate_id, item.raw_data)
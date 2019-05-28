from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import time
import json
import house.settings
from house.house_model import House

engine = create_engine("mysql+pymysql://root:macbook@localhost:3306/spider", max_overflow=5)
Base = declarative_base()
time_string = time.strftime("%Y%m%d", time.localtime())

#创建单表
class House(Base):
	__tablename__ = time_string
	id = Column(Integer, primary_key=True)
	title = Column(String(64))
	link = Column(String(64))
	area = Column(String(64))
	location = Column(String(64))
	totalPrice = Column(String(64))
	unitPrice = Column(String(64))
	flood = Column(String(64))
	follow = Column(String(64))
	tag1 = Column(String(64))
	tag2 = Column(String(64))

def init_db():
	Base.metadata.create_all(engine)

def drop_db():
	Base.metadata.drop_all(engine)
	
def insert_data_many(insert_data):
	Session = sessionmaker(bind=engine)
	session = Session()
	session.add_all(insert_data)
	session.commit()


def insert_data_one_by_one(insert_data):
	Session = sessionmaker(bind=engine)
	session = Session()
	session.add(insert_data)
	session.commit()


if __name__ == '__main__':
	# def create_db():
	# hous_s = House()
	# hous_s.title = "title"
	# hous_s.area = "area"
	# insert_data_one_by_one(hous_s)
    init_db()
    # data = read_json("./data/20190520_hours.json")
    # insert_data(data)
    
    
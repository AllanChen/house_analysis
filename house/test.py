from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import time
import json
import house.settings

engine = create_engine("mysql+pymysql://root:macbook@localhost:3306/spider", max_overflow=5)
Base = declarative_base()
time_string = time.strftime("%Y%m%d", time.localtime())

# 创建单表
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
    
#定义初始化数据库函数
def init_db():
    Base.metadata.create_all(engine)

#顶固删除数据库函数
def drop_db():
    Base.metadata.drop_all(engine)
    
def insert_data(data_json):
	insert_data = []
	Session = sessionmaker(bind=engine)
	session = Session()
	for item in data_json:
		insert_data.append(
			House(
				title = item['title'],
				link = item['link'],
				area = item['area'],
				location = item['location'],
				totalPrice = item['totalPrice'],
				unitPrice = item['unitPrice'],
				# flood = item['flood'],
				follow = item['follow'],
				# tag1 = item['tag1'],
				# tag2 = item['tag']
			)
		)
	session.add_all(insert_data)
	session.commit()

init_db()

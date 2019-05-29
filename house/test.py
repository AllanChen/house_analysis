from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
import codecs
import house.settings

engine = create_engine("mysql+pymysql://root:zPSsZYtmmjAJAcjR@39.105.97.84:3306/house", max_overflow=5)
Base = declarative_base()
tb_name = "20190525_21"


class House(Base):
    __tablename__ = tb_name
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


def txt_to_json(name):
    # txt_name = name + ".txt"
    # with open(txt_name, 'r', encoding='utf-8') as file:
    #     data = file.read()
    #
    # data = "[" + data
    # data = data + "]"
    # data = data.replace(",]", "]")
    json_save_name = "./data/" + name + "_hours.json"
    # file = codecs.open(json_save_name, 'wb', 'utf-8')
    # file.write(data)

    insert_data = []
    with open(json_save_name, 'r', encoding='utf-8') as f:
        data_json = json.load(f)
        f.close()

        for house in data_json:
            insert_h = House()
            insert_h.title = house['title']
            insert_h.link = house['link']
            insert_h.area = house['area']
            insert_h.location = house['location']
            insert_h.totalPrice = house['totalPrice']
            insert_h.unitPrice = house['unitPrice']
            # insert_h.flood = house['flood']
            insert_h.follow = house['follow']
            # insert_h.tag1 = house['tag1']
            # insert_h.tag2 = house['tag2']
            insert_data.append(insert_h)

    insert_data_many(insert_data)


if __name__ == '__main__':
    # def create_db():
    # hous_s = House()
    # hous_s.title = "title"
    # hous_s.area = "area"
    # insert_data_one_by_one(hous_s)
    init_db()
    # txt_to_json(tb_name)
# data = read_json("./data/20190520_hours.json")
# insert_data(data)

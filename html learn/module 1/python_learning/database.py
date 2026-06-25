from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///users.db")
Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)

class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    age=Column(Integer)
    city=Column(String)

Base.metadata.create_all(engine)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB setup
engine = create_engine('sqlite:///gym.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

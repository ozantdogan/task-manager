from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os
import messages

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database')
os.makedirs(DATABASE_PATH, exist_ok=True)
DATABASE_URI = os.environ.get('DATABASE_URI') or f'sqlite:///{os.path.join(DATABASE_PATH, "tasks.db")}'

def connect_db():
    try:
        engine = create_engine(DATABASE_URI)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as e:
        print(messages.DATABASE_CONNECTION_ERROR, e)
        return None

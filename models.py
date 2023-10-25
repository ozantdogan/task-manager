import uuid
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
    createdon = Column(DateTime, default=func.now())
    modifiedon = Column(DateTime, default=None, onupdate=func.now())
    parent_id = Column(Integer, default=None)

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', description='{self.description}', is_completed={self.is_completed})>"
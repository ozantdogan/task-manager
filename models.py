from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
    createdon = Column(DateTime, default=func.now())
    modifiedon = Column(DateTime, default=None, onupdate=func.now())

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', description='{self.description}', is_completed={self.is_completed})>"
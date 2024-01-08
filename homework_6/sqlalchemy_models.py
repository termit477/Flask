from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Boolean


Base = declarative_base()


class Task2(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Boolean, default=False)


class Task2(Base):
    __tablename__ = 'tasks2'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    done = Column(Boolean, default=False)
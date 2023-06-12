from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    top_left_x = Column(Integer)
    top_left_y = Column(Integer)
    width = Column(Integer)
    height = Column(Integer)
    confidence = Column(Float)
    label = Column(Integer)

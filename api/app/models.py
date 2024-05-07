from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Foody(Base):
    __tablename__ = "foody"

    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255))
    Address = Column(String(255))
    Phone = Column(String(50))
    Image = Column(String(255))
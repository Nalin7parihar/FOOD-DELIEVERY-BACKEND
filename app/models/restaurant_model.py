from sqlalchemy import Column, Integer, String, ForeignKey,Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
import enum

class RestaurantStatus(str,enum.Enum):
  OPEN = "open"
  CLOSED = "closed"


class Restaurant(Base):
  __tablename__ = 'restaurants'
  
  id=  Column(Integer,primary_key=True,index=True)
  name = Column(String(100),nullable=False,index=True)
  description = Column(String(255),nullable=False)
  address = Column(String(255),nullable=False)
  phone = Column(String(15),nullable=False,unique=True)
  status = Column(Enum(RestaurantStatus),nullable=False,default=RestaurantStatus.OPEN)
  
  owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  
  owner = relationship("User", back_populates="restaurants")
  

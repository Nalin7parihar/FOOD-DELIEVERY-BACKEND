from sqlalchemy import Column, Integer, String, ForeignKey,Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
import enum

from geoalchemy2 import Geometry

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
  
  #Geospatial Data
  location = Column(Geometry(geometry_type='POINT',srid=4326),index=True)
  
  status = Column(Enum(RestaurantStatus),nullable=False,default=RestaurantStatus.OPEN)
  
  owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  
  #relationships
  menu_items = relationship("MenuItem", back_populates="restaurant",cascade="all, delete-orphan")
  owner = relationship("User", back_populates="restaurants")
  orders = relationship("Order", back_populates="restaurant")
  

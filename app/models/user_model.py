from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
import enum

class UserRole(str, enum.Enum):
  ADMIN = "admin"
  CUSTOMER = "customer"
  DRIVER = "driver"
  RESTAURANT = "restaurant"

class User(Base):
  
  __tablename__ = 'users'
  
  id = Column(Integer,primary_key=True,index=True)
  email = Column(String,nullable=False,unique=True,index=True)
  hashed_password = Column(String,nullable=False,unique=False,index=True)
  role = Column(Enum(UserRole),nullable=False,default=UserRole.CUSTOMER)
  is_active = Column(Boolean,default=True)
  
  #RelationShips
  restaurants = relationship("Restaurant",back_populates="owner")
  
  __mapper_args__ = {
      'polymorphic_identity': 'user',
      'polymorphic_on': role
  }
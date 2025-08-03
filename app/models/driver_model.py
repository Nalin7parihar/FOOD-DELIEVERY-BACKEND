from sqlalchemy import Column,Integer,ForeignKey,String,Boolean,Enum
import enum
from sqlalchemy.orm import relationship
from .user_model import User, UserRole

class DriverRole(str, enum.Enum):
  OFFLINE = "offline"
  AVAILABLE=  "available"
  BUSY = "busy"
  
  
  
class Driver(User):
  __tablename__ = 'drivers'
  
  id = Column(Integer,ForeignKey('users.id'),primary_key=True)
  name = Column(String, nullable=False,index=True)
  age = Column(Integer, nullable=False)
  phone = Column(Integer, nullable=False,unique=True)
  license_number = Column(String,nullable=False,unique=True)
  
  __mapper_args__ = {
    'polymorphic_identity': UserRole.DRIVER,
  }
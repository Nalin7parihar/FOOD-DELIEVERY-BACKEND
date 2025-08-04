from sqlalchemy import Column,Integer,ForeignKey,String,Enum
import enum
from sqlalchemy.orm import relationship
from .user_model import User, UserRole

class DriverStatus(str, enum.Enum):
  OFFLINE = "offline"
  AVAILABLE=  "available"
  BUSY = "busy"
  
  
  
class Driver(User):
  __tablename__ = 'drivers'
  
  id = Column(Integer,ForeignKey('users.id'),primary_key=True)
  name = Column(String, nullable=False,index=True)
  age = Column(Integer, nullable=False)
  phone = Column(String(20), nullable=False,unique=True)
  license_number = Column(String,nullable=False,unique=True)
  driver_status = Column(Enum(DriverStatus),nullable=False,default=DriverStatus.OFFLINE)
  #relationships
  orders = relationship("Order", back_populates="driver")
  
  
  __mapper_args__ = {
    'polymorphic_identity': UserRole.DRIVER,
  }
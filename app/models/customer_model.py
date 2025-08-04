from sqlalchemy import Column, Integer, String,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from .user_model import User,UserRole

class Customer(User):
  __tablename__ = 'customers'
  
  id = Column(Integer,ForeignKey('users.id'),primary_key=True)
  name = Column(String,nullable=False,index=True)
  age = Column(Integer,nullable=False)
  phone = Column(String(20),nullable=False,unique=True)
  address = Column(String,nullable=False)
  state = Column(String,nullable=False)
  country = Column(String,nullable=False)
  
  __mapper_args__ = {
      'polymorphic_identity': UserRole.CUSTOMER,
  }
  
  #Relationships 
  orders = relationship("Order", back_populates="customer")
   
  
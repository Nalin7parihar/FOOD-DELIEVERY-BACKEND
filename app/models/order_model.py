from sqlalchemy import Column, Integer, String, ForeignKey,Enum,DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base
from sqlalchemy.sql import func
import enum


class OrderStatus(str,enum.Enum):
  PENDING = "pending"
  ACCEPTED = "accepted"
  PREPARING = "preparing"
  OUT_FOR_DELIVERY = "out_for_delivery"
  COMPLETED = "completed"
  CANCELLED = "cancelled"
class Order(Base):
  __tablename__ = 'orders'
  
  id = Column(Integer,primary_key=True,index=True)
  customer_id = Column(Integer,ForeignKey('customers.id'),nullable=False)
  driver_id = Column(Integer,ForeignKey('drivers.id'),nullable=True)
  restaurant_id = Column(Integer,ForeignKey('restaurants.id'),nullable=False)
  delivery_address = Column(String(255),nullable=False)
  delievery_charges = Column(Integer,nullable=False)
  tax_amount = Column(Integer,nullable=False)
  status = Column(Enum(OrderStatus), nullable=False, default=OrderStatus.PENDING)
  total_amount = Column(Integer,nullable=False)
  
  #TimeSTamps
  created_at = Column(DateTime(timezone=True),server_default=func.now())
  updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())
  
  #relationships
  customer = relationship("Customer", back_populates="orders")
  driver = relationship("Driver", back_populates="orders")
  restaurant = relationship("Restaurant", back_populates="orders")
  
  #this links the order to its menu items
  items = relationship("OrderItem",back_populates="order")
  
  
  
  
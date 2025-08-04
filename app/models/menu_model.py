from sqlalchemy import Column, Integer, String, ForeignKey,Float,Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base


class MenuItem(Base):
  __tablename__ = 'menu_items'
  
  id = Column(Integer,primary_key=True,index=True)
  dish = Column(String(100),nullable=False,index=True)
  description = Column(String(255),nullable=False)
  price = Column(Float,nullable=False)
  is_vegetarian = Column(Boolean,default=False)
  restaurant_id = Column(Integer,ForeignKey('restaurants.id'),nullable=False)
  is_available = Column(Boolean,default=True)
  category = Column(String(50),nullable=False)
  image_url = Column(String(255),nullable=True)
  
  
  #Relationships
  restaurant = relationship("Restaurant",back_populates="menu_items")
  order_items = relationship("OrderItem",back_populates="menu_item")
  
  


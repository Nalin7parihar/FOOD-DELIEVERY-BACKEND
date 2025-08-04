from app.db.session import Base
from sqlalchemy import Column,Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class OrderItem(Base):
  __tablename__ = 'order_items'
  
  id = Column(Integer, primary_key=True, index=True)
  quantity = Column(Integer, nullable=False)
  price_per_item = Column(Float, nullable=False)
  order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
  menu_item_id = Column(Integer, ForeignKey('menu_items.id'), nullable=False)

  # relationships
  order = relationship("Order", back_populates="items")
  menu_item = relationship("MenuItem",back_populates="order_items")
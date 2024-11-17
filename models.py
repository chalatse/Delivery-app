from database import Base
from sqlalchemy import Column,Integer,String,Boolean,Text
from sqlalchemy.types import ChoiceType # type: ignore

class User(Base):
    __table__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(25),unique=True)
    email=Column(String(80),unique=True)
    password=Column(Text,nullable=True)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)


    def  __repr__(self):
        return f"<User {self.username}"
    

class Choice(Base):
    ORDER_STATUS=(
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered')
    )

    __table__='orders'
    id=Column(Integer,primary_key=True)
    quantity=Column(Integer,nullable=False)
    order_status=Column(ChoiceType(Choices=ORDER_STATUS), default="PENDING")
    
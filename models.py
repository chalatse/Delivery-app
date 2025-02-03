from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String


class User:
    __tablename__='user'
    id=Column(Integer, primary_key=True)
    username=Column(String(25), unique=True)
    email=Column(String(80), unique=True)
    password=Column(Text, nullable=True)
    is_staff=Column(Boolean, default=False)
    is_active=Column(Boolean,default=False)


    def __repr__(self):
        return f"<User {self.username}"
    

class Choice(Base):

    ORDER_STATUSES=(
        ('PENDING','pending')
        ('IN-TRANSIT','in-transit')
        ('DELIVERED','delivered')        
    )
    __tablename__='orders'
    id=Column(Integer, primary_key=True)
    quantity=Column(Integer, nullable=False)



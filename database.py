from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine= create_engine("jdbc:postgresql://localhost:5432/postgres/delivery",
                      echo=True
)
Base=declarative_base()
session=sessionmaker()

from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import date
from decimal import Decimal
from sqlalchemy import create_engine

class Subscription(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal

class Payments(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscription_id: int = Field(foreign_key='subscription.id')
    subscription: Subscription = Relationship(back_populates='payments')
    date: date

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)


Subscription.payments: Optional[list[Payments]] = Relationship(back_populates="subscription") # type: ignore
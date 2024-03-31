import asyncio

from sqlalchemy import ARRAY, DATE, Boolean, Column, ForeignKey, Integer, Text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# psycopg


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    form_complete = Column(Boolean, nullable=False)
    form_data = relationship('Form', back_populates='user')


class Form(Base):
    __tablename__ = 'form'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Boolean, nullable=False)
    date_born = Column(DATE, nullable=False)
    user = relationship('User', back_populates='form_data')


class Subscribe(Base):
    __tablename__ = 'subscribe'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    date_sub = Column(DATE, nullable=False)
    level_sub = Column(Integer, nullable=False)


class Horo(Base):
    __tablename__ = 'horo'

    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    horo_arr = Column(ARRAY(Text), nullable=False)


# dialect+driver://username:password@host:port/database
async_engine = create_async_engine(url="postgresql+asyncpg://horo_tg:1111qwert@localhost:5432/horo_tg", echo=True
                                   # pool_size=5,
                                   # max_overflow=10)
                                   )


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_tables())
# engine.connect()
# print(Base.metadata.create_all(engine))
print(async_engine)

# Rename to models.py

import asyncio

import sqlalchemy.types as types
from sqlalchemy import (ARRAY, Boolean, Column, Date, ForeignKey,
                        Integer, String, Text)
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

STRING_MAX_LENGTH = 64

Base = declarative_base()


class ChoiceType(types.TypeDecorator):
    impl = types.String

    def __init__(self, choices, **kw):
        self.choices = dict(choices)
        super(ChoiceType, self).__init__(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.iteritems() if v == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]


class User(Base):
    __tablename__ = 'user'

    first_name = Column(String, nullable=False, length=STRING_MAX_LENGTH)
    second_name = Column(String, nullable=False, length=STRING_MAX_LENGTH)
    last_name = Column(String, nullable=False, length=STRING_MAX_LENGTH)
    date_of_birth = Column(Date, nullable=False, )
    gender = Column(
        ChoiceType(
            {'M': 'Male',
             'F': 'Female'}
        ),
        nullable=False
    )
    form_data = relationship('Form', back_populates='user')


class FormStatus(Base):
    __tablename__ = 'form_status'
    form = relationship('Form', back_populates='')
    form_complete = Column(Boolean, nullable=False)


class Form(Base):
    __tablename__ = 'form'

    user = relationship('User', back_populates='form_data')
    form_status = Column()


class Subscribe(Base):
    __tablename__ = 'subscribe'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    date_sub = Column(Date, nullable=False)
    level_sub = Column(Integer, nullable=False)


class Horo(Base):
    __tablename__ = 'horo'

    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    horo_arr = Column(ARRAY(Text), nullable=False)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_user(user_data: dict):
    """
    Добавляет пользователя с заданными данными в базу данных.
    :param user_data: Словарь с данными пользователя.
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Создание нового экземпляра пользователя
            new_user = User(**user_data)
            session.add(new_user)
        await session.commit()
        return new_user


async def update_form_complete(user_id: int, form_complete: bool):
    """
    Обновляет статус form_complete для пользователя с указанным user_id.
    :param user_id: ID пользователя.
    :param form_complete: Новое значение для поля form_complete.
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Запрос пользователя по ID
            query = select(User).where(User.user_id == user_id)
            result = await session.execute(query)
            user = result.scalars().first()
            if user:
                # Обновление поля form_complete
                user.form_complete = form_complete
                await session.commit()
                return True
            else:
                return False


# dialect+driver://username:password@host:port/database
async_engine = create_async_engine(
    url="postgresql+asyncpg://horo_tg:1111qwert@localhost:5432/horo_tg",
    echo=True)
AsyncSessionLocal = async_sessionmaker(async_engine, class_=AsyncSession,
                                       expire_on_commit=False)


# async def foo(some:types.FunctionType):
#     AsyncSessionLocal = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
#     # создаем транзакцию
#     async with AsyncSessionLocal() as s:
#         some_do(some)
#     await s.commit()

class CRUD:
    def __init__(self):
        pass

    async def create_user(self, user_data: dict):
        """Добавляет нового пользователя в базу данных."""
        async with AsyncSessionLocal() as session:
            async with session.begin():
                new_user = User(**user_data)
                session.add(new_user)
            await session.commit()
            return new_user

    async def get_user(self, user_id: int):
        """Получает информацию о пользователе по ID."""
        async with AsyncSessionLocal() as session:
            async with session.begin():
                result = await session.execute(
                    select(User).where(User.user_id == user_id))
                user = result.scalars().first()
            return user


async def main():
    crud = CRUD()

    # Создание таблиц
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(main())

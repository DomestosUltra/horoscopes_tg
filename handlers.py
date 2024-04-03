from aiogram import F, Router, types
from aiogram.filters.command import Command, CommandStart
from aiogram.filters.state import State, StateFilter, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

import keyboards
from handlers_form import FORM

router = Router()

# form format:
# - Дата рождения
# - Имя
# - Пол
# - Интересующие категории


class MAINSTATES(StatesGroup):
    horo = State()
    form = State()
    subs = State()
    rate = State()


@router.message(CommandStart())
async def get_user_id(message: types.Message):
    user_id = message.chat.id
    form_complete = 0
    date_complete = message.date
    await message.answer(text=f'id: {user_id}\n'
                              f'date: {date_complete}\n'
                              f'form_complete: {form_complete}')


@router.message(StateFilter(default_state))
async def echo_main(message: types.Message):
    await message.answer(text='Главное меню', reply_markup=keyboards.main_inline_kb())


@router.callback_query(F.data == 'get_horo')
async def get_horo(in_qr: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(MAINSTATES.horo)
    await in_qr.message.edit_text(text='Ваш гороскоп', reply_markup=keyboards.back_1())
    # await in_qr.message.answer(text='Главное меню', reply_markup=keyboards.main_inline_kb())


@router.callback_query(F.data == 'load_form')
async def load_form(in_qr: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(FORM.name)
    await in_qr.message.edit_text(text='Как я могу к вам обращаться?', reply_markup=keyboards.back_1())


@router.callback_query(F.data == 'back_1')
async def back2main(in_qr: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await in_qr.message.edit_text(text='Главное меню', reply_markup=keyboards.main_inline_kb())

from aiogram import F, Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters.state import StateFilter, StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup, InlineKeyboardBuilder
from datetime import datetime
from aiogram.enums.content_type import ContentType
import keyboards
import bot
from pprint import pprint


router = Router()
subscribe = State()


@router.callback_query(F.data == 'subscribe')
async def choose_sub(in_qr: types.CallbackQuery, state: FSMContext):
    await state.set_state(subscribe)
    await in_qr.message.edit_text(text='Подписка', reply_markup=keyboards.choose_sub().as_markup())


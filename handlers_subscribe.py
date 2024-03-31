from aiogram import F, Router, types
from aiogram.filters.state import State
from aiogram.fsm.context import FSMContext

import keyboards

router = Router()
subscribe = State()


@router.callback_query(F.data == 'subscribe')
async def choose_sub(in_qr: types.CallbackQuery, state: FSMContext):
    await state.set_state(subscribe)
    await in_qr.message.edit_text(
        text='Подписка',
        reply_markup=keyboards.choose_sub().as_markup()
    )

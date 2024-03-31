from aiogram import F, Router, types
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


# class FORM(StatesGroup):
#     name = State()
#     age = State()
#     gender = State()
#     cat = State()


# @router.message(StateFilter(default_state), Command('main'))
# async def sent_main_kb(message: types.Message):
#     await message.answer(text='main', reply_markup=keyboards.main_inline_kb())

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


# @router.message(StateFilter(FORM.name))
# async def take_name(message: types.Message, state: FSMContext):
#     # check symb
#     if message.text.isalpha() or len(message.text) > 20:
#         name = message.text
#         await state.update_data(name=name)
#         await message.answer(text=f'{name}, введите вашу дату рождения в формате ДД.ММ.ГГГГ', reply_markup=keyboards.back_1())
#         await state.set_state(FORM.age)
#     elif len(message.text) > 20:
#         await message.answer(text='Слишком длинное имя! Введите другое', reply_markup=keyboards.back_1())
#     else:
#         await message.answer(text='Некорректное имя! Введите другое', reply_markup=keyboards.back_1())
#
#
# @router.message(StateFilter(FORM.age))
# async def take_age(message: types.Message, state: FSMContext):
#     try:
#         if datetime.strptime(message.text, '%d.%m.%Y').date():
#             date_born = message.text
#             age = date_born.split('.')
#             if 1900 < int(age[-1]) < 2024:
#                 await state.update_data(date_born=date_born)
#                 await state.set_state(FORM.gender)
#                 await message.answer(text='Отлично! Теперь укажите ваш пол:', reply_markup=keyboards.choose_gender())
#             else:
#                 await message.answer(text='Некорректная дата! Введите другую', reply_markup=keyboards.back_1())
#     except ValueError:
#         await message.answer(text='Некорректная дата! Введите другую', reply_markup=keyboards.back_1())
#
#
# @router.callback_query(StateFilter(FORM.gender), F.data.in_({'man', 'woman'}))
# async def take_gender(in_qr: types.CallbackQuery, state: FSMContext):
#     if in_qr.data == 'man':
#         await state.update_data(gender='man')
#     elif in_qr.data == 'woman':
#         await state.update_data(gender='woman')
#     await state.set_state(FORM.cat)
#     await in_qr.message.edit_text(text='Выберите категории:', reply_markup=keyboards.choose_cat().as_markup())
#
#
# @router.message(StateFilter(FORM.gender))
# async def echo_gender(message: types.Message):
#     await message.answer(text='Укажите ваш пол:', reply_markup=keyboards.choose_gender())
#
#
# cat_kb = keyboards.choose_cat()
#
#
# @router.callback_query(F.data.in_({'cat 1 🚫', 'cat 2 🚫', 'cat 3 🚫', 'cat 1 ✅', 'cat 2 ✅', 'cat 3 ✅'}),
#                        StateFilter(FORM.cat))
# async def take_cat(in_qr: types.CallbackQuery, state: FSMContext):
#     global cat_kb
#     but_num = int(str(in_qr.data)[-3]) - 1
#     in_kb = cat_kb.export()
#     if in_qr.data[-1] == '🚫':
#         in_kb[but_num] = [InlineKeyboardButton(text=f'{in_qr.data[:-2]} ✅', callback_data=f'{in_qr.data[:-2]} ✅')]
#     elif in_qr.data[-1] == '✅':
#         in_kb[but_num] = [InlineKeyboardButton(text=f'{in_qr.data[:-2]} 🚫', callback_data=f'{in_qr.data[:-2]} 🚫')]
#     cat_kb = InlineKeyboardBuilder(markup=in_kb)
#     cat_dict = dict()
#     for but in cat_kb.export()[:-1]:
#         cat_dict[but[0].text[:-2]] = but[0].text[-1] == '✅'
#     await state.update_data(cat=cat_dict)
#     await in_qr.message.edit_text(text='Выберите категории:', reply_markup=cat_kb.as_markup())
#
#
# @router.message(StateFilter(FORM.cat))
# async def echo_cat(message: types.Message):
#     global cat_kb
#     await message.answer(text='Выберите категории:', reply_markup=cat_kb.as_markup())
#
#
# @router.callback_query(F.data == 'confrim', StateFilter(FORM.cat))
# async def confrim_form(in_qr: types.CallbackQuery, state: FSMContext):
#     # await state.clear()
#     user_data = await state.get_data()
#     print(user_data.keys())
#     print(user_data.values())
#     gender = 'Мужчина' if user_data['gender'] == 'man' else 'Женщина'
#     cat = user_data['cat']
#     s = ''
#     for c, v in cat.items():
#         if v:
#             s += f'{c} ✅\n'
#         else:
#             s += f'{c} 🚫\n'
#     form = f"Имя: {user_data['name']}\nДата рождения: {user_data['date_born']}\nПол: {gender}\nВыбранные категории:\n{s[:-1]}"
#
#     # load data base
#     await in_qr.message.edit_text(text=f'Ваша анкета\n{form}', reply_markup=keyboards.back_1())


@router.callback_query(F.data == 'back_1')
async def back2main(in_qr: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await in_qr.message.edit_text(text='Главное меню', reply_markup=keyboards.main_inline_kb())

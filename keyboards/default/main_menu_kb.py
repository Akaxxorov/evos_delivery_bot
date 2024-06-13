from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🍴 Menyu")
        ],
        [
            KeyboardButton(text="🛍 Mening buyurtmalarim")
        ],
        [
            KeyboardButton(text="✍️ Fikr bildirish"),
            KeyboardButton(text="⚙️ Sozlamalar")
        ]
    ]
)

tastiqlash = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='✅Tastiqlash'),
         KeyboardButton(text='❌bekor qilish')]
    ]
)
payments = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Naqd pul')],
        [KeyboardButton(text="Click")],
        [KeyboardButton(text="Payme")],
        [KeyboardButton(text="⬅️ Ortga")]
    ]
)
number = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='📞Mening raqamim',request_contact=True)],
        [KeyboardButton(text="⬅️ Ortga")]
    ]
)


menu2nd = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🗺 Mening manzillarim")
        ],
        [
            KeyboardButton(text="📍 Geolokatsiyani yuboring", request_location=True),
            KeyboardButton(text="⬅️ Ortga")
        ],
    ]
)
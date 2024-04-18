from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Я ученик", callback_data="student")
        ],
        [
            InlineKeyboardButton(text="Я учитель", callback_data="teacher")
        ]
    ]

)



table_student = InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text="1 класс", callback_data="1class")
        ],
        [
            InlineKeyboardButton(text="2 класс", callback_data="2class")
        ],
        [
            InlineKeyboardButton(text="3 класс", callback_data="3class")
        ],
        [
            InlineKeyboardButton(text="4 класс", callback_data="4class")
        ],
        [
            InlineKeyboardButton(text="5 класс", callback_data="5class")
        ],
        [
            InlineKeyboardButton(text="6 класс", callback_data="6class")
        ],
        [
            InlineKeyboardButton(text="7 класс ", callback_data="7class")
        ],
        [
            InlineKeyboardButton(text="8 класс ", callback_data="8class")
        ],
        [
            InlineKeyboardButton(text="9 класс", callback_data="9class")
        ],
        [
            InlineKeyboardButton(text="10 класс ", callback_data="10class")
        ],

        [
            InlineKeyboardButton(text="11 класс", callback_data="11class")
        ],

        [
            InlineKeyboardButton(text='◀️<<', callback_data="edit_orqa"),
            InlineKeyboardButton(text='>>▶️', callback_data="edit_oldin"),
        ],

    ]
)
Katalog2 = InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text="🧱 Qurilish va tamirlash", callback_data="Qurilish va tamirlash"),
        ],

        [
            InlineKeyboardButton(text="🚘 Avtotovarlar", callback_data="Avtotovarlar"),
        ],
        [
            InlineKeyboardButton(text="👶 Bolalar tovarlari", callback_data="Bolalar tovarlari")
        ],

        [
            InlineKeyboardButton(text="🤔 Xobbi va ijod", callback_data="Xobbi va ijod")
        ],
        [
            InlineKeyboardButton(text="⚽️ Sport va hordiq", callback_data="Sport va hordiq")
        ],

        [
            InlineKeyboardButton(text="🥕 Oziq-ovqat mahsulotlari", callback_data="Oziq-ovqat mahsulotlari")
        ],
        [
            InlineKeyboardButton(text="👨‍🔬 Maishiy kimyoviy moddalar", callback_data="Maishiy kimyoviy moddalar")
        ],

        [
            InlineKeyboardButton(text="📚 Kanselyariya tovarlari", callback_data="Kanselyariya tovarlari")
        ],
        [
            InlineKeyboardButton(text="🦓 Hayvonlar uchun tovarlar", callback_data="Hayvonlar uchun tovarlar")
        ],

        [
            InlineKeyboardButton(text="📖 Kitoblar", callback_data="Kitoblar")
        ],
        [
            InlineKeyboardButton(text="🏡 Dacha, bog va tomorqa", callback_data="Dacha, bog va tomorqa")
        ],
        [
            InlineKeyboardButton(text='◀️<<', callback_data="edit_orqa"),
            InlineKeyboardButton(text='>>▶️', callback_data="edit_oldin"),
        ]
    ],

)
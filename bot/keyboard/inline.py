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
teacher = InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text="", callback_data=""),
        ],

        [
            InlineKeyboardButton(text="", callback_data=""),
        ],
        [
            InlineKeyboardButton(text="", callback_data="")
        ],

        [
            InlineKeyboardButton(text="", callback_data="")
        ],
        [
            InlineKeyboardButton(text="", callback_data="")
        ],

        [
            InlineKeyboardButton(text="", callback_data="")
        ],
        [
            InlineKeyboardButton(text="", callback_data="")
        ],

        [
            InlineKeyboardButton(text="", callback_data="")
        ],
        [
            InlineKeyboardButton(text="🦓", callback_data="")
        ],

        [
            InlineKeyboardButton(text="", callback_data="")
        ],
        [
            InlineKeyboardButton(text="", callback_data="")
        ],
        [
            InlineKeyboardButton(text='◀️<<', callback_data="edit_orqa"),
            InlineKeyboardButton(text='>>▶️', callback_data="edit_oldin"),
        ]
    ],

)
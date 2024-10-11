from telebot.types import InputMediaPhoto, InputFile
from ..Markups import *
from ..States import *


with open('Modules/BookFinder/Data/IMG/Success.png', 'rb') as img_png:
    success_image = InputMediaPhoto(img_png.read())



inline_markups_list  = [
    numeric_markup, 
    yn_markup, 
    yn_markup, 
    genre_markup,

    numeric_markup, 
    what_do_u_want_markup, 
    numeric_markup, 
    pages_amount_markup,
    
    agreement_markup
]

states_list = [
    BookSearchState.set_hero_props,
    BookSearchState.stroy_end,
    BookSearchState.set_adaptation,
    BookSearchState.set_genre,

    BookSearchState.set_interests,
    BookSearchState.set_experience,
    BookSearchState.set_setting,
    BookSearchState.set_pages_amount,

    BookSearchState.accept_policy
]
questions_cards_list = []

source_dir = "Modules/BookFinder/Data/IMG"

for index in range(0,8):
    img_path = f"{source_dir}/BookFinderCard_0{index+1}.png" 
    with open(img_path, "rb") as png_img:
        str_img = png_img.read()
        questions_cards_list.append(
            {   
                "state":   states_list[index],
                "photo":   str_img,
                "e_photo": InputMediaPhoto(str_img),
                "reply_markup": inline_markups_list[index]
            }
        )
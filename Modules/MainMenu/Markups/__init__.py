from FletBot.Markups import MarkupBuilder
from ..Buttons import *

main_menu_markup = (
    MarkupBuilder()
        .inline()
        .build()
            .add(profile)
            .add(my_book)
)
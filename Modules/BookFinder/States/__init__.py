from FletBot import State, StatesGroup, StateFilter

class BookSearchState(StatesGroup):
    init=State()
    set_hero_props = State()
    stroy_end = State()
    set_adaptation = State()
    set_genre = State()
    set_active_story=State()
    set_experience=State()
    set_setting=State()
    set_pages_amount=State()
    set_interests=State()
    accept_policy=State()
async def set_book_search_user_data(user_data):
    user_data.update(
        { 
            "question_index":  0,
            "hero_props":      None,
            "stroy_end":       None,
            "has_adaptation":  None,
            "genre":           None,
            "interests":       None,
            "is_active_story": None,
            "experience":      None,
            "setting":         None,
            "pages_amount":    None,
    })
    return user_data   
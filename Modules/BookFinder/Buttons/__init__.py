from FletBot.Keyboards import ButtonBuilder


# Numeric buttons
# =========================================================================================#
numeric_dict = {
    "1":  ButtonBuilder().inline().set_text("1️⃣").set_callback_data("one_1").build(),
    "2":  ButtonBuilder().inline().set_text("2️⃣").set_callback_data("two_2").build(),
    "3":  ButtonBuilder().inline().set_text("3️⃣").set_callback_data("three_3").build(),
    "4":  ButtonBuilder().inline().set_text("4️⃣").set_callback_data("four_4").build(),
    "5":  ButtonBuilder().inline().set_text("5️⃣").set_callback_data("five_5").build(),
    "6":  ButtonBuilder().inline().set_text("6️⃣").set_callback_data("six_6").build(),
    "7":  ButtonBuilder().inline().set_text("7️⃣").set_callback_data("seven_7").build(),
    "8":  ButtonBuilder().inline().set_text("8️⃣").set_callback_data("eight_8").build(),
    "9":  ButtonBuilder().inline().set_text("9️⃣").set_callback_data("nine_9").build(),
    "10": ButtonBuilder().inline().set_text("🔟").set_callback_data("ten_10").build()
}
# =========================================================================================#

# Genre buttons
# =========================================================================================#
genre_dict = {
    "drama":       ButtonBuilder().inline().set_text("Драма").set_callback_data("drama_1").build(),
    "adventure":   ButtonBuilder().inline().set_text("Приключение").set_callback_data("adventure_2").build(),
    "detective":   ButtonBuilder().inline().set_text("Детектив").set_callback_data("detective_3").build(),    
    "fantastic":   ButtonBuilder().inline().set_text("Фантастика").set_callback_data("fantastic_4").build(),
    "triller":     ButtonBuilder().inline().set_text("Триллер").set_callback_data("triller_5").build(),
    "child":       ButtonBuilder().inline().set_text("Детское").set_callback_data("child_6").build(),
}
# =========================================================================================#

# What do u want
# =========================================================================================#
what_do_u_want_dict = {
    "study":  ButtonBuilder().inline().set_text("Обучение").set_callback_data("study_1").build(),
    "chill":  ButtonBuilder().inline().set_text("Расслабиться").set_callback_data("chill_5").build(),
    "pscyho_analize":  ButtonBuilder().inline().set_text("Психологический анализ").set_callback_data("psycho_analize_10").build()
}
# =========================================================================================#

# yes no buttons
# =========================================================================================#
yes_no_dict = {
    "yes": ButtonBuilder().inline().set_text("да").set_callback_data("yes").build(),
    "no":  ButtonBuilder().inline().set_text("нет").set_callback_data("no").build()
}
# =========================================================================================#

# pages amount
# =========================================================================================#
pages_amount = {
    "1-50":     ButtonBuilder().inline().set_text("1-50").set_callback_data("1").build(),
    "50-100":   ButtonBuilder().inline().set_text("50-100").set_callback_data("2").build(),
    "100-150":  ButtonBuilder().inline().set_text("100-150").set_callback_data("3").build(),
    "150-200":  ButtonBuilder().inline().set_text("150-200").set_callback_data("4").build(),
    "200-250":  ButtonBuilder().inline().set_text("200-250").set_callback_data("5").build(),
    "250-300":  ButtonBuilder().inline().set_text("250-300").set_callback_data("6").build(),
    "300-450":  ButtonBuilder().inline().set_text("300-450").set_callback_data("7").build(),
    "450-500+": ButtonBuilder().inline().set_text("450-500+").set_callback_data("8").build()
}
# =========================================================================================#


# agree/disagree buttons
agreement_dict = {
    "agree":    ButtonBuilder().inline().set_text("Согласиться").set_callback_data("agree").build(),
    "disagree": ButtonBuilder().inline().set_text("Отказаться").set_callback_data("disagree").build()
}
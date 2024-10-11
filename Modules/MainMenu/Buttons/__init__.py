from FletBot.Keyboards import ButtonBuilder

profile = (
    ButtonBuilder()
        .inline()
        .set_text("Профиль")
        .set_callback_data("profile")
    .build()
)

my_book = (
     ButtonBuilder()
        .inline()
        .set_text("Мои книги")
        .set_callback_data("leadbooks")
    .build()
)
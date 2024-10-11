from FletBot.Markups import MarkupBuilder
from ..Buttons import *

numeric_markup = (
    MarkupBuilder().inline().build()
        .row(numeric_dict["1"], numeric_dict["2"], numeric_dict["3"])
        .row(numeric_dict["4"], numeric_dict["5"], numeric_dict["6"])
        .row(numeric_dict["7"], numeric_dict["8"], numeric_dict["9"])
        .add(numeric_dict["10"])
)

genre_markup = (
    MarkupBuilder().inline().build()
        .add(genre_dict["drama"])
        .add(genre_dict["adventure"])
        .add(genre_dict["detective"])
        .add(genre_dict["fantastic"])
        .add(genre_dict["triller"])
        .add(genre_dict["child"])
)


what_do_u_want_markup = (
    MarkupBuilder().inline().build()
        .add(what_do_u_want_dict["study"])
        .add(what_do_u_want_dict["chill"])
        .add(what_do_u_want_dict["pscyho_analize"])
)


yn_markup = (
    MarkupBuilder().inline().build()
        .row(yes_no_dict['yes'], yes_no_dict['no'])
)

pages_amount_markup = (
    MarkupBuilder().inline().build()
        .add(pages_amount["1-50"])
        .add(pages_amount["50-100"])
        .add(pages_amount["100-150"])
        .add(pages_amount["150-200"])
        .add(pages_amount["200-250"])
        .add(pages_amount["250-300"])
        .add(pages_amount["300-450"])
        .add(pages_amount["450-500+"])
)

agreement_markup = (
    MarkupBuilder().inline().build()
        .add(agreement_dict["agree"])
        .add(agreement_dict["disagree"])
)
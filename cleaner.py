def clean_text(text):

    corrections={

        "|":"I",

        "ﬁ":"fi",

        "ﬂ":"fl",

        "0":"O"

    }

    for wrong,right in corrections.items():

        text=text.replace(wrong,right)

    return text
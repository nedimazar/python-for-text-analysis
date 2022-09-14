def clean_text_general(text, /, chars_to_remove={'\n', ',', '.', '"'}):
    for character in chars_to_remove:
        text = text.replace(character, "")
    return text
clean_text_general(" difj nr #$(%U$%I gkjbsf ),", chars_to_remove={"#", "$", "%", " "})

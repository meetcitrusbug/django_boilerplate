from google_trans_new import google_translator  


def language_translate(text, code='en'):
    try:
        translator = google_translator()  
        translate_text = translator.translate(text,lang_tgt=code)
        return translate_text
    except:
        return text
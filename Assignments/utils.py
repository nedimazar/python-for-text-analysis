import lxml.etree as et

def load_root(path):
    tree = et.parse(path)
    root = tree.getroot()
    return root

def get_id(talk):
    id = talk.find('head/talkid').text
    return id

def get_date(talk):
    date = talk.find('head/date').text
    return date

def get_title(talk):
    title = talk.find('head/title').text
    speaker = get_speaker(talk)
    return title.strip(speaker + ':')

def get_speaker(talk):
    speaker = talk.find('head/speaker').text
    return speaker

def get_wc(talk):
    wc = int(talk.find('head/wordnum').text)
    return wc

def date_to_int(year, month, day):
    return year * 100000 + month * 1000 + day

def extract_language(lang_id):
    rev = lang_id[::-1]
    # split only at first point:
    f_id, lang = rev.split('-', 1)
    return lang[::-1]
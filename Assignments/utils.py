import nltk
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
    return title

def get_speaker(talk):
    speaker = talk.find('head/speaker').text
    return speaker

def get_wc(talk):
    wc = int(talk.find('head/wordnum').text)
    return wc

def date_to_int(year, month, day):
    return year * 100000 + month * 1000 + day
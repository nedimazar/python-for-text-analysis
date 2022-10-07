import os
import json
from utils import load_root, get_id, get_title, extract_language

# STEP 1
def map_languages_to_path():
    workdir = '../Data/ted-talks/XML_releases/xml'
    files = os.listdir(workdir)
    lang_to_path = dict()
    for file in files:
        if not file.endswith('.xml'):
            continue
        # Getting rid of ted_ and .xml
        lang_id = file[4:-4]
        language = extract_language(lang_id=lang_id)
        
        langpath = os.path.abspath(workdir + '/' + file)

        lang_to_path[language] = langpath
    return lang_to_path

# STEP 2
def find_coverage(lang_to_path):
    coverage = dict()
    for lang in lang_to_path:
        root = load_root(lang_to_path[lang])
        talks = root.findall('file')
        coverage[lang] = len (talks)
    return coverage

# STEP 3
def get_id_title_dict():
    path = '../Data/ted-talks/XML_releases/xml/ted_en-20160408.xml'
    root = load_root(path)
    talks = root.findall('file')

    id_title_dict = dict()
    for talk in talks:
        id = get_id(talk)
        title = get_title(talk)
        id_title_dict[id] = title
    return id_title_dict

# STEP 4
def map_talks_to_languages(lang_to_path):
    talks_to_lang = dict()
    for lang in lang_to_path:
        path =  lang_to_path[lang]
        root = load_root(path)
        talks = root.findall('file')
        for talk in talks:
            id = get_id(talk)
            if id not in talks_to_lang:
                talks_to_lang[id] = []
            talks_to_lang[id].append(lang)
    return talks_to_lang

# STEP 5
def map_nlang_to_talks(talks_to_lang):
    nlang_to_talks = dict()
    for talk, langs in talks_to_lang.items():
        nlangs = len(langs)
        if nlangs not in nlang_to_talks:
            nlang_to_talks[nlangs] = []
        nlang_to_talks[nlangs].append(talk)
    return nlang_to_talks

# STEP 6
def find_top_coverage(lang_to_fp, mostleast='most'):
    id_title_dict = get_id_title_dict()
    talks_to_languages = map_talks_to_languages(lang_to_path=lang_to_fp)
    nlangs_to_talks = map_nlang_to_talks(talks_to_languages)
    
    if mostleast == 'most':
        func = max
    else:
        func = min
    
    talks = nlangs_to_talks[func(nlangs_to_talks.keys())]

    talk_to_langs = dict()
    for talk in talks:
        talk_to_langs[id_title_dict[talk] + f" (id: {talk})"] = talks_to_languages[talk]
    return (talk_to_langs)

def find_translations(lang_to_path, mostleast='most'):
    if mostleast == 'most':
        func = max
    else:
        func = min

    n = None
    language = None
    
    for lang in lang_to_path:
        path =  lang_to_path[lang]
        root = load_root(path)
        talks = root.findall('file')

        if (n is None and language is None)\
            or (func(len(talks), n) != n):
            language = lang
            n = len(talks)
    return language

def main():
    lang_to_path = map_languages_to_path()

    # most_coverage = find_top_coverage(lang_to_path, mostleast='most')
    # least_coverage = find_top_coverage(lang_to_path, mostleast='least')

    # print('Least translated talks:')
    # print(least_coverage)
    # print()
    # print('Most translated talks:')
    # print(most_coverage)

    most_translations = find_translations(lang_to_path=lang_to_path, mostleast='most')
    least_translations = find_translations(lang_to_path=lang_to_path, mostleast='least')

    print('\nLaguage with most traslations:', most_translations)
    print('\nLaguage with least traslations:', least_translations)


if __name__ == '__main__':
    main()
import os
import nltk
import operator
from pathlib import Path

def get_paths(input_folder):
    '''Gets file paths for all .txt files in a specified folder.
    
    Parameters:
        input_folder (str): A folder path.
        
    Returns:
        items (list[str]): A list of file paths for all .txt files in input_folder.'''
    items = os.listdir(input_folder)
    items = [os.path.abspath(Path(input_folder) / Path(item)) for item in items if item.endswith('.txt')]
    return items

def get_basic_stats(txt_path):
    '''Gets basic statistics for a specified text file.
    
    Parameters:
        txt_path (str): A text file path.
        
    Returns:
        stats (dict): A dictionary of basic statistics for txt_path, including the number of sentences, tokens, unique vocabulary, and chapters or acts (depending on the text).'''
    with open(txt_path, 'r') as infile:
        text = infile.read()

    sentences = nltk.sent_tokenize(text)
    tokens = nltk.word_tokenize(text)

    num_chapters = None

    if "HuckFinn.txt" in txt_path:
        num_chapters = tokens.count('CHAPTER')
    elif "AnnaKarenina.txt" in txt_path:
        num_chapters = tokens.count('Chapter')
    elif "Macbeth.txt" in txt_path:
        num_chapters = tokens.count('ACT')

    top_30 = []

    token2freq = {tok: tokens.count(tok) for tok in set(tokens)}
    for token, _ in sorted(token2freq.items(),
    key=operator.itemgetter(1),
    reverse=True):
        if len(top_30) < 30:
            top_30.append(token)

    return {"num_sents" : len(sentences),
    "num_tokens" : len(tokens),
    "vocab_size" : len(set(tokens)),
    "num_chapters_or_acts" : num_chapters,
    "top_30_tokens": top_30}

    




if __name__ == "__main__":
    print(get_basic_stats(txt_path="../Data/books/AnnaKarenina.txt"))
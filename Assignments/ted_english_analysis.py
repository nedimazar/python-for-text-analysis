import lxml.etree as et
from utils import load_root, get_id, get_date, get_title, get_speaker, get_wc, date_to_int

def find_length(talks, /, length = 'longest'):
    if length == 'longest':
        func = max
    else:
        func = min
    
    curr_talk = None
    curr_len = None

    total_wc = 0
    total_talks = 0

    for talk in talks:
        wc = get_wc(talk)
        if (curr_talk is None and curr_len is None)\
            or (func(wc, curr_len) != curr_len):
            curr_talk = talk
            curr_len = wc
        total_wc += wc
        total_talks  += 1
    if total_talks == 0:
        total_talks = 1
    return (get_title(curr_talk), get_id(curr_talk)), curr_len, total_wc / total_talks 

def find_date(talks, /, time = 'latest'):
    if time == 'latest':
        func = max
    else:
        func = min
    
    curr_talk = None
    curr_time = None

    for talk in talks:
        year, month, day = [int(x) for x in get_date(talk).split('/')]
        value = date_to_int(year, month, day )
        if ((curr_talk is None) and (curr_time is None ))\
            or (func(value, curr_time) != curr_time):
            curr_talk = talk
            curr_time = value

    return (get_title(curr_talk), get_id(curr_talk)), get_date(curr_talk)

def find_speaker(talks):
    speaker_dict = dict()

    for talk in talks:
        speaker = get_speaker(talk)
        title = get_title(talk)
        id  = get_id(talk)

        if speaker not in speaker_dict:
            speaker_dict[speaker] = []
        speaker_dict[speaker].append((title, id))
    return {key: value for key, value in speaker_dict.items() if len(value) > 1}


def main():
    path = "../Data/ted-talks/XML_releases/xml/ted_en-20160408.xml"
    root = load_root(path)
    talks = root.findall('file')

    n_talks = len(talks)

    print(f"In total, there are {n_talks} Eglish Ted talks in the dataset.")
    
    print('\nTalk length:')
    ((longest_title, longest_id), longest_len, average1) =  find_length(talks)
    print(f"Longest Talk: {longest_title} (id: {longest_id})")
    ((shortest_title, shortest_id), shortest_len, average2) =  find_length(talks, length='shortest')
    print(f"Shortest Talk: {shortest_title} (id: {shortest_id})")
    print(f"Mwan word count: {average1}")

    print('\nTalk date:')
    ((oldest_title, oldest_id), date1) =  find_date(talks, time='oldest')
    print(f"Oldest Talk: {oldest_title} (id: {oldest_id}) (date: {date1})")
    ((latest_title, latest_id), date2) =  find_date(talks)
    print(f"Latest Talk: {latest_title} (id: {latest_id}) (date: {date2})")

    speaker_dict = find_speaker(talks)
    print(speaker_dict)
        
    
    
if __name__ == '__main__':
    main()

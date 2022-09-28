import os
from utils import get_paths, get_basic_stats

paths = get_paths(input_folder="../Data/books")

book2stats = dict()

for path in paths:
    basename = os.path.basename(path)
    book = basename.strip('.txt')

    stats = get_basic_stats(path)
    print(book, stats)

    book2stats[book] = stats

print()
print(book2stats)
print()

stats2book_with_highest_value = {
    'num_sents': None,
    'num_tokens': None,
    'vocab_size': None,
    'num_chapters_or_acts': None
}

current_max_values = {key: 0 for key in stats2book_with_highest_value}

for book in book2stats:
    for key in book2stats[book]:
        if key == 'top_30_tokens':
            continue
        if book2stats[book][key] and book2stats[book][key] >= current_max_values[key]:
            current_max_values[key] = book2stats[book][key]
            stats2book_with_highest_value[key] = book

print(current_max_values)
print(stats2book_with_highest_value)

# 4b
for book in book2stats:
    top_30 = book2stats[book]['top_30_tokens']
    with open(f'top_30_{book}.txt', 'w') as outfile:
        for x in top_30:
            outfile.write(f"{x}\n")
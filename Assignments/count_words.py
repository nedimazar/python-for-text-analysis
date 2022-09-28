from utils_3a import preprocess

def count(string, remove=["'", "(", ")"]):
    '''Counts the number of times each word occurs in the input string.
    
    Parameters:
        string (str): A string.
        remove (list[str], optional): A list of characters to remove from the string before counting. Defaults to ["'", "(", ")"].
        
    Returns:
        word_counts (dict[str, int]): A dictionary mapping words to the number of times they occur in the input string'''
    string = preprocess(string, set(remove))
    
    # I am assuming that the count should be case insensitive, that is why I am converting everything to lowercase
    string = string.lower()
    words = string.split(" ")
    
    word_counts = {word : words.count(word) for word in set(words)}
    
    return word_counts


b = "one. two, two. three, three, three. four, four, four, four!"
results_b = count(b, remove=[',', '.', '!'])
print("String:", b)
print("Counts dictionary:", results_b)

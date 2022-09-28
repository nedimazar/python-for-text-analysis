def preprocess(string, remove):
    '''Preprocesses a string by removing specified characters.
    
    Parameters:
        string (str): A string.
        remove (set[character]): A set of characters to be removed from string.
        
    Returns:
        string (str): The string with specified characters removed.'''
    for character in remove:
        string = string.replace(character, "")
    return string
markerChars = []


def marker_finder(num_of_chars):
    char_in_data = [char for char in open("Dataset.txt").read()]
    for index, mainChar in enumerate(char_in_data):
        chunk = char_in_data[index:index + num_of_chars]
        if len(set(chunk)) == len(chunk):
            return index + num_of_chars

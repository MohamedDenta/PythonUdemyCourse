import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(
            "Did you mean {} instead press Y if yes or N if no .".format(get_close_matches(word, data.keys())[0]))
        if yn == "Y":
            return get_close_matches(word, data.keys())[0]
        elif yn == "N":
            return "The word doesn't exist"
        else:
            return "We didn't understand your entry."
    else:
        return "The Word doesn't exist!"


word = input("Enter word: ")
output = translate(word=word)
if type(output) is list:
    for item in output:
        print(item)
else:
    print(output)

# Write a short Python function that takes a string s,representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return "Lets try Mike"

def remove_punctuations(s):
    if not isinstance(s, str):
        raise TypeError('parameter must be a string')
    new_sentence = []
    for i in s:
        if i != ',' and i != '.' and i != "'":
            new_sentence.append(i)
    edited_sentence = ''.join(new_sentence)

    return edited_sentence


print(remove_punctuations("Let's try, Mike."))


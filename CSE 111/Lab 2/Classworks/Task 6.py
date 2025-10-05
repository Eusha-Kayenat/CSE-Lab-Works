def correct_capitalization(text):
    text = list(text)
    if text:
        text[0] = text[0].upper()
    for i in range(1, len(text)):
        if text[i - 1] in ['.', '!', '?']:
            text[i] = text[i].upper()
        elif text[i] == 'i' and (i == 0 or text[i-1] != "'"):
            text[i] = 'I'
    return ''.join(text)
input_string = input("Enter the paragraph: ")
print(correct_capitalization(input_string))

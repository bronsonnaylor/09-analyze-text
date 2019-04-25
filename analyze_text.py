def analyze_text(text):
    return "The text contains " + str(letter_count(text)) + " alphabetic characters, of which " + str(e_count(text)) + " (" + str(percentifier(letter_count(text), e_count(text))) + ") are 'e'."
    
def letter_count(text):
    letter_counter = 0
    for char in text:
        if char.isalpha():
            letter_counter += 1
    return letter_counter
            
def e_count(text):
    e_counter = 0
    for char in text:
        if char == "e" or char == "E":
            e_counter += 1
    return e_counter
            
def percentifier(letter, e):
    percent = e / letter
    #return f'{percent:.2%}'
    return '{:.2%}'.format(percent)

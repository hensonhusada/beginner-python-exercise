import re

THEMES_VARIATION = 1

HALLOWEEN = """\nI can't believe it's already {holiday}!\nI can't wait to put on my {noun1} and visit every {place} in my neighborhood.\nThis year, I am going to dress up as {person} with {adjective1} {body_part}.\nBefore I {verb}, I make sure to grab my {adjective2} {noun2} to hold all of my {food}.\nFinally, all of my {noun3} are ready to go!\n"""

theme_key = {'1': HALLOWEEN}

def get_texts_inputs(text):
    text_inputs = re.findall(r"{(.+?)}", text)
    return text_inputs

while True:
    print('Pick a Theme')
    print("""[1] Halloween """)
    choice = input("Pick: ")
    texts = []
    text_inputs = get_texts_inputs(theme_key[choice])
    i = 0
    for x in text_inputs:
        texts.append(input(str(x)))
        exec("%s='%s'" % (x, texts[i]))
        i+=1

    print(theme_key[choice].format(
        holiday=holiday,
        noun1=noun1,
        place=place,
        person=person,
        adjective1=adjective1,
        body_part=body_part,
        verb=verb,
        adjective2=adjective2,
        noun2=noun2,
        food=food,
        noun3=noun3
        ))
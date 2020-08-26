import re

file = open('testing.txt', 'r')
lines = file.read()
file.close()

def read_email(text):
    reg = r'([a-zA-z-\.]+)@[\w-]+\.+[\w-]{2,4}'
    result = re.findall(reg, text)
    return result

result = read_email(lines)
print(result)
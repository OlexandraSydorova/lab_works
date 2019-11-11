import re
re_float = re.compile("^[-+]{0,1}\d+\.{0,1}\d+$")
re_int = re.compile("^\d+$")
re_symbol = re.compile("^.{1}$")
def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text
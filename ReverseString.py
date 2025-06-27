def ReverseString(text):
    return text[::-1]

def ReverseString2(text):
    text = reversed(text)
    return ''.join(text)

def ReverseString3(text):
    for i in range(len(text)-1,-1,-1):
       print(text[i], end="")
    return ''


print(ReverseString3("harsh"))
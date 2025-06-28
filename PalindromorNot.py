def PalindromorNot(text):
    return text[::-1] == text

text = input("Enter a string:  ")
if PalindromorNot(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

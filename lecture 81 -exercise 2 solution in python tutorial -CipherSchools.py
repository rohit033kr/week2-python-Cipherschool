def palindrome(text):
    if text==text[::-1]:
        return True
    else:
        return False
text=input("enter a string :")
result=palindrome(text)
print(result)

def palindrome(string):
    string1=string[::-1]
    if string1==string:
        return(True)
    else:
        return(False)
string=input()
print(palindrome(string))
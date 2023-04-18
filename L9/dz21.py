def is_palindrome(text):
    filter_text = []
    for c in text:
        if c.isalnum():
            filter_text.append(c)
    text = ''.join(filter_text).lower()
    filter = text == text[::-1]
    return filter


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
print("ОК")
def popular_words(text, words):
    text = text.lower().split()
    result = {}
    for w in words:
        result[w] = text.count(w)
    return result


assert popular_words('''When I was One I had just begun When
I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

# text ='''When I was One I had just begun When
# I was Two I was nearly new '''
# words = ['i', 'was', 'three', 'near']
# print(popular_words(text, words))

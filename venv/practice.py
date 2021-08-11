def index_filter(indexes, string):
    letters = []
    words = string.split(" ")
    for word in words:
        for char in word:
            letters.append(char)
    result = ""
    for index in indexes:
        result += letters[index]
    return result.lower()

r = index_filter([2, 3, 8, 11], "Autumn in New York")
print(r)
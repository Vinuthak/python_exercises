def find_duplicates(text):
    words = text.lower().split()
    seen = set()
    duplicates = set()

    for word in words:
        if word in seen:
            duplicates.add(word)
        else:
            seen.add(word)
    unique = seen - duplicates

    print(f"unique words are {unique}")
    print(f"duplicate words are {duplicates}")
paragraph = "Python is fun and learning Python is easy and fun"
find_duplicates(paragraph)

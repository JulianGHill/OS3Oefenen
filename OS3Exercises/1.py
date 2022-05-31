def word_count():
    file = open("test.txt", "r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if len(word) > 4:
            count += 1
    print(count)
    file.close()

word_count()

with open('my_file.txt', mode='r+') as file:
    file.seek(0)
    text = list(file.read())
    index = 0
    for letter in text:
        index += 1
        if letter == 'a':
            text.insert(index, ' / ')
    string = str()
    for letter in text:
        string = string + letter
    file.seek(0)
    file.write(string)
    file.seek(0)
    print(file.readlines())

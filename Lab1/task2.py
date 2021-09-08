def readFileAndDuplicate(fileName):
    file = open(fileName, 'r+')
    file_contents = file.read()
    file.write('\n' + file_contents)
    print("File content:")
    print(file_contents)

    file.close()

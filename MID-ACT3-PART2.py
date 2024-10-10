from ArrayStack import ArrayStack as Stack
filename = 'file.txt'


def reverse_file(filename):

    S = Stack()
    original = open(filename)

    for line in original:
        S.push(line.rstrip("\n"))

    original.close()

    output = open(filename, 'w')

    while not S.is_empty():
        output.write(S.pop() + "\n")
    print("The file has been reversed!")

    output.close()

reverse_file('file.txt')
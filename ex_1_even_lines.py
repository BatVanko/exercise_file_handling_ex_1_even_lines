with open("./input_text.txt", 'w+') as file:
    file.write('''-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
''')
punctuation_symbols = ["-", ",", ".", "!", "?"]
with open("input_text.txt", 'r') as file:
    for index,line in enumerate(file):
        if index % 2 == 0:
            for symbol in line:
                if symbol in punctuation_symbols:
                    line = line.replace(symbol,'@')
            reversed_line = line.split()[::-1]
            print(*reversed_line)



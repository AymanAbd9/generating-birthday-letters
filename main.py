with open('Input/Names/invited_names.txt') as names:
    for name in names:
        name = name.strip()
        with open('Output/ReadyToSend/' + name + '.txt', "w+") as new_letter:
            with open('Input/Letters/starting_letter.txt') as letter:
                for line in letter:
                    new_letter.write(line.replace("[name]", name))

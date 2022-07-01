PLACEHOLDER = "[name]"

with open('Input/Names/invited_names.txt') as names_file:
    for name in names_file:
        stripped_name = name.strip()
        with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', "w+") as new_letter:
            with open('Input/Letters/starting_letter.txt') as template_letter:
                for line in template_letter:
                    new_letter.write(line.replace(PLACEHOLDER, stripped_name))

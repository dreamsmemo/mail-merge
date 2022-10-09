# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
with open("./input/Names/invited_names.txt") as f:
    name_list_str = f.read()
    # split string s by newline character
    name_list = name_list_str.split("\n")
    # you can also use readlines: names = names_file.readlines()
    print(name_list)

# Replace the [name] placeholder with the actual name.

for i in name_list:
    with open("./input/Letters/starting_letter.txt") as s:
        contents = s.read()
    letter_with_names = contents.replace("[name]", i)
    print(letter_with_names)

# Save the letters in the folder "ReadyToSend".
    with open(f"./output/ReadyToSend/letter_for_{i}.txt", mode="w") as output:
        output.write(letter_with_names)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

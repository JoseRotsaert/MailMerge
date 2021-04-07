#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
##Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode = "r") as input_names:
    names_list =input_names.readlines()   #readlines creates a list
    # check
    # print(names_list)

with open("./Input/Letters/starting_letter.txt", mode = "r") as input_letter:
    template_letter =input_letter.read()
    # check
    # print(template_letter)
    for name in names_list:
        stripped_name = name.strip("\n")
        new_letter = template_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/starting_letter_{stripped_name}.txt", mode="w") as letter_final:
            letter_final.write(new_letter)




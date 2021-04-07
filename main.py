#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#
with open("./Input/Names/invited_names.txt", mode = "r") as input_names:
    names_list =input_names.readlines()   #readlines creates a list
    # check
    # print(names_list)

with open("./Input/Letters/starting_letter.txt", mode = "r") as input_letter:
    template_letter =input_letter.read()
    # check
    # print(template_letter)

for name in names_list:
    name = name.strip("\n")
    template_letter_name = template_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/starting_letter_{name}.txt", mode="w") as letter_final:
        letter_final.write(template_letter_name)




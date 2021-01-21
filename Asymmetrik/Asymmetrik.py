import regex as re 
import spacy
import sys

#Setting up a list to catch the names we parse into it from the txt file
name_list = []

#function to determine which test file to open based on user input
def test_case_fctn():
    test_case = input("Please type what number test you would like to run(1-5)")
    global readable #need this variable in the open_file function
    doc_num = ''
    if int(test_case) > 5:
        print("That is not a valid test number, please try again")
        sys.exit()
    elif int(test_case) == 1:
        doc_num = 'test_1.txt'
    elif int(test_case) == 2:
        doc_num = 'test_2.txt'
    elif int(test_case) == 3:
        doc_num = 'test_3.txt'
    elif int(test_case) == 4:
        doc_num = 'test_4.txt'
    elif int(test_case) == 5:
        doc_num = 'test_5.txt'

    #opening the selected document
    test_doc = open(doc_num)
    readable = test_doc.read()



#function to open the correct file and load the spacy library for name recognition
def open_file():
    global text_to_scan
    nlp = spacy.load("en_core_web_sm")
    text_to_scan = nlp(readable)
   

#function to look for a human name in the text document
def look_for_name():
    for word in text_to_scan:
        if word.ent_type_ == 'PERSON':
            name_list.append(word)
        else:
            pass

#function to look for a phone number specifically, excluding fax numbers, including country code, working with various ways to write a phone number
def look_for_phone_number():
    global Final_result
    original_character1 = "("
    original_character2 = ")"
    r = re.compile("(?<=Tel:)\s*[+\d\s\(]{1,4}\s*\d{3}[-\.\s\)]??\d{3}[-\.\s]??\d{4}|(?<=Tel:)\s[+\d\s\(]{1,4}\d{3}\)\s*\d{3}[-\.\s]??\d{4}|(?<!Fax:)[+\d\s\(]\s*\d{3}[-\.\s\)]??\d{3}[-\.\s]??\d{4}|")
    results = r.findall(readable)
    res = ' '.join([str(item) for item in results]) #pulls the result from a list to a string for better display
    #next several lines filter out the special characters so that the display is in the format of "Phone: 1234567890"
    result1 = res.replace('-', '')
    result2 = result1.replace(original_character1, ' ')
    result3 = result2.replace(original_character2,'')
    result4 = result3.replace(' ', '')
    result5 = result4.replace('+', '')
    Final_result = result5.replace(".", '')


#function to look for email, checks for all characters attached to the @ symbol
def look_for_email():
    global res1
    r1 = re.compile ('\S+@\S+')
    results1 = r1.findall(readable)
    res1 = ' '.join([str(item) for item in results1]) #pulls the result from a list to a string for better display



#function to organize and run functions in proper order
def __main__():
    test_case_fctn() #runs the function to determine the test number first
    open_file() #opens the correct file
    look_for_name() #checks for the name
    look_for_phone_number() #checks for the phone number
    look_for_email() #checks for the email address

    print("Name:", name_list[0], name_list[1]) #displays name
    print("Phone:" , Final_result) #displays phone number
    print("Email:" , res1) #displays email address

if __name__ == "__main__": #runs main function
    __main__()  
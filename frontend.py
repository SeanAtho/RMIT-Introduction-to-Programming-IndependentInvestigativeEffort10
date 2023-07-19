import sys
import backend

class PasswordManagerUI:
    
    #In the below code block the method's parameter takes a string supplied when a call to the
    #method is made, if a user happens to enter an empty string or value they are prompted
    #repeatedly after each invalid input to provide a valid input in response to the prompt.
    #Alternative names could be “str_input” or “str_entered”. However, these names don’t indicate
    #as effectively what the purpose of the method is.
    def get_str(prompt):
        sys.stdout.write(prompt)
        
        #Alternatively it the variable could be named “taken_str”, “entered_string” however its current
        #naming scheme avoids complications and uses appropriate terminology. 
        inputted_str=sys.stdin.readline().strip()
        
        #A proposed alternative to the current statement where it's equal to an empty string could be
        #instead to have it equal simply “None”, however the method by design will only be dealing with strings. 
        while(inputted_str==""):
            sys.stdout.write("Error! Invalid Input, Re-Enter: \n")
            inputted_str=sys.stdin.readline().strip()
        return inputted_str
    
    def __init__(self):

        self.__backend=backend.PasswordManager("passwords.csv")
        sys.stdout.write(str(self.__backend.get_password_count())+ " passwords loaded...\n\n")
        sys.stdout.write("Welcome to Password Manager Application\n")

        #The below code block contains the main menu and is displayed each time a user launches
        #the program or is prompted to enter a choice. Its current implementation of outputting the
        #menu calls to the “get_str” method effectively takes care of both the output and the input of
        #the users choice in response to the menu selection prompt, as such this prevents unneeded
        #code repetition.
        #
        #The current name given is menu however an alternative would be “selection”.
        #However current name “menu” is preferred as in this instance menu gives a better indication of
        #its purpose and use in the program.
        menu=""
        menu+="============================\n"
        menu+="Password Manager Application\n"
        menu+="============================\n"
        menu+="[A]dd Login\n"
        menu+="[E]dit Login\n"
        menu+="[R]emove Stored Login\n"
        menu+="[D]isplay Stored Logins\n"
        menu+="[S]ave\n"
        menu+="E[x]it\n"
        menu+="Menu Choice: "

        menu_choice=PasswordManagerUI.get_str(menu).lower()
        
        sys.stdout.write("\n")
        
        #The Below code block is mainly contained within a while loop which is used to bring a user back
        #to them after each task is completed. Within are is are if-elif-else statements which as
        #previously mentioned are required to be indented underneath the while for the program to
        #repeat after a selection is made. 
        while(menu_choice!="x"):
            
            #Following if statement\s are used to determine which of the menu options was made and then
            #to carry out the appropriate code. An else has been used to check for invalid inputs in the
            #if-statement. 
            if(menu_choice=="a"):
                sys.stdout.write("Add Login to Password Manager...\n")
                
                #Variable takes the input from the user through the get_str method.
                #An alternative name would be “account” or “login” however these are easily confused with
                #other items are they are too vague and can easily be misinterpreted. 
                site = PasswordManagerUI.get_str("Name of Website or Application: ")
                
                #Two below variables takes the input from the user through the get_str method.
                #These could alternatively be named site_username and site_password, however, the increased
                #characters don’t stand to add much-needed clarification 
                username=PasswordManagerUI.get_str("Username for " +site+ ": ")
                password=PasswordManagerUI.get_str("Password for " +username+ ": ")
                self.__backend.add_password(site,username,password)

            elif(menu_choice=="e"):
                sys.stdout.write("Edit Login in Password Manager...\n")
                #Below variables have been justified previously on lines 66-74.
                site=PasswordManagerUI.get_str("Name of Website or Application: ")
                username=PasswordManagerUI.get_str("Username for " +site+ ": ")
                password=PasswordManagerUI.get_str("Password for " +username+ ": ")
                new_password=PasswordManagerUI.get_str("Enter the new password for" +username+ ": ")
                if (self.__backend.edit_password(site,username,password,new_password)):
                    sys.stdout.write("Password was Succesfully changed.\n")
                else:
                    sys.stdout.write("Password could not be changed. Please Re-enter details\n")
                
            elif(menu_choice=="r"):
                
                sys.stdout.write("Remove Saved Login Details from Password Manager...\n")
                #Below variables have been justified previously on lines 67-75.
                site=PasswordManagerUI.get_str("Name of Website or Application: ")
                username=PasswordManagerUI.get_str("Username for " +site+ ": ")
                password=PasswordManagerUI.get_str("Password for " +username+ ": ")
                self.__backend.remove_password(site,username,password)
                
            elif(menu_choice=="d"):
                sys.stdout.write("Display all Logins Stored in Password Manager...\n")
                sys.stdout.write(self.__backend.__str__())

            elif(menu_choice=="s"):
                sys.stdout.write("Saving to passwords.csv...\n")
                self.__backend.save_to_file()
                
            else:
                sys.stdout.write("Invalid Menu menu_choice! Select from the following options...\n")
                
            #The below line is unindented from if - statements in an effort to avoid code duplication inside each statement. 
            menu_choice=PasswordManagerUI.get_str(menu).lower()

        sys.stdout.write("Application Proccess Succesfully Completed\n")
                


pm=PasswordManagerUI()

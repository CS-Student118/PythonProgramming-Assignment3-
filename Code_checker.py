'''
Code_checker.py
This program uses the A3 Codes.txt file and determines if a code is valid or not. The criteria for a valid code is that it must have at least 10 characters, the positions
4 - 7 must be digits(these represent the country code) and the character in the 10th position must be a capital letter (this represents the security level). It also double
checks within the valid codes to see if it is an invalid restricted code. An invalid restricted code is a code that has a security level of 'R' and a country code of 2000 
or higher. It then adds the code to the valid codes string, the invalid codes string or the invalid restricted codes string accordingly.
'''

def main():
    
    """This is the main method which will execute the test_codes() method below."""
    test_codes() 
    



def test_codes():
    
    """ This will open the A3 Codes.txt file and check each code. It will add it into the valid_codes string,
    the invalid_codes string or the invalid_restricted_codes string accordingly"""

    valid_codes = ''    #String to hold the valid codes.

    invalid_codes = ''  #String to hold the invalid codes.

    invalid_restricted_codes = ''   #String to hold the invalid restricted codes.

    with open('A3 Codes.txt','r') as code_file: #Opens and allows us to read the A3 Codes file.
    
        for line in code_file:  #Loops through each line in the file
        
            if len(line)>=10 and line[3:7].isdigit() and line[9].isupper(): #Checks if the line meets the criteria for a valid code.
            
                if line[9] == 'R' and int(line[3:7]) >= 2000:   #If the line is valid, it further checks if it is an invalid restricted code or not.
                
                    invalid_restricted_codes = invalid_restricted_codes + line  #If it is an invalid restricted code, then it adds it to the string accordingly.
                
                else:   #Otherwise it is valid, it adds it to the valid_codes accordingly.
                
                            valid_codes = valid_codes + line
                
            else:   #If it does not meet the clauses above then it is invalid. This adds it to that string.
            
                invalid_codes = invalid_codes + line
            

    print('Valid Codes: ')  #Prints the heading for valid codes and prints the codes out.

    print(valid_codes)

    print('Invalid Codes: ')    #Prints the heading for invalid codes and prints the invalid codes out.

    print(invalid_codes) 

    print('Invalid Restricted Codes: ') #Print the heading for invalid restricted codes and prints the invalid restricted codes out.

    print(invalid_restricted_codes)           

            
            
main()  #This will call and execute the main method.

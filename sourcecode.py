from itertools import permutations

import argparse
import random 
import string

def passwordgen(pwLength, noOflettersAndNumbers):

    '''
    This is a function that generates a random password based on user inputs

    function parameters:
    :param pwLength: This is the length of the password you want
    :type pwLength: int
    :param lettersAndNumbers: This is the number of letters and digits you want in your password. The remaining charcters will be special characters
    :type lettersAndNumbers: int

    :return: The function returns a random password as per your specifications 
    :rtype: str
    '''

    try:
        password_length=int(pwLength)
        nooflettsandnums=int(noOflettersAndNumbers)
    except password_length < 6:
        print("too short! 6 characters minimum")
    except nooflettsandnums > password_length:
        print("number of letters and digits cannot be more than password length")

    pwdstring=string.ascii_letters+string.digits
    password="".join(random.SystemRandom().choice(pwdstring) for i in range(nooflettsandnums))
    
    pwdstring=string.punctuation
    specialchars=password_length-nooflettsandnums
    password+="".join(random.SystemRandom().choice(pwdstring) for j in range(specialchars))

    #now to mix password characters as you do not want patterns
    passwordList = list(permutations(password)) #this is a list
    passwordChoice = random.randrange(0, len(passwordList))
    
    password = "".join(passwordList[int(passwordChoice)])
    return password

def main():

    '''
    To call the passwordgen() function, used parsed arguments (argparse)
    For example, if a password of length 9 and number of letters and digits in it should be 6,
    run "python sourcecode.py --pwlength 9 --lettersnumbers 6" from your Linux shell
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("--pwlength", dest = "pwlength")
    parser.add_argument("--lettersnumbers", dest = "lettersnumbers")
    args = parser.parse_args()
    password = passwordgen(args.pwlength, args.lettersnumbers)
    print(password)

if __name__ == '__main__':
    main()

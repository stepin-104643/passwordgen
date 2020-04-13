import random 

import string

def passwordgen():
    
    password_length=int(input("enter pwd length"))
    
    if(password_length<6):
        print("too short! 6 characters minimum")
        exit()
    
    
    nooflettsandnums=int(input("enter no. of letters and nos"))
    
    pwdstring=string.ascii_letters+string.digits
    
    password="".join(random.SystemRandom().choice(pwdstring) for i in range(nooflettsandnums))
    
    pwdstring1=string.punctuation
    
    specialchars=password_length-nooflettsandnums
    
    password+="".join(random.SystemRandom().choice(pwdstring1) for j in range(specialchars))
    
    return password

print(passwordgen())

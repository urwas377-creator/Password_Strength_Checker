def password_strength_Checker():
    password = input("Enter the user password: ")
    check = input("let's check your password:")
    while check ==int(input("check the user password: ")):
        password = input("Enter password:")
        
        if password == 1234:
            print("your password is too, short")
        elif password == 12345:
             print("your password is weak , choose another")
        elif password == 12345600:
            print("Password is strong")
        else :
            print("Invalid Password")
            
    input("user password")
    len(password) <= 8
    print("passwordis too short")
    if len (password)==1:
        print("password is weak")
   
    elif len(password) == password:
        print("password is strong")
    else:
        print("Ivalid password")
     
    
    
        
        
        
    
    
    
    
    
    
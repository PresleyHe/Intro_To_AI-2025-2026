password = "BCTS2025"
# password_input = input("What is your password?:")
attempts = 0
max_attempts = 3

while(attempts < max_attempts):
    
    password_input = input("What is your password?:")
    
    max_attempts -= 1
    if password == password_input:
        print("Password correct!")
        break
    
    if attempts < max_attempts:
        print(f"Passworld incorrect! Try again! {max_attempts - attempts} attempts remaining!")
        print("wrong Password!")
    else:
        print("Login Failed! Too many attempts!")
        break
    
     
     
     
     
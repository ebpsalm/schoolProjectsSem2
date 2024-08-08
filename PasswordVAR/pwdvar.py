
def verifyPassword(password):
     pwd_length = len(password)
     special_characters = "~`! @#$%^&*()-_+={}[]|\;:\"<>,./?"
     contains_lower = False
     contains_upper = False
     contains_digit = False
     contains_special_character = False
     
     if (pwd_length >= 8) and (pwd_length <= 18):
          for char in password:
               if char.islower() == True:
                    contains_lower = True
               elif char.isupper() == True:
                    contains_upper = True
               elif char.isdigit() == True:
                    contains_digit = True
               elif char in special_characters:
                    contains_special_character = True
                    
     if contains_lower and contains_upper  and contains_digit  and contains_special_character:
          return 1
     else:
          return 0

separator = "*"*70
print(f"\t\t\tPASSWORD VAR\n{separator}")
while True:
     password = input("Please enter valid password: ")
     if verifyPassword(password=password):
          print("password is valid.")
          break
     else:
          print(f"\t\t*****INVALID PASSWORD*****\nPassword must contain:\n Between 8 and 16 characters.\n Lower case characters.\n Upper case characters.\n At least one digit.\n At least one special character.\n")


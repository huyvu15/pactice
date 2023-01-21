
# def verify_email(email):
#     if 65 <= ord(email[0]) <= 90 or 97 <= ord(email[0]) <= 122:
#         return True
#     else:
#         return False
    
#     for i in email:
#         if i =="@" or i==".":
#             return True
        
#         if email[i] == "@":
#             for j in email[i:]:
#                 if j==".":
#                     return True
#                 else:
#                     return False
    
#     if email[-1] == ".":
#         return False



# email = input()

# if verify_email(email)==True:
#     print("Valid")
# else:
#     print("Invaild")

def verify_email(email):
  for i in email:
    if not (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57):
      return False

  if "@" not in email or "." not in email:
    return False

  if email.index(".") < email.index("@"):
    return False

  return True

email = input()

if verify_email(email)==True:
  print("Valid")
else:
  print("Invalid")


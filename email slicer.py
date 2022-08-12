import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = input("please enter your email").strip()
def check(email):
    if(re.search(regex,email)):
        print("valid email")
        username=email[:email.index("@")]
        domain=email[email.index("@")+1:]
        print(f"Your username is {username} & domain is {domain}")
    else:
        print("email not valid")
check(email)

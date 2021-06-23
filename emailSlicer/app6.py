print("Heyy Welcome to my custom Email Slicer APP!\n")

popular_domains = {
"gmail": "Google",
"outlook":"Microsoft",
"hotmail":"Microsoft",
"yahoo":"Yahoo"}

user_email = input("Heyy What is your email address? ")
user_name = user_email.split('@')[0]
user_domain = user_email.split('@')[-1]
user_domain = user_domain.split('.')[0]

if user_name == user_email or user_domain == "":
    print("please double check your email address!!")
else:
    if user_domain in popular_domains.keys():
        print(f"Heyy {user_name} it seems like your email is registered with {popular_domains[user_domain]}!")
    else:
        print(f"Heyy {user_name} it seems like you have your own custom domain at {user_domain}!")

print("\nThank you for using Me!!")
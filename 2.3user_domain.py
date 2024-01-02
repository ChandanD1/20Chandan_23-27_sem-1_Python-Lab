# Write a program that scans the email address and forms a tuple of username and domain.

emails = input("Enter the Email addresses separated by commas: ")
elist = emails.split(',')

for email in elist:
    username, domain = email.strip().split('@')
    print("Username: ", username, "Domain: ", domain)
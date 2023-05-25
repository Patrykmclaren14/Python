# slice email from user
# split the email using the @, the first part as the username, the second prat is gonna be saved as domain
# split domain using .,

from distutils import extension


def main():
    print(" Welcom tu the email slicer ")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


while True:
    main()

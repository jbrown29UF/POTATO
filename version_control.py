#Joshua Brown

def main():
    def menu():
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

    def encode():
        pass_to_encode = input("Please enter your password to encode: ")
        encoded_pass = " "
        for number in pass_to_encode:
            new_digit = str(int(number) + 3)
            encoded_pass += new_digit
        return

    while True:
        menu()
        menuOption = input("Please enter an option: ")
        if menuOption == "1":
            encode()
            print("Your password has been encoded and stored!\n")
        elif menuOption == "2":
            pass
        elif menuOption == "3":
            break



if __name__ == "__main__":
    main()
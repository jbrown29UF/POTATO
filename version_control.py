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
        encoded_pass = ""
        for number in pass_to_encode:
            new_digit = str((int(number) + 3)%10)
            encoded_pass += new_digit
        return encoded_pass
    def decode(pass_to_decode):
        decoded_pass = ""
        for number in pass_to_decode:
            new_digit = str((int(number)-3)%10)
            decoded_pass += new_digit

        print(f"The encoded password is {pass_to_decode}, and the original password is {decoded_pass}.\n")
    
    password = ""
    while True:
        menu()
        menuOption = input("Please enter an option: ")
        if menuOption == "1":
            password = encode()
            print("Your password has been encoded and stored!\n")
        elif menuOption == "2":
            decode(password)
        elif menuOption == "3":
            break



if __name__ == "__main__":
    main()
"""
Project: Python Text-Based Life Changing Game
"""

__author__ ="UTHSAB CHNADRA PAUL SAJIB"


def main():
    """
    Today we will know about a life changing game of a Bangladeshi Student.
    """

    print("Welcome to a life changing jurney of a Bangladeshi Student!")
    print("After completing HSC what will a BD student do?"
    "There are only two ways.\n1. Admission Test in Bangladesh in different Public University"
    " and \n2. Go to abroad. \nWhich way he/she will choose? [1 or 2]")

    choice = input("Enter your choice:")

    if choice == "1":

        print("Go for admission choaching.")
        print("Where should I go? There are a lot of options.")
        print("1. Medical")
        print("2. Engineering")
        print("3. Versity")

        Wish = input("Enter yoyr wish:")

        match Wish:

            case "1":
                print("Go for Retina, Unmesh")

            case "2":
                print("Go for ACS, UDVASH")

            case "3":
                print("Go for UDVASH")

            case _:
                print("Online Class \nSelf Preparation.")

        print("After publishing result, Students will admit in diffirent universities and\nstart their new life journey!")

    elif choice == "2":

        print("Take IELTS Preparation.\nThere are many IELTS choaching centers.")
        print("1. Mentors'")
        print("2. Banglay IELTS")
        print("3. BARC")
        print("4. 10 Minute School")
        print("5. Shafin's")

        option = input("What will you choose?")

        match option:

            case "1":
                print("Go to Mentors' and take preparation.")

            case "2":
                print("Go to Banglay IELTS and take preparation.")

            case "3":
                print("Go to BARC and take preparation.")

            case "4":
                print("Go to 10 Minute School and take preparation.")

            case "5":
                print("Go to Safin's and take preparation.")

            case _:
                print("Go for Online class and take preparation.")

        print("After geeting desire score, select country.")
        print("Country: Australia")
        print("There are total 6 states and 2 Main teritories.")
        print("Which state will you go? [State / Teritory]")

        userinput = input("Enter your decision:")

        if userinput == "State":
            print("Which state will you go?")
            print("1. New South Wales (NSW)")
            print("2. Victoria")
            print("3. Queensland")
            print("4. South Australia")
            print("5. Western Australia")
            print("6. Tasmania")

            answer = input("Enter your state:")

            if answer == "1":
                print("Welcome to NSW!")

            elif answer == "2":
                print("Welcome to Victoria!")

            elif answer == "3":
                print("Welcome to Queensland!")

            elif answer == "4":
                print("Welcome to South Australia!")

            elif answer == "5":
                print("Welcome to Western Australia!")

            else:
                print("Welcome to Tasmania")

        if userinput == "Teritory":
            print("1. Capital Teritoy")
            print("2. Northern Teritory ")

            answer = input("Enter your Teritory:")

    else:
        print("Last Option: 🎉Suicide!🎉")


if __name__ == "__main__":
    main()
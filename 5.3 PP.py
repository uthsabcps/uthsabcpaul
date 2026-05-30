"""
5.3PP Test template
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


def main():
           CAPACITY: int = 20 # warn if number of people is above this
           occupants: int # the current number of occupants

           occupants = -int(input("Enter current number of occupants: "))
           if occupants > CAPACITY:
               print(f"The safe number of occupants has been exceeded!")
               print(f"The maximum number of occupants is {CAPACITY}.")

if __name__ == "__main__":
    main()

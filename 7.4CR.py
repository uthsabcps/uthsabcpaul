"""
Contact Book App

The program allows users to:
- Add contact
- View contacts
- Update contact
- Delete contact
- Search contact
- Count contacts
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


# Import libraries
from dataclasses import dataclass
from enum import Enum


class Category(Enum):
    """
    Represents contact category.
    """

    FRIEND = "Friend"
    FAMILY = "Family"
    WORK = "Work"


@dataclass
class Contact:
    """
    Stores contact information.
    """

    name: str  # Contact name
    age: int  # Contact age
    mobile: str  # Phone number
    email: str  # Email address 
    category: Category  # Contact category


contact_list: list[Contact] = []  # Global list to store contacts

def show_menu():
    """
    Displays program menu.
    """

    print("\n ===== CONTACT BOOK APP =====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit")


def add_contact():
    """
    Adds new contact.

    Args: None
    Returns: None
    """
    # Pre-declare variables
    name: str  # Stores the user's input name
    contact: Contact  # Represents each contact in the list
    found: bool  # Flag to check if contact already exists

    name = input("Enter your name: ")
    found = False

    for contact in contact_list:
        if contact.name.lower() == name.lower():
          found = True
          
    if found:
        print(f"Contact {name} already exists!")
        return

    age = int(input("Enter your age: "))
    mobile = input("Enter your phone number: ")
    email = input("Enter your Email Address: ")
    input_category = input("Enter category [Friend/Family/Work]: ")            
    
    category = Category[input_category.upper()]
        
    contact_list.append(Contact(name, age, mobile, email, category))

    print("Contact added successfully!")


def view_contact():
    """
    Displays a specific contact.
    
    Args: None
    Returns: None
    """
    # Pre-declare variables
    name: str  # Stores the user's input name
    contact: Contact  # Represents each contact in the list

    name = input("Enter name to view: ")

    for contact in contact_list:
        if contact.name.lower() == name.lower():
            print(f"Name: {contact.name}, Age: {contact.age}, Mobile: {contact.mobile}, Email: {contact.email}, Category: {contact.category.value} ")
            
            return
        
    print("Contact not found!")


def update_contact():
    """
    Updates contact information.

    Args: None
    Returns: None
    """
    # Pre-declare variables
    name: str  # Stores the user's input name
    contact: Contact  # Represents each contact in the list

    name = input("Enter name to update: ")
    
    for contact in contact_list:
        if contact.name.lower() == name.lower():
           contact.age = int(input("Enter your new age: "))
           contact.mobile = input("Enter your new phone number: ")
           contact.email = input("Enter your new Email Address: ")
           input_category = input("Enter new category [Friend/Family/Work]: ")
           
           contact.category = Category[input_category.upper()]
           
           print(f"Name: {name}, Age: {contact.age}, Mobile: {contact.mobile}, Email: {contact.email}, Category: {input_category} ")
           print("Contact updated successfully!")

           return
        
    print("Contact not found!")


def delete_contact():
    """
    Deletes a contact.

    Args: None
    Returns: None
    """
    # Pre-declare variables
    name: str  # Stores the user's input name
    contact: Contact  # Represents each contact in the list

    name = input("Enter name to delete: ")
    
    for contact in contact_list:
        if contact.name.lower() == name.lower():
           contact_list.remove(contact)
        
           print(f"Contact name {name} deleted successfully!")
           return

    print("Contact not found!")


def search_contact():
    """
    Searches contact by partial name.
    """
    # Pre-declare variables
    search_name: str  # Stores search keyword
    contact: Contact  # Represents each contact object 
    found: bool  # Indicates if match found

    search_name = input("Enter name to search: ")
    found = False

    for contact in contact_list:
        if search_name.lower() in contact.name.lower():
            print(f"Found - Name: {contact.name}, Age: {contact.age}, Email: {contact.email}, Mobile: {contact.mobile}, Category: {contact.category.value}")

            found = True

    if not found:
        print("Contact not found!")


def count_contact():
    """
    Displays total contacts.

    Args: None
    Returns: None
    """
    print(f"Total contacts: {len(contact_list)}")


def main():
    """
    Main program loop.
    """
    # Pre-declare variables
    choice: str  # Stores user menu choice
    running: bool  # Controls program loop

    running = True

    while running:
        
        show_menu()

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                add_contact()

            case "2":
                view_contact()

            case "3":
                update_contact()

            case "4":
                delete_contact()

            case "5":
                search_contact()

            case "6":
                count_contact()

            case "7":
                print("Good Bye!!!")
                running = False


if __name__ == "__main__":
    main()




    










    
















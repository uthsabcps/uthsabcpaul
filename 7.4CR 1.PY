"""
7.4CR Task: Mini MyLO Student Management System

The program simulates a simplified version of the MyLO student system. It allows users to 
manage university-related information including units, assignments, study sessions, assingments.
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


# Import libraries
from dataclasses import dataclass
from enum import Enum


class Priority(Enum):
    """
    Stores assingnment priority levels.
    """
    LOW = "Low" # Low priority
    MEDIUM = "Medium" # Medium priority
    HIGH = "High" # High priority


class Status(Enum):
    """
    Stores assingnment status types.
    """
    NOT_STARTED = "Not started" # Task not started
    IN_PROGRESS = "In Progress" # Task in progress
    SUBMITTED = "Submitted" # Task submitted
    COMPLETED = "Completed" # Task completed


@dataclass
class Unit:
    """
    Represents a university unit.
    """
    code: str # Unit code
    name: str # Unit name
    lecturer: str # Lecturer name


@dataclass
class Assignment:
    """
    Represents assignment details.
    """
    title: str # Assignment title
    unit_code: str # Related unit code
    due_date: str # Assignment due date
    marks: int # Total marks
    progress: int # Completion percentage (%s)
    priority: Priority # Assignment priority
    status: Status # Assignment status


@dataclass
class Announcement:
    title: str # Announcement title
    message: str # Announcement message
    date: str # Announcement date


@dataclass
class StudySession:
    unit_code: str # Unit code
    duration: int # Study duration in minutes
    date: str # Study date


units: list[Unit] = [] # Stores all unit objects
assignments: list[Assignment] = [] # Stores all assignment objects
announcements: list[Announcement] = [] # Stores all announcement objects
study_sessions: list[StudySession] = [] # Stores all study session objects


def show_menu():
    """
    Displays the main menu.
    """
    print("\n===== MINI MYLO STUDENT MANAGEMENT SYSTEM =====")

    print("\n1. Add Unit")
    print("2. View Units")
    print("3. Search Unit")
    print("4. Add assignment")
    print("5. View assignments")
    print("6. Update assignment")
    print("7. Delete assignment")
    print("8. Submit assignment")
    print("9. Search assignment")
    print("10. Filter assignment by unit")
    print("11. Filter assignment by Priority")
    print("12. Sort assignment by Due Date")
    print("13. Calculate grade average")
    print("14. Generate grade report")
    print("15. Add announcement")
    print("16. View announcement")
    print("17. Add study session")
    print("18. View study session")
    print("19. Calculate study hours")
    print("20. Exit")


def add_unit():
    """
    Adds a new unit.

    Args: None
    Returns: None
    """
    code = input("Enter unit code: ")
    name = input("Enter unit name: ")
    lecturer = input("Enter lecturer name: ")

    unit = Unit(code, name, lecturer) # Create unit object

    units.append(unit) # Add unit object into list

    print("\n 🎉🎉Unit added successfully!🎉🎉")


def view_units():
    """
    Displays all units.

    Args: None
    Returns: None
    """

    if not units:
        print("No units available.😭")       
        return
    
    for unit in units:
        print(f" Code: {unit.code}")
        print(f"Name: {unit.name}")
        print(f"Lecturer: {unit.lecturer}")


def search_unit():
    """
    Searches unit by code.

    Args: None
    Returns: None
    """

    search_unit_code= input("Enter unit code: ")

    found = False

    for unit in units:
        if unit.code.lower() == search_unit_code.lower():

            print("🎉 Unit Found! 🎉")
            print(f"\nCode: {unit.code}")
            print(f"Name: {unit.name}")
            print(f"Lecturer: {unit.lecturer}")

            found = True

    if not found:
        print("😭")
        print("Unit not found.")


def add_assignment():
    """
    Adds new assignment.

    Args: None
    Returns: None
    """

    title = input("Enter assignment title: ")
    unit_code = input("Enter unit code: ")
    due_date = input("Enter Assignment Due Date: ")
    marks = int(input("Enter total marks: "))
    progress = int(input("Enter progress percentage: "))

    print("Priority Options:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    choice = input("Enter your priority choice: ")

    match choice:

        case "1":
            priority = Priority.LOW

        case "2":
            priority = Priority.MEDIUM

        case "3":
            priority = Priority.HIGH

        case _:
            print("Invalid choice.")
            
            return
    
    status = Status.NOT_STARTED

    # Create assignment object
    assignment = Assignment(title, unit_code, due_date, marks, progress, priority, status)

    assignments.append(assignment) # Add assignment into list

    print("🎉Assignment added successfully!🎉")


def view_assignments():
    """
    Displays all assignments.

    Args: None
    Returns: None
    """

    if not assignments:
        print("No assignment found!")

        return
    
    for assignment in assignments:

        print(f"Title: {assignment.title}")
        print(f"Unit Code: {assignment.unit_code}")
        print(f"Due Date: {assignment.due_date}")
        print(f"Marks: {assignment.marks}")
        print(f"Progress: {assignment.progress}")
        print(f"Priority: {assignment.priority.value}")
        print(f"Status: {assignment.status.value}")
      
       
def update_assignment():
    """
    Updates assignment details.

    Args: None
    Returns: None
    """
    title = input("Enter assignment title to update: ")

    for assignment in assignments:
        if assignment.title.lower() == title.lower():

            new_progress = int(input("Enter new progress: "))

            assignment.progress = new_progress

            print("Status Options: ")
            print("\n1. Not Started")
            print("2. In Progress")
            print("3. Submitted")
            print("4. Completed")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                assignment.status = Status.NOT_STARTED

            elif choice == "2":
                assignment.status = Status.IN_PROGRESS

            elif choice == "3":
                assignment.status = Status.SUBMITTED

            else:
                assignment.status = Status.COMPLETED

            print("Assignment updated successfully!")

            return
        
    print("Assignment not found.")


def delete_assignment():
    """
    Deletes assignment.

    Args: None
    Returns: None
    """
    title = input("Enter assignment title to delete: ")

    for assignment in assignments:

        if assignment.title.lower() == title.lower():

            assignments.remove(assignment)
            print("Assignment deleted successfully! ")

            return
        
    print("Assignment not found.")


def submit_assignment():
    """
    Marks assignment as submitted.

    Args: None
    Returns: None
    """
    title = input("Enter assignment title: ")

    for assignment in assignments:
        if assignment.title.lower() == title.lower():
            assignment.status = Status.SUBMITTED

            print("Assignment submitted successfully!")

            return
        
    print("Assignment not found.")


def search_assignment():
    """
    Searches assignment by title.

    Args: None
    Returns: None
    """

    search_title = input("Enter assignment title to search: ")

    found = False

    for assignment in assignments:
        if assignment.title.lower() == search_title.lower():

            print("Assignment Found!")

            print(f"Title: {assignment.title}")
            print(f"Unit Code: {assignment.unit_code}")
            print(f"Due Date: {assignment.due_date}")

            found = True

    if not found:
       print("Assignment not found.")


def filter_by_unit():
    """
    Filters assignment by unit.

    Args: None
    Returns: None
    """

    unit_code = input("Enter unit code: ")

    found = False

    for assignment in assignments:
        if assignment.unit_code.lower() == unit_code.lower():
            print(f"Title: {assignment.title}")
            print(f"Due Date: {assignment.due_date}")

            found = True

    if not found:
        print("Assignment not found.")


def filter_by_priority():
    """
    Filters assignment by priority.

    Args: None
    Returns: None
    """
    print("Priority Options:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    choice = input("Enter your priority: ")

    if choice == "1":
        selected_priority = Priority.LOW

    elif choice == "2":
        selected_priority = Priority.MEDIUM

    else:
        selected_priority = Priority.HIGH

    for assignment in assignments:
        if assignment.priority == selected_priority:

            print(f"Title: {assignment.title}")
            print(f"Priority: {assignment.priority.value}")


def sort_by_due_date():
    """
    Sort assignment by due dates.

    Args: None
    Returns: None
    """
    sorted_assignments = sorted(assignments, key=lambda assignment: assignment.due_date)

    for assignment in sorted_assignments:
        print(f"Title: {assignment.title}")
        print(f"Due Date: {assignment.due_date}")


def calculate_grade_average() -> float:
    """
    Calculates average marks.

    Args: None
    Returns:
           float: The average 
    """
    # Pre-declare variable
    total: int # Store total marks

    total = 0

    if not assignments:
        return 0

    for assignment in assignments:
        total += assignment.marks

    average = total / len(assignments)

    return average


def generate_report():
    """
    Generates assignment report.

    Args: None
    Returns: None
    """
    #Pre-declare variable
    completed: int # Completed count
    
    total_assignments = len(assignments)
    completed = 0

    for assignment in assignments:
        if assignment.status == Status.COMPLETED:
            completed += 1

    print(f"Total Assignments: {total_assignments}")
    print(f"Completed Assignment: {completed}")


def add_announcement():
    """
    Adds announcement.

    Args: None
    Returns: None
    """

    title = input("Enter announcement title: ")
    message = input("Enter announcement message: ")
    date = input("Enter announcement date: ")

    announcement = Announcement(title, message, date)

    announcements.append(announcement)

    print("Announcement added successfully!")


def view_announcement():
    """
    Displays all announcements.

    Args: None
    Returns: None
    """

    if not announcements:
        print("No announcements available.")
        return

    for announcement in announcements:
        print(f"Title: {announcement.title}")
        print(f"Message: {announcement.message}")
        print(f"Date: {announcement.date}")

        
def add_study_session():
    """
    Adds study session.

    Args: None
    Returns: None
    """

    unit_code = input("Enter unit code: ")
    duration = int(input("Enter duration in minutes: "))
    date = input("Enter study date: ")

    session = StudySession(unit_code, duration, date)

    study_sessions.append(session)

    print("Added study session successfully!")


def view_study_session():
    """
    Displays all study sessions.

    Args: None
    Returns: None
    """

    if not study_sessions:
        print("No study sessions available.")
        return

    for session in study_sessions:
        print(f"Unit Code: {session.unit_code}") 
        print(f"Duration: {session.duration}") 
        print(f"Date: {session.date}") 


def calculate_hours() -> float:
    """
    Calculates total study hours.

    Args: None
    Returns:
           float: 
    """
    # Pre-declare variable
    total_minutes: int # Stores total minutes

    total_minutes = 0

    for session in study_sessions:
        total_minutes += session.duration

    hours = total_minutes / 60 # convert minutes to hours

    return hours


def main():
    """
    Controls the whole program.

    Args: None
    Returns: None
    """
    # Pre-declare variable
    choice: str 

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        match choice:
            
            case "1":
                add_unit()

            case "2":
                view_units()

            case "3":
                search_unit()

            case "4":
                add_assignment()

            case "5":
                view_assignments()

            case "6":
                update_assignment()

            case "7":
                delete_assignment()

            case "8":
                submit_assignment()

            case "9":
                search_assignment()

            case "10":
                filter_by_unit()

            case "11":
                filter_by_priority()

            case "12":
                sort_by_due_date()

            case "13":
                average = calculate_grade_average() 
                print(f"Average Marks: {average:.2f}") 

            case "14":
                generate_report()

            case "15":
                add_announcement()

            case "16":
                view_announcement()

            case "17":
                add_study_session()

            case "18":
                view_study_session()

            case "19":
                hours = calculate_hours()
                print(f"Total Study Hours: {hours:.2f}")

            case "20":
                print("Thank you!")

                break


if __name__ == "__main__":
    main()



   
"""
6.2CR Dictionaries
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


def add_student(results: dict[str, list[int]], sid: str):
    """
    Adds a new student ID.

    Args:
        results: dict[str, list[int]] # Dictionary of student results
        sid: str # Student ID

    Returns: None
    """
    # TODO: Implement this function
    if sid in results:
        print("Student already exists")
    
    else:
        results[sid] = []
        print("Student added successfully")


def add_student_result(results: dict[str, list[int]], sid: str, result: int):
    """
    Adds a result to the results on record for an existing student.

    results: dict[str, list[int]] # Dictionary of student results
    sid: str # Student ID
    result: int # Student result
    
    Reutrns: None
    """
    # TODO: Implement this function
    if sid not in results:
        print(f"There is no student on record with ID: {sid}")

    else:
        if 0 <= result <= 100:
            results[sid].append(result)
            print("Result added successfully!")

        else:
            print("Invalid result. Must be between 0 and 100")


# TODO: Implement calculate_average
def calculate_average(results: dict[str, list[int]]) -> float:
    """
    Calculates the average of all results on record for all students.

    Args:
        results: dict[str, list[int]] # Dictionary of student results

    Returns: float # The calculated average of all student results  
    """
    # Pre-declare variables
    total: int # Total of all unit results for all students, initialised to 0
    count: int # Count of all result entries for all students, initialised to 0
    average: float # Calculated average, initialised to 0

    total = 0
    count = 0
    average = 0

    for student_results in results.values():
        total += sum(student_results)
        count += len(student_results)

    if count >= 1:
        average = total / count

    else:
        print("No student results recorded.")

    return average


# TODO: Implement calculate_cumulative_gpa
def calculate_cumulative_gpa(results: dict[str, list[int]], sid: str) -> float:
    """
    Calculates the GPA of a student's recorded results

    Args:
        results: dict[str, list[int]] # Dictionary of student results
        sid: str # Studnet ID

    Returns: 
           float: The calculated GPA for the given student's results  
    """
    # Pre-declare variables
    gpa_value: int # Calculataed GPA value for current result
    gpa: float # Calculated cumulative GPA, initialised to 0
    stud_results: list[int] # Student's results

    gpa = 0

    if sid in results:
        stud_results = results[sid]

        for result in stud_results:
            gpa_value = 0

            if result >= 80:
                gpa_value = 7

            elif 70 <= result <= 79:
                gpa_value = 6

            elif 60 <= result <= 69:
                gpa_value = 5
            
            elif 50 <= result <= 59:
                gpa_value = 4

            else: 
                gpa_value = 0

            gpa += gpa_value * 12.5
        
        gpa = gpa / (len(stud_results) * 12.5)

    else:
        print(f"No student with id {sid} exists.")

    return gpa

           
def list_students(results: dict[str, list[int]]):
    """
    Displays all students and their results.
    """
    print(f"Displaying students and results for {len(results)} record(s):")
    for k, v in results.items():
        print(f"Results for {k}: {v}")


def main():
    results: dict[str, list[int]] = {} # collection of students and unit results
    sid: str # student ID
    res: int # result in the range 0-100
    choice: int = 0 # user's menu selection

    SID_PROMPT = "Enter the student ID: "
    RES_PROMPT = "Enter a unit result between 0-100: "

    print("Student GPA Calculator")
    while choice != 6:
        print()
        print("1. Add student\n"
              "2. Add result to existing student\n"
              "3. Calculate average\n"
              "4. Calculate GPA\n"
              "5. List students\n"
              "6. Quit")
        choice = int(input("Action: "))
        match choice:
            case 1:
                # TODO: Add code here
                sid = input(SID_PROMPT)
                add_student(results, sid)

            case 2:
                # TODO: Add code here
                sid = input(SID_PROMPT)
                res = int(input(RES_PROMPT))
                add_student_result(results, sid, res)

            case 3:
                # TODO: Add code 
                average = calculate_average(results)
                print(f"Cohort average is {average:.1f}")

            case 4:
                # TODO: Add code here
                sid = input(SID_PROMPT)
                gpa = calculate_cumulative_gpa(results, sid)
                print(f"Cumulative GPA for student {sid} is {gpa:.1f}")

            case 5:
                list_students(results)

            case 6:
                print("Good Bye!!!")


if __name__ == "__main__":
    main()

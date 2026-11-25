def get_letter_grade(score):
    if score < 50:
        return "FF"
    elif 50 <= score <= 69:
        return "CC"
    elif 70 <= score <= 84:
        return "BB"
    elif 85 <= score <= 100:
        return "AA"

def grade_distribution(student_dict):
    counts = {}
    for student in student_dict.values():      
        let_grade = get_letter_grade(student["score"])
        counts[let_grade] = counts.get(let_grade, 0) + 1
    return counts

students = {
    "101": {"name": "Ada", "score": 88},
    "102": {"name": "Ece", "score": 45},
    "103": {"name": "Can", "score": 72}
}
while True:

    user_input = input("(1: Add/Update Student | 2: Remove Student | 3: Show Distribution | 4: Quit): ")

    match user_input:
        case "1":
            id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            score = int(input("Enter Student Score: "))
            students[id] = {"name": name,"score": score}

        case "2":
            del_id = input("Enter Student ID to Remove: ")
            if del_id in students:
                removed = students.pop(del_id)
                print(f"Removed {removed.values[0]}.")
            else:
                print("Student not found.")

        case "3":
            print(grade_distribution(students))

        case "4":
            print("Exiting...")
            break

        case _:
            print("Invalid choice!")



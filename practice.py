
#Week 1 - Data Science Journey
import csv


def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average < 90 and average >= 80:
        return "B"
    elif average < 80 and average >= 70:
        return "C"
    elif average < 70 and average >= 60:
        return "D"
    else:
        return "F"




def get_report(finals):
    for final in finals:
        average = float(final["average"])
        letter = get_letter_grade(average)

        if average >= 60:
            status = "Pass"
        else:
            status = "Fail"

        print(f"Name: {final['name']}")
        print(f"Major: {final['major']}")
        print(f"Average: {round(average, 1)}")
        print(f"Grade: {letter}")
        print(f"Status: {status}")
        print("---")



with open ("Students.csv", "r") as file:
    reader = csv.DictReader(file)
    get_report(reader)


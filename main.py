# Author: zhuoyangjiang zfj5038@psu.edu

def getGradePoint(grade):
    if grade == "A":
        return 4.0
    elif grade == "A-":
        return 3.67
    elif grade == "B+":
        return 3.33
    elif grade == "B":
        return 3.0
    elif grade == "B-":
        return 2.67
    elif grade == "C+":
        return 2.33
    elif grade == "C":
        return 2.0
    elif grade == "D":
        return 1.0
    else:
        return 0.00

def run():
    print("Enter your course 1 letter grade:" , end='')
    gradepoint1 = getGradePoint(input())
    print("Enter your course 1 credit:" , end='')
    credit1 = int(input())
    print(f"Grade point for course 1 is: {gradepoint1}")

    print("Enter your course 2 letter grade:" , end='')
    gradepoint2 = getGradePoint(input())
    print("Enter your course 2 credit:" , end='')
    credit2 = int(input())
    print(f"Grade point for course 2 is: {gradepoint2}")

    print("Enter your course 3 letter grade:" , end='')
    gradepoint3 = getGradePoint(input())
    print("Enter your course 3 credit:" , end='')
    credit3 = int(input())
    print(f"Grade point for course 3 is: {gradepoint3}")

    GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 
    print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
    run()
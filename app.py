import random

choice = int(input("Welcome pick a number: \n1. Predict my age in 5 years\n2. Guess the number game\n3. Calculate average of grades\n4. Who passed the exam checker\nChoice: "))

if choice == 1:
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print(f"Hello, {name}. You are turning {int(age) + 5} in 5 years.")

elif choice == 2:
    random_number = random.randint(1 ,10)
    try_again = 'y'
    while try_again.lower() == 'y':
        guessed_number = input("Guess the number I'm thinking of (between 1 and 10): ")
        if int(guessed_number) == random_number:
            print("Congratulations! You guessed it right.")
            break
        else:
            print(f"Wrong guess. Try again? (y/n)")
            try_again = input()

elif choice == 3:
    def average_grades(*numbers):
        total = 0
        for num in numbers:
            total += num
        average = total / len(numbers)
        return int(average)

    grades = [75, 96, 98, 79, 83, 91, 87]
    print(f"The average grade is {average_grades(*grades)}")

elif choice == 4:
    grades = {}
    num_students = int(input("Enter number of students to add: "))

    for i in range(num_students):
        name = input("Enter student name: ")
        grade = int(input(f"Enter {name}'s grade: "))
        grades[name] = grade #store in dictionary
    
    print("\nPassing Students: ")
    for name, grade in grades.items():
        if grade < 75:
            continue
        print(f"{name} passed with a grade of {grade}")



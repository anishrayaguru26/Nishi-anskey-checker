import csv

def collect_answers():
    # Get total number of questions
    while True:
        try:
            total_questions = int(input("Enter the total number of questions: "))
            if total_questions > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    # Get CSV filename
    while True:
        csv_filename = input("Enter the name for your CSV file (without .csv extension): ").strip()
        if csv_filename:
            csv_filename = f"{csv_filename}.csv"
            break
        print("Please enter a valid filename.")

    # Initialize list to store answers
    answers = []

    # Collect answers for each question
    for question_num in range(1, total_questions + 1):
        answer = input(f"Enter answer for question {question_num} (press Enter for doubt): ").strip().lower()
        if not answer:
            answer = "doubt"
        answers.append([question_num, answer])

    # Write to CSV file
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Answer'])  # Header
        writer.writerows(answers)

    print(f"\nAnswers have been saved to '{csv_filename}'")

if __name__ == "__main__":
    print("Welcome to the Answer Collector!")
    print("This program will help you collect your answers and save them to a CSV file.")
    print("For any question you're not sure about, just press Enter to mark it as 'doubt'.\n")
    
    collect_answers() 
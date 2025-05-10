import csv
import os

def collect_answers(append_mode=False, existing_file=None):
    # Create answers directory if it doesn't exist
    answers_dir = "answers"
    if not os.path.exists(answers_dir):
        os.makedirs(answers_dir)

    # Get total number of questions
    while True:
        try:
            total_questions = int(input("Enter the total number of questions: "))
            if total_questions > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    # Get CSV filename if not in append mode
    if not append_mode:
        while True:
            csv_filename = input("Enter the name for your CSV file (without .csv extension): ").strip()
            if csv_filename:
                csv_filename = f"{csv_filename}.csv"
                break
            print("Please enter a valid filename.")
    else:
        csv_filename = existing_file

    # Initialize list to store answers
    answers = []

    # Get starting question number
    start_question = 1
    if append_mode:
        # Read existing file to get the last question number
        file_path = os.path.join(answers_dir, csv_filename)
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                start_question = max(start_question, int(row[0]) + 1)

    # Collect answers for each question
    for question_num in range(start_question, start_question + total_questions):
        answer = input(f"Enter answer for question {question_num} (press Enter for doubt): ").strip().lower()
        if not answer:
            answer = "doubt"
        answers.append([question_num, answer])

    # Write to CSV file
    file_path = os.path.join(answers_dir, csv_filename)
    mode = 'a' if append_mode else 'w'
    with open(file_path, mode, newline='') as file:
        writer = csv.writer(file)
        if not append_mode:
            writer.writerow(['Question', 'Answer'])  # Header only for new files
        writer.writerows(answers)

    print(f"\nAnswers have been saved to '{file_path}'")

def main():
    print("Welcome to the Answer Collector!")
    print("This program will help you collect your answers and save them to a CSV file.")
    print("For any question you're not sure about, just press Enter to mark it as 'doubt'.\n")
    
    while True:
        print("\nChoose an option:")
        print("1. Create a new answer file")
        print("2. Append to an existing file")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            collect_answers()
        elif choice == "2":
            # List existing files
            answers_dir = "answers"
            if not os.path.exists(answers_dir):
                print("No existing answer files found.")
                continue
                
            files = [f for f in os.listdir(answers_dir) if f.endswith('.csv')]
            if not files:
                print("No existing answer files found.")
                continue
                
            print("\nAvailable files:")
            for i, file in enumerate(files, 1):
                print(f"{i}. {file}")
                
            while True:
                try:
                    file_choice = int(input("\nSelect a file number to append to: ").strip())
                    if 1 <= file_choice <= len(files):
                        collect_answers(append_mode=True, existing_file=files[file_choice-1])
                        break
                    print("Invalid file number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
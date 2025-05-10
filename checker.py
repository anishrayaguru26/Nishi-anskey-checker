import pandas as pd
pd.set_option('display.show_dimensions', False)

# Read both CSV files
file1 = "answers/NA_solutions_part1.csv"
df1 = pd.read_csv(file1)
file2 = "answers/NA_solutions_ak.csv"
df2 = pd.read_csv(file2)

# Rename columns for clarity
df1.columns = ['Question', 'Your_Answer']
df2.columns = ['Question', 'Correct_Answer']

# Merge the dataframes on Question
merged_df = pd.merge(df1, df2, on='Question', how='left')

# Create a list to store all output
output_lines = []

# Function to add text to both console and output list
def add_output(text):
    print(text)
    output_lines.append(str(text))

# Find questions with doubts
add_output("NA_solutions_part1.csv")
add_output("NA_solutions_ak.csv")

doubts = merged_df[merged_df['Your_Answer'] == 'doubt']
add_output("\nDoubts:")
add_output(doubts[['Question', 'Your_Answer']].to_string(index=False))
add_output(f"\nTotal questions with doubts: {len(doubts)}")

# Find mismatched answers (excluding doubts)
mismatched = merged_df[
    (merged_df['Your_Answer'] != merged_df['Correct_Answer']) & 
    (merged_df['Your_Answer'].isin(['a', 'b', 'c', 'd']))
]
add_output("\nQuestions with mismatched answers:")
add_output(mismatched[['Question', 'Your_Answer', 'Correct_Answer']].to_string(index=False))
add_output(f"\nTotal questions with mismatched answers: {len(mismatched)}")

# Get lists of questions for both categories
doubt_questions = doubts['Question'].tolist()
mismatched_questions = mismatched['Question'].tolist()

# Print combined results
add_output("\nAll questions to review: " + str(sorted(doubt_questions + mismatched_questions)))
add_output("Total questions to review: " + str(len(doubt_questions + mismatched_questions)))
add_output("\nQuestions with doubts: " + str(doubt_questions) + " " + str(len(doubt_questions)))
add_output("Questions with wrong answers: " + str(mismatched_questions) + " " + str(len(mismatched_questions)))

# Save output to file
generated_file_name = "checker_results.txt"
with open(generated_file_name, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))






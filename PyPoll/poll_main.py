
import os
import csv

election_csv = os.path.join("election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Read the CSV file
with open('election_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

# Calculate % each candidate won
for candidate in candidates:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})")

# Calculate the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the total number of votes and the winner
print(f"Total Votes: {total_votes}")
print(f"Winner: {winner}")

# Export the results to a text file
with open('election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidates:
        percentage = (candidate_votes[candidate] / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
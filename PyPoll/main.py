#first read the data
import csv
import os
#file_name is for that script works for both raw datas with one change

file_name = 'election_data_1.csv'
path = os.path.join('raw_data', file_name)

with open(path, newline='') as csvfile:
    votes_csv = csv.reader(csvfile, delimiter=',')
    next(votes_csv, None)

    totalvote = 0

    for row in votes_csv:
        totalvote = totalvote + 1


print("Election Results")
print("---------------------")
print("Total votes: " + str(totalvote))

candidate_list = []
# assumed we already know that there are 4 candidates
candidate_1_vote = 0
candidate_2_vote = 0
candidate_3_vote = 0
candidate_4_vote = 0

with open(path, newline='') as csvfile:
    votes_csv = csv.reader(csvfile, delimiter=',')
    next(votes_csv, None)
    i = 0

    for row in votes_csv:
        candidates = row[2]
        #create candidate list
        if candidates not in candidate_list:
            candidate_list.append(row[2])
# for each candidate, count vote.
        if candidates == candidate_list[0]:
            candidate_1_vote = candidate_1_vote + 1
        elif candidates == candidate_list[1]:
            candidate_2_vote = candidate_2_vote + 1
        elif candidates == candidate_list[2]:
            candidate_3_vote = candidate_3_vote + 1
        elif candidates == candidate_list[3]:
            candidate_4_vote = candidate_4_vote + 1
candidate_1_percentage = (candidate_1_vote / totalvote * 100 )
candidate_2_percentage = (candidate_2_vote / totalvote * 100 )
candidate_3_percentage = (candidate_3_vote / totalvote * 100 )
candidate_4_percentage = (candidate_4_vote / totalvote * 100 )

print("-----------------------")
print(str(candidate_list[0]) + ": " + str(candidate_1_percentage) + "% " + str(candidate_1_vote))
print(str(candidate_list[1]) + ": " + str(candidate_2_percentage) + "% " + str(candidate_2_vote))
print(str(candidate_list[2]) + ": " + str(candidate_3_percentage) + "% " + str(candidate_3_vote))
print(str(candidate_list[3]) + ": " + str(candidate_4_percentage) + "% " + str(candidate_4_vote))

# find the winner
print("----------------------")

if candidate_1_vote > candidate_2_vote  and candidate_1_vote > candidate_3_vote and candidate_1_vote > candidate_4_vote:
    print("Winner : " + str(candidate_list[0]))
elif candidate_2_vote > candidate_3_vote and candidate_2_vote > candidate_4_vote:
    print("Winner : " + str(candidate_list[1]))
elif candidate_3_vote > candidate_4_vote:
    print("Winner : " + str(candidate_list[2]))
else:
    print("Winner : " + str(candidate_list[3]))
print("---------------------")


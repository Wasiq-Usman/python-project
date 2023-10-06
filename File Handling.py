# Creating a sample data file with students and their scores
data = """Alice 90 85 78
Bob 76 88 92
Charlie 82 79 85
David 91 94 88
Eve 87 90 92"""

with open("student_scores.txt", "w") as file:
    file.write(data)
# Reading the file and classifying data into students and scores
students_data = {}
with open('student_scores.txt','r') as file:
    for line in file:
        data_parts = line.split()
        student_name = data_parts[0]
        scores =list(map(int,data_parts[1:]))
        students_data[student_name] = scores
print(students_data)
# Calculating average score for each student
for student, scores in students_data.items():
    average = sum(scores)/len(scores)
    print(f'{student}: Average score ={average:.2f}')

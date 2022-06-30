last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subject = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 96, 99]

gradebook = [[subject[0],grades[0]], [subject[1],grades[1]], [subject[2],grades[2]], [subject[3],grades[3]]]

# print(gradebook)

gradebook.append(["computer science", 100])
# print(gradebook)

gradebook.append(["visual arts", 93])
# print(gradebook)

gradebook[-1][1] = gradebook[-1][1] + 5
# print(gradebook)

gradebook[2].remove(96)
# print(gradebook)

gradebook[2].append("Pass")
# print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
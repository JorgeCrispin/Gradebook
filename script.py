last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#create a list called subjects
subjects = ["physics", "calculus", "poetry", "history"]
#create a list called grades
grades = [98, 97, 85, 88]
#create a list called gradebook with subjects and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry",85], ["history", 88]]
#add computer science grade
gradebook.append(["computer science", 100])
#add visual arts grade
gradebook.append(["visual arts", 93])
#add 5 points to the visual arts grade
gradebook[-1][-1] += 5
#remove the 85 grade and replace it with pass fail
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)
print()
#make new list full_gradebook with grades from last semester and this semester
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

college=(108,"Neha George","BCom",75)

print("---------------------------------")

roll_no,name,department,marks=college

print("ROLL NO : ",roll_no)
print("NAME : ",name)
print("DEPARTMENT : ",department)
print("MARK : ",marks)

print("---------------------------------")

if marks>=80:
    grade=("Grade A")
elif marks>=60 and marks<=79:
    grade=("Grade B")
elif marks>=40 and marks<=59:
    grade=("Grade C")
elif marks<40:
    grade=("Fail")
else:
    grade=("Invalid")
print(grade)

print("---------------------------------")

mark=[86,60,72,38,65,91,40,68]
print("Highest Mark : ",max(mark))
print("Lowest Mark : ",min(mark))
print("Class Average : ",sum(mark)/len(mark))

print("---------------------------------")
averege=sum(mark)/len(mark)
if marks > averege:
    print(name,"score more than class average")
else:
    print(name,"not score more than class aveeage")

print("---------------------------------")

mark.sort(reverse=True)
print(mark)
print("Student Rank : ",mark.index(68)+1)

print("---------------------------------")

departments=["BCA","BCom","BCA","BBA","BCom","BBA","BCA","BCom"]
print("Unique departments : ",set(departments))
print("Length of unique departments : ",len(set(departments)))

print("---------------------------------")

print("====================")
print("----Reslut Card----")
print("NAME : ",name)
print("ROLL NO : ",roll_no)
print("DEPARTMENT : ",department)
print("MARK : ",marks)
print("GRADE : ",grade)
print("====================")
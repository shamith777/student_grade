marks =[]
for i in range(1,6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)
avg = sum(marks) / 5
if(avg >= 90):
    grade = "A"
elif(avg >= 75):
    grade = "B"
elif(avg >= 60):
    grade = "C" 
elif(avg >= 50):    
    grade = "D"
else:
    grade = "Fail"

    

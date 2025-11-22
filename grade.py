import sys
if len(sys.argv) != 6:
    print("ERROR: Please provide 5 subject marks as parameters.")
    print("Usage: python3 marks.py <SUB1> <SUB2> <SUB3> <SUB4> <SUB5>")
    sys.exit(1)
marks = list(map(float, sys.argv[1:6]))
print("\n=== INPUT RECEIVED FROM JENKINS PARAMETERS ===")
print("Marks:", marks)
avg = sum(marks) / 5
vg_marks = [m for m in marks if m > 90]
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "Fail"
print("\n===== RESULT =====")
print("Average:", avg)
print("Very Good Marks (>90):", vg_marks if vg_marks else "None")
print("Grade:", grade)

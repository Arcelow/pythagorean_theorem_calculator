import math
print("""
------------------------------------------------------------------------------------------------------
This is a Pythagorean Theorem calculator! Enter '?' if it's unknown. 
No negatives or non-numbers!!
------------------------------------------------------------------------------------------------------
""")
A = input("What is the length of A? ")
B = input("What is the length of B? ")
C = input("What is the length of C? ")
if C == "?":
    AB = float(A) ** 2 + float(B) ** 2
    C_Solution = math.sqrt(AB)
    print(C_Solution)
    exit()
elif B == "?":
    if A != C:
        AC = float(C) ** 2 - float(A) ** 2
        B_solution = math.sqrt(AC)
        print(B_solution)
        exit()
    else:
        print("Impossible! C can't equal A! ")
elif A == "?":
    if B != C:
        BC = float(C) ** 2 - float(B) ** 2
        A_solution = math.sqrt(BC)
        print(A_solution)
        exit()
    else:
        print("C is the largest side! It can't equal B!")
        exit()
elif A or B or C != "?":
    if A or B >= C:
        print("You know everything! But it's still invalid...4.")
        exit()
    else:
        print("You know everything already!")
        exit()




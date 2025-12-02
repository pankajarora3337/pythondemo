P = float(input("Enter your Amount: " ))
R = float(input("Enter interest Rate: "))
T = float(input("Enter Time: "))
si = (P * R * T) / 100
print("simple interest is :", si)
ci = P * ((1 + R / 100) ** T)
Int = (ci - P)
print("Your Compound is: ", Int)
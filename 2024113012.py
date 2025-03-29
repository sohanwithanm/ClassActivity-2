def find_cube_pairs(target):  # added colon at the end of the function definition
    solutions = []           
    max_num = round(target ** (1/3))  # corrected targ to target and *** to **

    #added colon to the end of each looping and conditional statement
    for a in range(1, max_num + 1):  # changed ranges to range
        for b in range(a, max_num + 1):  # changed ranges to range
            if a ** 3 + b ** 3 == target:  # changed *** to ** and targ to target
                solutions.append((a, b))  # changed sol to solutions

    return solutions  # changed sol to solutions, fixed indent

pairs = find_cube_pairs(1729)  
print("Valid cube pairs for 1729:")  # changed printf to print, 1728 to 1729

#changed for a,b to x, taking the whole tuple in x and accessing from there
for x in pairs:  # changed pair to pairs 
    print(f" → {x[0]}³ + {x[1]}³ = {x[0]**3} + {x[1]**3} = 1729")  # changed {a**2} and {b**2} to {a**3} and {b**3}

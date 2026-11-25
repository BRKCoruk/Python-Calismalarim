students = [("Ada",45),("Ece",70),("Can",50)]
passed = 0

for name in students:
    if name[1] >= 50:
        passed = passed + 1
        print(name[0])
print(passed)
    
    



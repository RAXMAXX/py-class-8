str1 = input("enter a sentence:")
num = 1

for i in range(len(str1)):
    if(str1[i]== ' '):
        num+=1

print("Total number of words= ",num)
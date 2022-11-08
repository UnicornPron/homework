numbers = []
with open("numbers.txt") as file:
    lines = file.readlines()
    for i in lines:
      numbers.append([int(n) for n in i.split()])
for f, b, max_num in numbers:
    for num in range (1, max_num+1):
        if (num%f == 0 and num%b==0):
            print("FB")
        elif (num%f == 0):
            print("F")
        elif (num%b == 0):
            print("B")
        else:
            print(num)

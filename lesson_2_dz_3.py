print("Fizz:")
fizz = int(input())
print("Buzz:")
buzz = int(input())
print("3 number:")
num = int(input())
for i in range (1,num):
    if (i%fizz == 0 and i%buzz==0):
        print("FB")
    elif (i%fizz == 0):
        print("F")
    elif (i%buzz == 0):
        print("B")
    else:
        print(i)
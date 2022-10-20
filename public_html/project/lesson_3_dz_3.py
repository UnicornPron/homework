numbers = []
result = []
with open("numbers.txt") as file:
    lines = file.readlines()
    for i in lines:
        numbers.append([int(n) for n in i.split()])
for f, b, max_num in numbers:
    for num in range(1, max_num + 1):
        if num % f == 0 and num % b == 0:
            result.append("FB")
        elif num % f == 0:
            result.append("F")
        elif num % b == 0:
            result.append("B")
        else:
            result.append(num)
results = "\n".join([str(i) for i in result])
my_file = open("results.txt", "w")
my_file.write(results)
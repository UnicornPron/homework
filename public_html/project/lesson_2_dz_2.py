print("How much is the fish?")  # отсылка на песню
number = int(input())
if 1000 <= number:
    print("Too expensive")
elif (number >= 200) and (number <= 500):
    print("Reasonable price")
elif number < 200:
    print("Hehe, good deal")
else:
    print("Okay, man")

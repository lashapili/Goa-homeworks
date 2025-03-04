number=int(input("enter your number: "))
for i in range (number):
    print(i)

yourname=str(input("enter your name: "))
if yourname=="lasha" :
    print("hello")
else:
    print("bye")
score=int(input("enter score: "))
if score>=90:
    print("A")
elif score >= 70   :
    print("B")
elif score >= 50:
    print("C")
else:
    print("D")



while i <= 100:
    if i % 2 == 0:
        print(i, "is Even!")
    else:
        print(i, "is Odd!")
    i = i + 1
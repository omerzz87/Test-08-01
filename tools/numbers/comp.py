

def sumofdigits(num):
    sum=0
    for digit in str(num):
        sum+= int(digit)
    return sum
num = int(input("enter number to sum it:"))
print(sumofdigits(num))



def ispal(numpali):
    return str(numpali) ==str(numpali)[::-1]
while True:
    numpali = int(input("enter number to check if the number is palindrome: "))
    answer=ispal(numpali)
    ispal(numpali)

    if answer:
        print(True)
        break
    else:
        print( False)
        break





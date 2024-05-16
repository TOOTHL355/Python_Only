import time


def Add(value1, value2):
    print(f"Sum of the numbers {value1} and {value2} is {value1 + value2}")


def Subtract(value1, value2):
    print(f"Difference between the numbers {value1} and {value2} is {value1 - value2}")


def Multiply(value1, value2):
    print(f"Product of the numbers {value1} and {value2} is {value1 * value2}")


def Divide(value1, value2):
    if value2 == 0:
        print("cannot divide by 0")
        return 0
    else:
        print(f" {value1} divided by {value2} is {value1 / value2}")


def Read_Int(msg, pos=False, Range_Chk=None):
    while 1:
        value = input(msg)
        value = value[1:] if value.startswith("+") else value
        dx = 1
        msg = "syntax error!!Enter valid number\n"
        if value.startswith("-"):
            dx = -1
            value = value[1:]
            if not value.isnumeric():
                msg = "syntax error!!Enter valid number\n"
                continue
        elif not value.isnumeric():
            continue
        num = dx * int(value)
        if pos and num < 0:
            continue
        if Range_Chk and not Range_Chk[0] <= num <= Range_Chk[1]:
            msg="Enter between range[1-5]\n"
            continue
        return num


while 1:
    print("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n5. Exit")
    choice = Read_Int("Enter the operation\n", True, Range_Chk=(1, 5))
    if choice == 5:
        print("Thank you muji for using this calc")
        time.sleep(2)
        break

    value1 = Read_Int("enter 1st number\n")
    value2 = Read_Int("enter 2nd number\n")
    if choice == 1:
        Add(value1, value2)

    elif choice == 2:
        Subtract(value1, value2)

    elif choice == 3:
        Multiply(value1, value2)

    elif choice == 4:
        Divide(value1, value2)
    print("_________________________________\n")

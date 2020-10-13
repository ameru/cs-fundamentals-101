# Problem I
def problem_1()-> None:
    input_1 = int(input("Enter a number: "))
    print(int((((input_1 * 2) + 10) / 2) - input_1))

# Problem II
def problem_2()-> None:
    input_1 = int(input("Enter a number: "))
    input_2 = int(input("Enter another number: "))
    var3 = input_1 + input_2
    var4 = var3 + input_2
    var5 = var4 + var3
    var6 = var5 + var4
    var7 = var6 + var5
    var8 = var7 + var6
    var9 = var8 + var7
    var10 = var9 + var8
    print((input_1 + input_2 + var3 + var4 + var5
         + var6 + var7 + var8 + var9 + var10) / var7)


# Problem III
def problem_3()-> None:
    input_1 = int(input("Enter a four-digit number, each digit different: "))
    first_digit = input_1 // 1000
    # 3
    second_digit = ((input_1 - (first_digit * 1000)) // 100)
    # 3456 - 3000 = 456 // 100 = 4
    third_digit = (((input_1 - (first_digit * 1000)) - (second_digit * 100))\
    // 10)
    # 3456 - 3000 - 400 = 56 // 10 = 5
    fourth_digit = (((input_1 - (first_digit * 1000)) - (second_digit * 100))\
    - (third_digit * 10))
    # 3456 - 3000 - 400 - 50 = 6
    result = (fourth_digit * 1000) + (second_digit * 100) + (third_digit * 10)\
    + first_digit
    # 6000 + 400 + 50 + 3 = 6453
    diff = max(input_1, result) - min(input_1, result)
    # 6453 - 3456 = 2997
    first_digit2 = diff // 1000
    # 2997 // 1000 = 2
    second_digit2 = ((diff - (first_digit2 * 1000)) // 100)
    # 2997 - 2000 = 997 // 100 = 9
    third_digit2 = (((diff - (first_digit2 * 1000)) - (second_digit2 * 100))\
    // 10)
    # 2997 - 2000 - 900 = 97 // 10 = 9
    fourth_digit2 = (((diff - (first_digit2 * 1000)) - (second_digit2 * 100))\
    - (third_digit2 * 10))
    # 2997 - 2000 - 900 - 90 = 7
    result2 = first_digit2 + second_digit2 + third_digit2 + fourth_digit2
    # 2 + 9 + 9 + 7 = 27
    first_digit3 = result2 // 10
    # 27 // 10 = 2
    second_digit3 = result2 - (first_digit3 * 10)
    # 27 - 20 = 7
    print(int(first_digit3 + second_digit3))
    # 9

# Problem IV
def problem_4()-> None:
    input_1 = int(input("Enter a number 1-50, not div by 7: "))
    result = input_1 / 7
    result2 = result % 1
    first_digit = result2 // 0.1
    second_digit = (result2 // 0.01) % 10
    third_digit = (result2 // 0.001) % 10
    fourth_digit = (result2 // 0.0001) % 10
    fifth_digit = (result2 // 0.00001) % 10
    sixth_digit = (result2 // 0.000001) % 10
    print(int((first_digit + second_digit + third_digit + fourth_digit 
        + fifth_digit + sixth_digit)))

if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()

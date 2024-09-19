from sqlalchemy import Integer


def get_digits_from_number(number: Integer, base: Integer) -> list[Integer]:
    numList = []
    if number == 0: return [0]
    while number >= 1:
        d = number % base
        numList.append(d)
        number = number//base
    return numList

# assert get_digits_from_number(0, 2) == [0]
# assert get_digits_from_number(1, 10) == [1]
# assert get_digits_from_number(12, 10) == [2, 1]
# assert get_digits_from_number(123, 10) == [3, 2, 1]


def get_number_from_digits(digits: list[Integer], base: Integer) -> Integer:
    k = 0
    num = 0
    for digit in digits:
        num += digit * (pow(base,k))
        k += 1
    return num


# assert get_number_from_digits([0], 10) == 0
# assert get_number_from_digits([1], 10) == 1
# assert get_number_from_digits([2, 1], 10) == 12
# assert get_number_from_digits([3, 2, 1], 10) == 123


def add_via_digits(lhs_digits: list[Integer], rhs_digits: list[Integer], base: Integer) -> list[Integer]:
    carry = 0
    numList = []
    maxLen = max(len(lhs_digits),len(rhs_digits))
    
    if(maxLen == len(lhs_digits)):
        for i in range(maxLen - len(rhs_digits)):
            rhs_digits.append(0)
    else:
        for i in range(maxLen - len(lhs_digits)):
            lhs_digits.append(0)
    
    for i in range(maxLen):
        num = (carry + lhs_digits[i] + rhs_digits[i]) % base
        carry = (carry + lhs_digits[i] + rhs_digits[i]) // base
        numList.append(num)
    if carry > 0 : numList.append(carry)
    return numList



        

# for lhs in range(100):
#     for rhs in range(100):    
#         lhs_digits = get_digits_from_number(lhs, 10)
#         rhs_digits = get_digits_from_number(rhs, 10)
#         assert add_via_digits(get_digits_from_number(lhs, 10), get_digits_from_number(rhs, 10), 10) == get_digits_from_number(lhs + rhs, 10)



def grade_school_multiplication(lhs_digits: list[Integer], rhs_digits: list[Integer], base: Integer) -> list[Integer]:
    numList = [0] * (len(lhs_digits) + len(rhs_digits))
    
    for i in range(len(lhs_digits)):
        carry = 0
        for j in range(len(rhs_digits)):
            num = lhs_digits[i] * rhs_digits[j] + numList[i + j] + carry
            numList[i + j] = num % base
            carry = num // base
        
        numList[i + len(rhs_digits)] += carry
    
    
    while len(numList) > 1 and numList[-1] == 0:
        numList.pop()
    return numList


# for lhs in range(100):
#     for rhs in range(100):
#         lhs_digits = get_digits_from_number(lhs, 10)
#         rhs_digits = get_digits_from_number(rhs, 10)
#         assert grade_school_multiplication(get_digits_from_number(lhs, 10), get_digits_from_number(rhs, 10), 10) == get_digits_from_number(lhs * rhs, 10)



def basic_exp(x: Integer, n: Integer) -> Integer:
    if n==0: return 1
    num = x
    for i in range(n -1):
        num *= x
    return num

# for x in range(-10, 10):
#     for n in range(10):
#         assert basic_exp(x, n) == x ** n

def repeated_squaring(x: Integer, k: Integer) -> Integer:
    if k==0: return 1
    num = x
    for i in range(k):
        x *= x
    return x

for x in range(-10, 10):
    for k in range(1, 4):
        assert repeated_squaring(x, k) == x ** (2 ** k)
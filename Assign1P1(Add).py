def display_divmod(a,b):
    quotient = a // b # Integer division
    remainder = a % b
    
    if quotient>b:
        divmod(quotient,b)
    
    

def add(lhs_digits: list[int], rhs_digits: list[int], base: int):
    length = max(len(lhs_digits), len(rhs_digits))
    result = [0] * length
    carry = 0

    for i in range(length):
        left_digit = lhs_digits[i] if i < len(lhs_digits) else 0
        right_digit = rhs_digits[i] if i < len(rhs_digits) else 0

        digit_sum = left_digit + right_digit + carry
        carry = digit_sum // base
        result[i] = digit_sum % base
    if carry > 0:
        result.append(carry)
    return result


def mul(lhs_digits: list[int], rhs_digits: list[int], base: int):
    len_lhs = len(lhs_digits)
    len_rhs = len(rhs_digits)
    result = [0] * (len_lhs + len_rhs)

    for i in range(len_lhs):
        for j in range(len_rhs):
            product = lhs_digits[i] * rhs_digits[j]
            result[i + j] += product
            k = i + j
            while result[k] >= base:
                carry = result[k] // base
                result[k] %= base
                k += 1
                result[k] += carry

    while result[-1] == 0 and len(result) >1:
        result.pop()

    return result


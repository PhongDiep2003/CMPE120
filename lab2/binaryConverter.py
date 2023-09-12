def to_binary(number: int) -> str:
    """
    This is a comment
    Input: Number (integer)
    Output: String
    Example: Input = 43, Output = "101011"
    """
    answer = ""
    while True:   
        quotient = number // 2
        remainder = number % 2
        number = quotient
        answer = str(remainder) + answer
        if (quotient == 0):
            answer = "0b" + answer
            break

    return answer
n=int(input())
last_digit = n % 10
first_digit = n
while first_digit >= 10:
    first_digit = first_digit // 10
result = first_digit + last_digit
print(result)

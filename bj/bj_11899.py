def add_p(s):
    balance = 0
    result = 0
    for char in s:
        if char == "(":
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                result += 1
                balance = 0
    
    result += balance
    return result

s = input()

print(add_p(s))

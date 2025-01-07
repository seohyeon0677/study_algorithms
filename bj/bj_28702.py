def fizzbuzz_next(strings):
    sequence = []
    for s in strings:
        if s.isdigit():
            sequence.append(int(s))
        else:
            sequence.append(s)

    last_num = None
    from_end = None
    for i, item in enumerate(reversed(sequence)):
        if isinstance(item, int):
            last_num = item
            from_end = i + 1
            break
    
    next_num = last_num + from_end
    if next_num % 3 == 0 and next_num % 5 == 0:
        return "FizzBuzz"
    elif next_num % 3 == 0:
        return "Fizz"
    elif next_num % 5 == 0:
        return "Buzz"
    else:
        return str(next_num)
    
input_strings = [input().strip() for _ in range(3)]

print(fizzbuzz_next(input_strings))

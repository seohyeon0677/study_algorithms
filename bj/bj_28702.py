def next_output(inputs):
    def fizzbuzz_string(n):
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return str(n)
    
    a, b, c = inputs[0], inputs[1], inputs[2]

    for i in range(1, 101):
        if fizzbuzz_string(i) == a and fizzbuzz_string(i + 1) == b and fizzbuzz_string(i + 2) == c:
            return fizzbuzz_string(i + 3)

inputs = [input().strip() for _ in range(3)]

print(next_output(inputs))

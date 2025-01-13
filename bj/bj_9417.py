def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_max_gcd(test_cases):
    results = []
    for numbers in test_cases:
        max_gcd = 0
        length = len(numbers)
        for i in range(length):
            for j in range(i + 1, length):
                max_gcd = max(max_gcd, gcd(numbers[i], numbers[j]))
        results.append(max_gcd)
    return results

n = int(input())
test_cases = []
for _ in range(n):
    test_cases.append(list(map(int, input().split())))

results = find_max_gcd(test_cases)
for result in results:
    print(result)

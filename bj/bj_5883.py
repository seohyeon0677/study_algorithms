N = int(input())
B = [int(input()) for _ in range(N)]
values = set(B)

max_length = 0
for value in values:
    filtered = [b for b in B if b != value]

    current_length = 1
    max_local_length = 0
    for i in range(1, len(filtered)):
        if filtered[i] == filtered[i - 1]:
            current_length += 1
        else:
            max_local_length = max(max_local_length, current_length)
            current_length = 1
    max_local_length = max(max_local_length, current_length)
    
    max_length = max(max_length, max_local_length)

print(max_length)

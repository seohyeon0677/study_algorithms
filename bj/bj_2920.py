music = list(map(int, input().split()))

count = 0
for i in range(8):
    if music[i] == i + 1:
        count += 1
    elif music[i] == 8 - i:
        count -= 1
    else:
        break

if count == 8:
    print("ascending")
elif count == -8:
    print("descending")
else:
    print("mixed")

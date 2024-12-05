n = int(input())
workers = [tuple(map(int, input().split())) for _ in range(n)]

time_cover = [0] * 1001 #1000?

for start, end in workers:
    for hour in range(start, end):
        time_cover[hour] += 1

max_cover_time = 0
for i, (start, end) in enumerate(workers):
    temp_cover = time_cover[:]
    for hour in range(start, end):
        temp_cover[hour] -= 1
    cover_time = sum(1 for hour in temp_cover if hour > 0)
    max_cover_time = max(max_cover_time, cover_time)

print(max_cover_time)

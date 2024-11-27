dwarfs = [int(input()) for _ in range(9)]

dwarfs = sorted(dwarfs)

for d1 in range(0,8):
    for d2 in range(d1, 9):
        seven_dwarfs = [dwarfs[i] for i in range(0, 9) if i != d1 and i != d2]
        if sum(seven_dwarfs) == 100:
            for dwarf in seven_dwarfs:
                print(dwarf)

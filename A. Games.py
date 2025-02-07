n = int(input())

home_colors = []
away_colors = []

for _ in range(n):
    h, a = map(int, input().split())
    home_colors.append(h)
    away_colors.append(a)

conflicts = 0

for i in range(n):
    for j in range(n):
        if home_colors[i] == away_colors[j]:
            conflicts += 1

print(conflicts)
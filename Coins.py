a = b = c = 0  # Initialize scores
for _ in range(3):
    comp = input().strip()
    if comp[1] == '>':  # First coin is heavier
        if comp[0] == 'A':
            a += 1
        elif comp[0] == 'B':
            b += 1
        else:
            c += 1
    else:  # Second coin is heavier
        if comp[2] == 'A':
            a += 1
        elif comp[2] == 'B':
            b += 1
        else:
            c += 1
 
# Create a list of (coin, score) and sort by score
coins = [('A', a), ('B', b), ('C', c)]
coins.sort(key=lambda x: x[1])  # Sort by weight
 
# If we don't get unique scores (0,1,2), it's impossible
if [coins[0][1], coins[1][1], coins[2][1]] != [0, 1, 2]:
    print("Impossible")
else:
    print("".join([coins[0][0], coins[1][0], coins[2][0]]))  # Print ordered coins
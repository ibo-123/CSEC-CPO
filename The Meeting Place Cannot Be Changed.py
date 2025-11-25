def check(T, position, velocity):
    max_left = -1e18
    min_right = 1e18
    
    for i in range(len(position)):
        max_left = max(max_left, position[i] - velocity[i] * T)
        min_right = min(min_right, position[i] + velocity[i] * T)
    
    return max_left <= min_right
def Binary(Position , Velocity):
        left , right = 0.0 , 1e18
        for i in range(200):
                mid = (left + right)/2
                if check(mid ,Position , Velocity):
                        right = mid
                else:
                        left = mid
        return right
n = int(input())
m = list(map(int , input().split()))
l = list(map(int , input().split()))
ans = Binary(m , l)
print(f"{ans:.10f}")

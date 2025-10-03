N = int(input())
alice = list(map(int, input().split()))
M = int(input())
bob = list(map(int, input().split()))

i = j = 0
merged = []

while i < N and j < M:
    if alice[i] <= bob[j]:
        merged.append(alice[i])
        i += 1
    else:
        merged.append(bob[j])
        j += 1

while i < N:
    merged.append(alice[i])
    i += 1
while j < M:
    merged.append(bob[j])
    j += 1
print(*merged)

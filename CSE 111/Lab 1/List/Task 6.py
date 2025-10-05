def max_teams(n, k, participants):
    eligible_students = sum(1 for y in participants if 5 - y >= k)
    return eligible_students // 3

n, k = map(int, input().split()) 
participants = list(map(int, input().split())) 

print(max_teams(n, k, participants))

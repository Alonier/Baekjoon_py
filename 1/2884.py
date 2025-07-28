hour, min = map(int, input().split())

hour = hour if min >= 45 else  hour - 1
hour = hour if hour >= 0 else  23
min = min - 45 if min >= 45 else  15 + min

print(hour,min)
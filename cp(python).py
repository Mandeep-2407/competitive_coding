t = int(input())
# # t=1
# # n, m = map(int, input().split())
# # a = list(map(int, input().split()))
# # a.sort()
# import math


while t != 0:
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    if len(set(a)) == 1:
        print(0)
    else:
        for i in range(1, len(a) - 1):
            if a[i] != a[i + 1] and a[i] != a[i - 1]:
                ans += 1
            elif a[i] != a[i - 1]:
                ans += 2
            else:
                continue
        if a[len(a) - 1] != a[len(a) - 2]:
            ans += 2
        print(ans)
    t -= 1

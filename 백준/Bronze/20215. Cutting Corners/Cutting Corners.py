w, h = map(int, input().split())
ans = w + h - (w**2 + h**2)**0.5
print(ans)

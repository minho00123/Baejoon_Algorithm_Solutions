import math

num1, num2 = map(int, input().split())
area_in_arces = math.ceil((num1 * num2) / (5 * 4840))
print(area_in_arces)

first_KWH, additional_usage = map(int, input().split())
n = int(input())
for i in range(n):
  customer_energy_usage = int(input())
  if customer_energy_usage <= 1000:
    print(customer_energy_usage, customer_energy_usage * first_KWH)
  else:
    print(customer_energy_usage, (1000 * first_KWH) + ((customer_energy_usage - 1000) * additional_usage))

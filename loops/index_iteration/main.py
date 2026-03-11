prices = [29.99, 45.50, 12.75, 38.20]
for i in range(len(prices)):
    if i == 0:
        discount_rate = 0.10
    elif i == 1:
        discount_rate = 0.20
    elif i == 2:
        discount_rate = 0.15
    elif i == 3:
        discount_rate = 0.05
    prices[i] = prices[i] * (1-discount_rate)
    print(f"Updated price for item {i}: ${prices[i]:.2f}")
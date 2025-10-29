prices = [100,300,540,2300,1200,800,1500]

discount = 10 # 10% discount

final_prices = []

for price in prices:
    discounted_price = price - (price * discount / 100)
    final_prices.append(discounted_price)

print(final_prices)


# Solution using numpy for better performance
import numpy as np

prices_array = np.array([100,300,1200,800,1500])
discount = 10 # 10% discount

final_prices_array = prices_array - (prices_array * discount / 100)
print(final_prices_array)
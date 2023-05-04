import pandas as pd
import matplotlib.pyplot as plt

# Read the exchange rate data
exchange_rate = pd.read_csv('../python/dataset.csv', index_col='Date')

# Add a 'US' column with a constant value of 1 to represent the USD exchange rate
exchange_rate['US'] = 1.0

# Plot the exchange rates of various currencies against the USD
fig, ax = plt.subplots(figsize=(10, 6))

for country in exchange_rate.columns:
    if country != 'US':
        ax.plot(exchange_rate.index, exchange_rate[country] / exchange_rate['US'], label=country)

ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Exchange Rate (Normalized to USD)')
ax.set_title('Exchange Rates of Various Currencies Against the USD')

plt.show()

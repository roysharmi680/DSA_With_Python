import matplotlib.pyplot as plt

days = ["mon", "tue", "wed", "thu", "fri"]
temperature = [20, 30, 29, 32, 31]

plt.plot(days, temperature, marker="o")
plt.title("temperature over five days")
plt.xlabel("days")
plt.ylabel("temperature")
plt.grid(True)
plt.show()
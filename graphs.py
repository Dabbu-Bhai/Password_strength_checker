import matplotlib.pyplot as plt

# -------------------------------
# 4. Line Graph (Comparison)
# -------------------------------
def plot_graph(lengths, dict_times, brute_times):
    data = sorted(zip(lengths, dict_times, brute_times))
    lengths, dict_times, brute_times = zip(*data)

    plt.plot(lengths, dict_times, marker='o', label="Dictionary Attack")
    plt.plot(lengths, brute_times, marker='o', label="Brute Force")

    plt.xlabel("Password Length")
    plt.ylabel("Time (seconds)")
    plt.title("Password Cracking Time Comparison")
    plt.legend()
    plt.grid()

    plt.show()

# -------------------------------
# 5. Bar Chart
# -------------------------------
def plot_bar_chart(passwords, dict_times, brute_times):
    import numpy as np

    x = np.arange(len(passwords))
    width = 0.35

    plt.bar(x - width/2, dict_times, width, label='Dictionary')
    plt.bar(x + width/2, brute_times, width, label='Brute Force')

    plt.xlabel("Passwords")
    plt.ylabel("Time (seconds)")
    plt.title("Attack Time Comparison (Bar Chart)")
    plt.xticks(x, passwords, rotation=30)

    plt.legend()
    plt.grid(axis='y')

    plt.show()
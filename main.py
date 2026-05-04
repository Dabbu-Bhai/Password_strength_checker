from check import check_strength
from dictionary import dictionary_attack
from bruteforce import brute_force
from graphs import plot_graph , plot_bar_chart

# -------------------------------
#  MAIN FUNCTION
# -------------------------------
def main():
    print("🔐 Password Strength Analyzer\n")

    lengths = []
    dict_times = []
    brute_times = []
    passwords = []
    strengths = []

    n = int(input("How many passwords to test? "))

    for i in range(n):
        print(f"\n--- Password {i+1} ---")
        password = input("Enter password: ")

        strength = check_strength(password)

        dict_found, dict_time = dictionary_attack(password, "rockyou.txt")
        brute_found, brute_time = brute_force(password)

        lengths.append(len(password))
        dict_times.append(dict_time)
        brute_times.append(brute_time)
        passwords.append(password)
        strengths.append(strength)

        print("\nRESULT:")
        print("Strength:", strength)
        print("Dictionary Attack:", "Found" if dict_found else "Not Found", f"({dict_time:.4f} sec)")
        print("Brute Force:", "Found" if brute_found else "Not Found (limited)", f"({brute_time:.4f} sec)")

    print("\n📊 Generating graphs...")

    plot_graph(lengths, dict_times, brute_times)
    plot_bar_chart(passwords, dict_times, brute_times)


# -------------------------------
# RUN PROGRAM
# -------------------------------
if __name__ == "__main__":
    main()
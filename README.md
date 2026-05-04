# 🔐 Password Strength Analyzer

A Python-based cybersecurity mini-project that analyzes password strength and demonstrates how different password cracking techniques behave.

---

## 🚀 Project Overview

This project evaluates the **strength of passwords** and simulates two common attack methods:

* 📖 Dictionary Attack
* 💣 Brute Force Attack (limited)

It also visualizes the results using graphs for better understanding.

---

## ✨ Features

* 🔍 Password Strength Checker (Weak / Medium / Strong)
* 📖 Dictionary Attack Simulation using wordlist
* 💣 Brute Force Attack (limited for demonstration)
* ⏱️ Time measurement for each attack
* 📊 Data Visualization:

  * Line Graph (Trend Analysis)
  * Bar Chart (Attack Comparison)

---

## 🛠️ Technologies Used

* Python 🐍
* Matplotlib 📊
* Regex (re module)
* itertools & string

---

## 📁 Project Structure

```
Password_strength_checker/
│
├── main.py
├── rockyou.txt
├── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/Dabbu-Bhai/Password_strength_checker.git
cd Password_strength_checker
```

2. Install dependencies:

```bash
pip install matplotlib
```

3. Run the program:

```bash
python main.py
```

---

## ▶️ Usage

* Enter number of passwords
* Input passwords one by one
* View:

  * Strength classification
  * Attack results
  * Time taken

---

## 📸 Screenshots

### 🔹 Line Graph (Password Length vs Time)

<img width="797" height="682" alt="image" src="https://github.com/user-attachments/assets/a99b146d-c6c1-4116-b8a5-5457318a12ec" />


### 🔹 Bar Chart (Attack Comparison)

<img width="1672" height="908" alt="image" src="https://github.com/user-attachments/assets/0e364118-a11e-40ab-86bb-86d55328401a" />

---

## 📊 Sample Output

```
Password: Secure@123
Strength: Strong
Dictionary Attack: Not Found (0.45 sec)
Brute Force: Not Found (limited) (2.10 sec)
```

---

## 🧠 Key Learnings

* Weak passwords are easily cracked using dictionary attacks
* Brute force attacks become slower as password length increases
* Strong passwords significantly improve security

Studies also show that weak passwords are very common, making them easy targets for attackers ([arXiv][1])

---

## ⚠️ Disclaimer

This project is created for **educational purposes only**.
Do not use it for unauthorized password cracking.

---

## 📌 Future Improvements

* Entropy-based strength calculation
* GUI / Web interface
* Larger dataset analysis
* Real-time password suggestions

---

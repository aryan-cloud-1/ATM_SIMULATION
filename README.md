<div align="center">

# 🏧 ATM Simulation

### *Experience banking from your terminal*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=gnometerminal&logoColor=white)

<br/>

> 💡 A sleek, command-line based ATM simulation built in Python — supporting deposits, withdrawals, balance checks, and transaction statements, all in one clean interactive loop.

<br/>

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 💰 **Check Balance** | View your current account balance instantly |
| ➕ **Deposit** | Add funds to your account with input validation |
| ➖ **Withdraw** | Withdraw funds with insufficient-funds protection |
| 📋 **Statement** | View a complete summary of all your transactions |
| 🚪 **Exit** | Gracefully exit the ATM session |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.x** installed on your machine
- A terminal / command prompt

### ▶️ Run the Simulation

```bash
# Clone the repository
git clone https://github.com/aryan-cloud-1/ATM_SIMULATION.git

# Navigate into the directory
cd ATM_SIMULATION

# Run the ATM simulation
python ATM.py
```

---

## 🖥️ Demo

```
╔══════════════════════════════╗
║       Welcome to ATM         ║
╚══════════════════════════════╝

1-> Check Balance
2-> Deposit
3-> Withdraw
4-> Statement
5-> Exit

Enter your choice(1-5): 2
Enter the amount to be deposited: 1000
1000.0 deposited
Balance =  1000.0

Enter your choice(1-5): 3
Enter the amount to be withdrawn: 300
300.0 withdrawn
Balance remains =  700.0

Enter your choice(1-5): 4
Deposit = 1000.0
Withdraw = 300.0
700.0

Enter your choice(1-5): 5
Thank you for using the ATM
```

---

## 🗂️ Project Structure

```
ATM_SIMULATION/
│
├── ATM.py          # Main source file — all logic lives here
└── README.md       # Project documentation (you're reading it!)
```

---

## 🔍 Code Breakdown

```python
ATM.py
├── Balance            → Global variable tracking current balance
├── statement          → Dictionary storing total deposits & withdrawals
│
├── checkBalance()     → Prints the current balance
├── Deposit()          → Accepts & validates deposit amount, updates balance
├── Withdraw()         → Validates & processes withdrawal, handles edge cases
├── Statement()        → Displays transaction summary
└── ATM()              → Main loop — drives the menu-driven interface
```

---

## 🛡️ Input Validation

The simulation handles the following edge cases gracefully:

- ❌ **Negative or zero amounts** → Prints `"Enter a valid amount"`
- ❌ **Overdraft attempts** → Prints `"Insufficient funds"`
- ❌ **Invalid menu choices** → Prints `"Invalid input"`

---

## 🧰 Tech Stack

<div align="center">

| Technology | Usage |
|---|---|
| 🐍 Python 3 | Core programming language |
| 📦 Built-ins only | No external libraries required |

</div>

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/YourFeature`)
3. 💾 Commit your changes (`git commit -m 'Add YourFeature'`)
4. 📤 Push to the branch (`git push origin feature/YourFeature`)
5. 🔃 Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

<div align="center">

Made with ❤️ by [aryan-cloud-1](https://github.com/aryan-cloud-1)

⭐ *If you found this helpful, give it a star!* ⭐

</div>

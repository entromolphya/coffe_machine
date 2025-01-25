
---

# Coffee Machine Project

This is a Python-based Coffee Machine simulation that allows users to choose from a menu of drinks, make payments, and track resources. The program uses a simple menu system, manages resources (water, milk, coffee beans), handles payment, and serves coffee. Users can view reports, buy multiple drinks, and exit when done.

## Features
- **Menu Options:** Users can choose from a list of drinks (coffee, tea, etc.).
- **Resource Management:** Ensures there are enough resources (water, milk, coffee beans) before making a drink.
- **Payment System:** Simulates a payment system that accepts coins and ensures payment is received.
- **Reports:** Users can check available resources and earnings.
- **Clear Screen:** The program clears the screen for a cleaner interface.

## How to Play
1. Run the program.
2. Choose a drink from the menu (e.g., coffee, tea).
3. The machine will check if enough resources are available and request payment.
4. If resources are sufficient and payment is made, the machine will make the coffee.
5. Users can view reports or quit the program by typing "off" at any time.

### Available Drinks:
- The drink menu is dynamic and will show the available options based on the predefined drinks in the `Menu` class.

### Commands:
- **"off":** Turn off the coffee machine.
- **"report":** Show current resources and money earned.
- **Drink Names:** Choose a drink from the menu (e.g., "latte", "espresso").

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/entromolphya/coffe_machine.git
   ```

2. Navigate to the project directory:
   ```bash
   cd coffe_machine
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## Requirements
- Python 3.x

## Game Flow
1. The program asks what drink you want from the menu.
2. After selecting a drink, it checks if there are enough resources.
3. If resources are available, it prompts for payment.
4. Once the payment is confirmed, the coffee is prepared.
5. The program will then ask if you'd like another drink.
6. You can also type "report" to view the current resources and money or "off" to stop the program.

## Enjoy your coffee!

---

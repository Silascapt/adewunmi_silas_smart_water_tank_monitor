# Smart Water Tank Monitoring System

## What it does
This Python mini project simulates a water tank monitoring system. The user enters the tank capacity and water-level readings, and the program calculates the amount of water available, reports the tank status, and recommends whether a pump should be on, off, or on standby.

## Features
- Accepts tank capacity and water-level readings.
- Calculates the available water volume in litres.
- Classifies the tank as low, normal, or high.
- Recommends a pump action to help prevent dry running or overflow.
- Estimates the time needed to fill the tank using the pump flow rate entered by the user.
- Stores readings in a list and displays reading history.

## My own twist
The program includes a **sudden water-level drop alert**. If a new reading is at least 15 percentage points lower than the previous reading, it displays a leak/unusual-usage warning. This is only an alert based on entered readings; it does not prove that a leak exists.

## How to run it
1. Install Python 3, or use an Android Python app such as Pydroid 3.
2. Save the program as `smart_water_tank_monitor.py`.
3. Run:

```bash
python smart_water_tank_monitor.py
```

## Sample output
```text
SMART WATER TANK MONITORING SYSTEM
Enter tank capacity in litres: 1000

MENU
1. Enter a new water-level reading
2. View reading history
3. Exit
Choose an option (1-3): 1
Enter current water level (0-100%): 15
Enter pump flow rate (litres per hour): 250

--- TANK MONITORING REPORT ---
Tank capacity: 1000.0 litres
Current water level: 15.0%
Water available: 150.0 litres
Status: LOW LEVEL - refill is needed.
PUMP ON: water level is low.
Estimated time to fill completely: 3.40 hours
```

## What I learned
- How to use functions to divide a program into smaller tasks.
- How to validate numeric input with `try` and `except`.
- How to use lists and loops to store and display readings.
- How conditional statements can be used to make simple monitoring decisions.

## Author
Adewunmi Silas Adeyemi
ND2 Mechatronics Engineering, Yaba College of Technology

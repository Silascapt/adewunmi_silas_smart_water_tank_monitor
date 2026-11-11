"""
Smart Water Tank Monitoring System
A beginner-friendly Python simulation for monitoring tank level and pump control.

This is a software simulation. It does not connect to real sensors or control real pumps.
"""

# Store each reading so the user can review the tank's history.
level_history = []


def get_tank_capacity():
    """Ask for the tank capacity and return a valid value in litres."""
    while True:
        try:
            capacity = float(input("Enter tank capacity in litres: "))
            if capacity <= 0:
                print("Capacity must be greater than zero. Try again.")
            else:
                return capacity
        except ValueError:
            print("Please enter a number, for example 1000.")


def get_water_level(capacity):
    """Ask for the current water level and return a valid percentage."""
    while True:
        try:
            level = float(input("Enter current water level (0-100%): "))
            if level < 0 or level > 100:
                print("Water level must be between 0 and 100%.")
            else:
                return level
        except ValueError:
            print("Invalid input. Enter a number between 0 and 100.")


def calculate_water_volume(capacity, level_percent):
    """Convert the level percentage into the amount of water in litres."""
    return capacity * level_percent / 100


def check_tank_status(level_percent):
    """Return a status message based on the water level."""
    if level_percent <= 20:
        return "LOW LEVEL - refill is needed."
    elif level_percent < 90:
        return "NORMAL LEVEL - tank is operating normally."
    else:
        return "HIGH LEVEL - tank is almost full."


def recommend_pump_action(level_percent):
    """Recommend whether the simulated pump should run or stop."""
    if level_percent <= 20:
        return "PUMP ON: water level is low."
    elif level_percent >= 90:
        return "PUMP OFF: tank is full enough; prevent overflow."
    else:
        return "PUMP STANDBY: water level is within the normal range."


def estimate_refill_time(capacity, level_percent, pump_rate):
    """Estimate refill time in hours using a user-provided pump rate."""
    water_needed = capacity - calculate_water_volume(capacity, level_percent)
    if water_needed <= 0:
        return 0
    return water_needed / pump_rate


def show_reading(capacity, level_percent, pump_rate):
    """Display the current reading, status, pump recommendation and estimate."""
    volume = calculate_water_volume(capacity, level_percent)
    status = check_tank_status(level_percent)
    pump_action = recommend_pump_action(level_percent)
    refill_time = estimate_refill_time(capacity, level_percent, pump_rate)

    print("\n--- TANK MONITORING REPORT ---")
    print(f"Tank capacity: {capacity:.1f} litres")
    print(f"Current water level: {level_percent:.1f}%")
    print(f"Water available: {volume:.1f} litres")
    print(f"Status: {status}")
    print(pump_action)

    if level_percent < 100:
        print(f"Estimated time to fill completely: {refill_time:.2f} hours")
    else:
        print("Tank is already full.")


def show_history():
    """Print all recorded water-level readings."""
    if not level_history:
        print("No readings have been recorded yet.")
    else:
        print("\n--- READING HISTORY ---")
        for number, reading in enumerate(level_history, start=1):
            print(f"Reading {number}: {reading:.1f}%")


def main():
    """Run the tank monitoring menu."""
    print("=" * 45)
    print(" SMART WATER TANK MONITORING SYSTEM")
    print("=" * 45)
    print("Note: This program is a simulation, not a real pump controller.\n")

    capacity = get_tank_capacity()

    while True:
        print("\nMENU")
        print("1. Enter a new water-level reading")
        print("2. View reading history")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            level = get_water_level(capacity)

            # Ask for pump flow rate to estimate how long a refill may take.
            while True:
                try:
                    pump_rate = float(input("Enter pump flow rate (litres per hour): "))
                    if pump_rate <= 0:
                        print("Pump flow rate must be greater than zero.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")

            level_history.append(level)
            show_reading(capacity, level, pump_rate)

            # Extra feature: warn when a sudden drop is seen between readings.
            if len(level_history) >= 2:
                previous = level_history[-2]
                drop = previous - level
                if drop >= 15:
                    print(
                        f"LEAK/UNUSUAL USAGE ALERT: level dropped by "
                        f"{drop:.1f} percentage points since the last reading."
                    )
                elif drop > 0:
                    print(f"Water level has decreased by {drop:.1f} percentage points.")
                else:
                    print("No sudden water-level drop detected.")

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Thank you for using the Smart Water Tank Monitoring System.")
            break

        else:
            print("Invalid menu option. Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()

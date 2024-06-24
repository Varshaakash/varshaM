def get_daily_water_usage():
    try:
        usage = float(input("Enter today's water usage in liters: "))
        return usage
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_daily_water_usage()

def check_for_leaks(daily_usage, daily_limit):
    if daily_usage > daily_limit * 1.5:
        return True
    return False

def provide_water_saving_tips():
    tips = [
        "Take shorter showers.",
        "Fix leaking taps and pipes.",
        "Use a broom instead of a hose to clean driveways and sidewalks.",
        "Collect rainwater for garden use.",
        "Run dishwashers and washing machines with full loads."
    ]
    return tips

def main():
    daily_limit = 150  # Set daily water usage limit in liters
    daily_usage = get_daily_water_usage()
    
    if daily_usage > daily_limit:
        print(f"Your water usage ({daily_usage} liters) is above the daily limit of {daily_limit} liters.")
    else:
        print(f"Your water usage ({daily_usage} liters) is within the daily limit of {daily_limit} liters.")
    
    if check_for_leaks(daily_usage, daily_limit):
        print("Warning: High water usage detected. Possible leak.")
    
    print("\nWater-Saving Tips:")
    for tip in provide_water_saving_tips():
        print(f"- {tip}")

if __name__ == "__main__":
    main()

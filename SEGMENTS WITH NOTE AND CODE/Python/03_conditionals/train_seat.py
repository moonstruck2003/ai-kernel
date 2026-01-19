seat_type = input("Enter seat type (sleeper, ac , general, luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - no ac, beds are available")
    case "ac": 
        print("AC - air conditioned")
    case "general":
        print("General - NO AC ")
    case "luxury":
        print("Luxury - MOST PREMIUM ")
    case _:
        print("Invalid seat type! ")

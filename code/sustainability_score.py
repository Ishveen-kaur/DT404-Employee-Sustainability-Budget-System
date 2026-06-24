# Simple sustainability score calculator

def calculate_sustainability_score(total_emissions):
    if total_emissions <= 200:
        return 90
    elif total_emissions <= 500:
        return 80
    elif total_emissions <= 800:
        return 70
    else:
        return 60

# Example employee emissions
employee_emissions = 420

score = calculate_sustainability_score(employee_emissions)

print("Employee emissions:", employee_emissions, "kg CO2e")
print("Sustainability score:", score, "/100")

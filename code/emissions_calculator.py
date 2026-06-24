# Carbon emissions factors (kg CO2e per km)

EMISSIONS_FACTORS = {
    "flight": 0.273,
    "rail": 0.03546
}

def calculate_emissions(mode, distance_km):
    factor = EMISSIONS_FACTORS[mode]
    return round(distance_km * factor, 2)

# Example journey
distance = 300

flight_emissions = calculate_emissions("flight", distance)
rail_emissions = calculate_emissions("rail", distance)

saving = round(flight_emissions - rail_emissions, 2)

print("Flight emissions:", flight_emissions, "kg CO2e")
print("Rail emissions:", rail_emissions, "kg CO2e")
print("Carbon saving:", saving, "kg CO2e")

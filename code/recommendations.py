# Sustainability recommendations engine

def recommend_travel(distance_km):

    if distance_km <= 500:
        return "Rail recommended - lower carbon option"

    else:
        return "Flight acceptable due to journey distance"


# Example trip

journey_distance = 300

recommendation = recommend_travel(journey_distance)

print("Journey distance:", journey_distance, "km")
print("Recommendation:", recommendation)

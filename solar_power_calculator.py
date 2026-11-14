def solar_power(irradiance, panel_area, efficiency):
    power = irradiance*panel_area*efficiency
    return power

def classify_power(power):
    if power < 100:
        return "low"
    elif 100<= power <= 250:
        return "moderate"
    else:
        return "high"

morning = solar_power(400, 2, 0.2)
afternoon =solar_power(900, 2, 0.2) 
evening = solar_power(200, 2, 0.2)

print("Morning power:", morning, "W", classify_power(morning))
print("Afternoon power:", afternoon, "W", classify_power(afternoon))
print("Evening power:", evening, "W", classify_power(evening))


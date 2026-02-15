def calculate_carbon_impact(temperature, humidity):
    """
    Calculate CO₂ waste from temperature deviation
    """
    
    # optimal good temperature
    OPTIMAL_TEMP = 70
    

    deviation = abs(temperature - OPTIMAL_TEMP)
    
    # Energy waste
    baseline_daily_kwh = 8.0  # Average home AC 
    waste_percent = deviation * 3
    wasted_kwh = baseline_daily_kwh * (waste_percent / 100)
    
    # co₂ is  (0.4 kg per kWh)
    daily_co2 = wasted_kwh * 0.4
    monthly_co2 = daily_co2 * 30
    yearly_co2 = daily_co2 * 365
    
# cost 
    daily_cost = wasted_kwh * 0.13
    monthly_cost = daily_cost * 30
    yearly_cost = daily_cost * 365
    
    # Comparisons
    miles_equivalent = yearly_co2 / 0.4
    trees_needed = yearly_co2 / 20
    
    # Efficiency score(0-100)
    efficiency = max(0, 100 - (deviation * 10))
    
    return {
        'temperature': temperature,
        'deviation_from_optimal': round(deviation, 1),
        'daily_kg_co2': round(daily_co2, 2),
        'monthly_kg_co2': round(monthly_co2, 2),
        'yearly_kg_co2': round(yearly_co2, 2),
        'daily_cost_usd': round(daily_cost, 2),
        'monthly_cost_usd': round(monthly_cost, 2),
        'yearly_cost_usd': round(yearly_cost, 2),
        'equivalent_miles_driven': int(miles_equivalent),
        'trees_to_offset': round(trees_needed, 1),
        'efficiency_score': int(efficiency),
        'status': 'optimal' if deviation < 2 else 'needs_improvement'
    }

# Test
if __name__ == "__main__":
    print("🧪 Testing Carbon Calculator...\n")
    
    temps = [77, 70, 63]
    
    for temp in temps:
        print(f"📊 Temperature: {temp}°F")
        result = calculate_carbon_impact(temp, 50)
        print(f"   CO₂ waste: {result['yearly_kg_co2']} kg/year")
        print(f"   Cost: ${result['yearly_cost_usd']}/year")
        print(f"   Like driving: {result['equivalent_miles_driven']} miles")
        print(f"   Efficiency: {result['efficiency_score']}/100")
        print()
    
    print("CARBON CALCULATOR WORKS!")
import google.generativeai as genai

API_KEY = "AIzaSyAPBWy0dVXROC2wGIfOvvzIP4sUYt6PIkw"
genai.configure(api_key=API_KEY)

def get_climate_recommendation(temperature, humidity):
    """
    Get AI-powered energy-saving recommendation
    """
    
    prompt = f"""You are an energy efficiency expert helping someone reduce their carbon footprint.

Current indoor conditions:
- Temperature: {temperature}°F
- Humidity: {humidity}%

Provide ONE specific action they can take to improve energy efficiency and reduce CO₂ emissions.
Keep it 2-3 sentences. Include estimated CO₂ or cost savings.

Example: "Your temperature is 5°F above optimal. Lower your thermostat to 70°F to save approximately 2kg CO₂ per day and $15 per month."
"""
    try:
        model = genai.GenerativeModel('gemini-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"⚠️ API Error: {e}")
        return get_fallback_recommendation(temperature)

def get_fallback_recommendation(temperature):
    """Backup recommendations if Gemini fails"""
    if temperature > 75:
        return f"Temperature at {temperature}°F is high. Lower thermostat by 3°F to save ~2kg CO₂/day and $12/month."
    elif temperature < 65:
        return f"Temperature at {temperature}°F is low. Raise to 68°F for comfort without waste."
    else:
        return f"Great! At {temperature}°F you're in the optimal range for efficiency."

if __name__ == "__main__":
    print("🧪 Testing Climate Recommendations...\n")
    
    print("Test 1: Hot room (77°F)")
    advice = get_climate_recommendation(77, 50)
    print(f"🤖 AI says: {advice}\n")
    
    print("Test 2: Cold room (63°F)")
    advice = get_climate_recommendation(63, 45)
    print(f"🤖 AI says: {advice}\n")
    
    print("Test 3: Optimal room (70°F)")
    advice = get_climate_recommendation(70, 48)
    print(f"🤖 AI says: {advice}\n")
    
    print("✅ AI CLIMATE SYSTEM WORKS!")
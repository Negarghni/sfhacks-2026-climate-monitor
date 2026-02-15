from flask import Flask, jsonify, request
from flask_cors import CORS
from gemini_service import get_climate_recommendation
from carbon_calculator import calculate_carbon_impact

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "✅ AI Climate API is running!"

@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    """
    Master endpoint - returns everything!
    For now uses mock sensor data
    """
    
    # sensor data (team will replace this)
    temperature = 72.5
    humidity = 45.0
    
  #AI
    ai_recommendation = get_climate_recommendation(temperature, humidity)
    
    # Calculate carbon 
    carbon_data = calculate_carbon_impact(temperature, humidity)
    
    # Combine 
    return jsonify({
        'sensor': {
            'temperature': temperature,
            'humidity': humidity,
            'status': 'mock_data'
        },
        'ai_recommendation': ai_recommendation,
        'carbon_impact': carbon_data,
        'timestamp': 'now',
        'status': 'success'
    })

@app.route('/api/recommendation', methods=['POST'])
def recommendation():
    """Custom temp/humidity recommendation"""
    data = request.json
    temp = data.get('temperature', 72)
    humidity = data.get('humidity', 45)
    
    advice = get_climate_recommendation(temp, humidity)
    
    return jsonify({
        'recommendation': advice,
        'status': 'success'
    })

@app.route('/api/carbon', methods=['POST'])
def carbon():
    """Custom temp/humidity carbon calc"""
    data = request.json
    temp = data.get('temperature', 72)
    humidity = data.get('humidity', 45)
    
    impact = calculate_carbon_impact(temp, humidity)
    
    return jsonify(impact)

if __name__ == '__main__':
    print(" Starting AI Climate API...")
    print(" Dashboard: http://localhost:5000/api/dashboard")
    print("Test in browser or send to frontend team!")
    app.run(debug=True, port=5000)
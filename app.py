from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

print("✅ Hotel Backend Server Starting...")

# Test data
bookings = []

@app.route('/')
def home():
    return jsonify({"message": "🏨 Grand Azure Hotel API is running!", "status": "success"})

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy", "timestamp": "2024"})

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    try:
        data = request.get_json()
        print("📦 Booking received:", data)
        
        booking = {
            "id": len(bookings) + 1,
            "checkIn": data.get('checkIn'),
            "checkOut": data.get('checkOut'),
            "adults": data.get('adults'),
            "status": "confirmed"
        }
        
        bookings.append(booking)
        
        return jsonify({
            "success": True,
            "message": "🎉 Booking confirmed!",
            "bookingId": booking["id"]
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/bookings')
def get_bookings():
    return jsonify({"bookings": bookings})

@app.route('/api/rooms')
def get_rooms():
    return jsonify({
        "rooms": [
            {"id": "ocean-view", "name": "Ocean View Suite", "price": 450},
            {"id": "executive-penthouse", "name": "Executive Penthouse", "price": 1200},
            {"id": "garden-terrace", "name": "Garden Terrace Room", "price": 300}
        ]
    })

if __name__ == '__main__':
    print("🚀 Server starting at: http://localhost:5000")
    print("📍 Health check: http://localhost:5000/api/health")
    app.run(debug=True, port=5000)
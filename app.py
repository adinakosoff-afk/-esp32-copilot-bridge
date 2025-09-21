from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    ai_response = f"Copilot says: You said '{user_message}'"
    return jsonify({"response": ai_response})

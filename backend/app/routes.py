from flask import Blueprint, request, jsonify
from .ai_engine import generate_response
from .message_dispatcher import dispatch_message

api_bp = Blueprint('api', __name__)

@api_bp.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    client_name = data.get('name')
    message = data.get('message')
    business_info = data.get('business_info', {})

    response = generate_response(client_name, message, business_info)
    dispatch_message(client_name, response)
    
    return jsonify({"status": "sent", "response": response})

from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure the Gemini AI model
genai.configure(api_key="AIzaSyBHriM6J7IcNZKjABjzMfQ9S8WELu0ByHc")
model = genai.GenerativeModel('gemini-pro')

chat_history = []

def get_disease_info(query):
    prompt = f"""
    You are a helpful medical assistant chatbot. Provide information about the disease or condition related to "{query}".
    If the query is not about a specific disease, respond in a friendly, conversational manner.
    If it is about a disease, include information about its symptoms, causes, treatment, and prevention.
    Keep your response concise and easy to understand.
    """

    chat_history.append({"role": "user", "parts": [query]})
    
    try:
        response = model.generate_content(chat_history)
        chat_history.append({"role": "model", "parts": [response.text]})
        return response.text
    except Exception as e:
        print(f"Error fetching disease information: {e}")
        return "I'm sorry, I couldn't retrieve the information at this time. Can you try asking again?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    query = data['message']
    print(f"Received message: {query}")
    
    response = get_disease_info(query)
    print(f"Sending response: {response}")
    
    return jsonify({'message': response, 'is_bot': True})

if __name__ == '__main__':
    app.run(debug=True)
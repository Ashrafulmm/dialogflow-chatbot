from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Dialogflow Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    intent = req['queryResult']['intent']['displayName']

    if intent == "greeting":
        reply = "Hello! I'm your smart bot."
    elif intent == "about":
        reply = "I'm built using Dialogflow, Flask, and Replit!"
    else:
        reply = "I don't know how to respond to that yet."

    return jsonify({
        "fulfillmentText": reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

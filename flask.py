from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    hash_value = data.get("hash")
    amount = data.get("amount")
    routing = data.get("routing")
    account = data.get("account")

    # Validate & process transaction logic here
    return jsonify({"status": "success", "message": f"Transferred {amount} via hash {hash_value}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


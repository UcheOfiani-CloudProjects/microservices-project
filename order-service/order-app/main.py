from fastapi import FastAPI
import requests

# Create FastAPI instance for Order Service
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Order Service is running"}

# Simulated endpoint to get order status
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return {"order_id": order_id, "status": "Processing"}

# Endpoint to create an order and trigger payment
@app.post("/create-order")
def create_order():
    # Simulated order data
    order_data = {
        "order_id": 123,
        "amount": 50.0,
        "currency": "USD"
    }

    try:
        # Call payment-service running in Docker network
        response = requests.post("http://payment-service:8000/process-payment", json=order_data)
        return {
            "status": "Order created",
            "payment_response": response.json()
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

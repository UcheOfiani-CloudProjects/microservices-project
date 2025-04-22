from fastapi import FastAPI, Request

# Create FastAPI instance for Payment Service
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Payment Service is running"}

# Add additional payment-related endpoints if needed
@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    return {"payment_id": payment_id, "status": "Completed"}

@app.post("/process-payment")
async def process_payment(request: Request):
    data = await request.json()
    return {
        "status": "Payment processed",
        "received": data
    }
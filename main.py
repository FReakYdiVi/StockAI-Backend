from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import analyze_stock  # Import your existing function

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://stock-ai-frontend-dsz5.vercel.app"],  # Allow frontend URL
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],  # Allow all HTTP methods
    allow_headers=["Content-type"],  # Allow all headers
)

# Define a request model
class StockQuery(BaseModel):
    query: str

# Define a route for stock analysis
@app.post("/analyze_stock")
def analyze_stock_endpoint(stock_query: StockQuery):
    try:
        response = analyze_stock(stock_query.query)  # Call the function
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
def root():
    return {"message": "Stock Analysis API is running!"}

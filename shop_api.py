from fastapi import FastAPI, HTTPException, Depends, Request
from dotenv import load_dotenv
from utils import load_vectorstore
import os
load_dotenv()

vectorstore = load_vectorstore(vectorstore_path="./shopify_langchaintesting_vectorstore", index_name="products")
vectorstore_refunds = load_vectorstore(vectorstore_path="./shopify_langchaintesting_vectorstore", index_name="refund")

app = FastAPI()

def veryify_api_key(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="No Api Key provided in the header")
    token_str = token.split(" ")[1]
    if token_str == os.getenv("SHOPIFY_STATIC_TOKEN"):
        return token
    else:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.get("/product_search/")
async def search_products(query: str, k: int = 4, token: str = Depends(veryify_api_key)):
    try:
        results = vectorstore.similarity_search(query, k=k)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/refund/")
async def search_products(query: str, k: int = 1, token: str = Depends(veryify_api_key)):
    try:
        results = vectorstore_refunds.similarity_search(query, k=k)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
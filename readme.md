# E-Commerce Product Recommender

## Overview
This repository contains code for creating a Langchain Vectorstore based on Shopify data and deploying it as an API using FastAPI on Render.
I also provided raw_products.json for you, so you can play around with the data and explore it yourself.
Here is how you can load it:

``````
import json
import pandas as pd
with open("raw_products.json", "r") as f:
    raw_products = json.load(f)

product_df = pd.DataFrame(raw_products["products"])
``````

The shop_api also contains a refund endpoint, which will be relevant on a future video.

## Part 1: Langchain Vectorstore based on Shopify data https://www.youtube.com/watch?v=FTj3FLBamj0
- Preprocess Shopify data to create a vector store.
- Embed the title, tags, text, and description for better product recommendations.
- Save the processed data as CSV and JSON.
- Create a vector store using the Langchain JSON loader.

## Part 2: FastAPI Endpoint and Render deployment https://www.youtube.com/watch?v=9cwlDYhnF2w
- Create a backend API using FastAPI.
- Wrap the vector store in an API endpoint for product search.
- Add a verification mechanism for API requests.
- Deploy the API on Render and access it via a web link.

## Deployment with Render
1. Upload the repository to GitHub.
2. Connect the repository to Render.
3. Set the correct host and port settings.
4. Access the deployed API via the provided link.

## Author
Leon Sander


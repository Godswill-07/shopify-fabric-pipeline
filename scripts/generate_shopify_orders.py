import requests
import json
import time

# --- 1. Configuration ---
STORE_NAME = "fabric-pipeline-dev"
API_TOKEN = "YOUR_TOKEN_HERE"
LIMIT_PER_PAGE = 250
TOTAL_ORDERS_NEEDED = 1000

API_VERSION = "2024-04"
url = f"https://{STORE_NAME}.myshopify.com/admin/api/{API_VERSION}/orders.json?limit={LIMIT_PER_PAGE}&status=any"

headers = {
    "X-Shopify-Access-Token": API_TOKEN,
    "Content-Type": "application/json"
}

all_orders = []
page_count = 1

print(f"🚀 Starting retrieval of up to {TOTAL_ORDERS_NEEDED} orders from Shopify...")

# --- 2. The Fetch Loop ---
while url and len(all_orders) < TOTAL_ORDERS_NEEDED:
    print(f"Fetching page {page_count}...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 429:
        print("Rate limit reached. Waiting 5 seconds...")
        time.sleep(5)
        continue
    elif response.status_code != 200:
        print(f"❌ Connection failed: {response.status_code} - {response.text}")
        break

    data = response.json()
    orders = data.get("orders", [])
    
    if not orders and page_count == 1:
        print("⚠️ Warning: Shopify returned 0 orders on the very first page.")
        break
        
    all_orders.extend(orders)
    
    if len(all_orders) >= TOTAL_ORDERS_NEEDED:
        all_orders = all_orders[:TOTAL_ORDERS_NEEDED]
        break

    # Pagination handling
    link_header = response.headers.get("Link")
    if link_header and 'rel="next"' in link_header:
        links = link_header.split(",")
        next_link = [link for link in links if 'rel="next"' in link][0]
        url = next_link.split(";")[0].strip("< >")
        page_count += 1
    else:
        url = None

# --- 3. The Spark & Delta Processing ---
# --- 3. The Spark & Delta Processing ---
# --- 3. The Spark & Delta Processing ---
# --- 3. The Spark & Delta Processing ---
print("\n--- Processing Data for Lakehouse ---")
if len(all_orders) > 0:
    print(f" Found {len(all_orders)} orders. Converting to clean JSON format...")
    
    # 1. Turn the list of Python dictionaries into a list of JSON strings
    json_strings = [json.dumps(order) for order in all_orders]
    
    # 2. Parallelize the strings into an RDD
    rdd_strings = spark.sparkContext.parallelize(json_strings)
    
    # 3. Read via Spark's robust JSON reader
    df = spark.read.json(rdd_strings)

    # 4. FIX: Add .option("overwriteSchema", "true") to drop the old corrupt schema format
    df.write.format("delta") \
            .mode("overwrite") \
            .option("overwriteSchema", "true") \
            .saveAsTable("orders_bronze")
    
    print("SUCCESS! Your 'orders_bronze' Delta table is officially populated and saved.")
    
    # Let's peek at the table to celebrate!
    display(spark.sql("SELECT id, name, total_price, created_at FROM orders_bronze LIMIT 5"))
else:
    print(" Process Stopped: 0 orders were retrieved.")

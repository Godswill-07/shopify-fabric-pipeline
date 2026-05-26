# 🚀 Shopify to Microsoft Fabric Data Pipeline

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Platform](https://img.shields.io/badge/Platform-Microsoft%20Fabric-blue)
![Language](https://img.shields.io/badge/Language-Python-green)

## 📌 Project Overview
An end-to-end cloud data engineering pipeline that ingests 
real e-commerce data from the Shopify REST API into 
Microsoft Fabric using the Medallion Architecture.

## 🏗️ Architecture

## ✅ Project Status

| Layer | Status |
|---|---|
| Landing Layer | ✅ Complete |
| Bronze Layer | ✅ Complete |
| Silver Layer | 🔜 Coming Soon |
| Gold Layer | 🔜 Coming Soon |
| Power BI Dashboard | 🔜 Coming Soon |

## 🛠️ Tools & Technologies

- **Microsoft Fabric** — Lakehouse, Data Factory, Notebooks
- **Apache Spark / PySpark** — Data processing
- **Shopify REST API** — Data source
- **Delta Lake** — Storage format
- **Python** — Scripting
- **Medallion Architecture** — Design pattern

## 📂 Repository Structure

shopify-fabric-pipeline/
├── README.md
├── scripts/
│   └── generate_shopify_orders.py
├── notebooks/
│   └── orders_bronze.ipynb
└── pipeline/
└── PL_Shopify_Landing.json

## 🚀 What I Built

1. Connected to Shopify REST API using a custom app and access token
2. Built a Data Factory Pipeline with pagination to ingest 1000+ orders
3. Designed a Lakehouse Landing Layer with proper folder structure
4. Processed nested JSON data using Apache Spark in Fabric Notebooks
5. Saved clean data as a Delta Table ready for SQL queries and Power BI

## ⚙️ How to Run This Project

1. Create a Shopify Partner account at partners.shopify.com
2. Create a development store and generate sample data
3. Create a custom app and get your Admin API access token
4. Set up a Microsoft Fabric workspace and Lakehouse
5. Run the order generation script:
```bash
pip install requests
python scripts/generate_shopify_orders.py
```
6. Configure the Data Factory Pipeline with your store details
7. Run the pipeline and verify data lands in the Lakehouse



## 👤 Author
Godswill Douglas— Data Engineering Portfolio Project

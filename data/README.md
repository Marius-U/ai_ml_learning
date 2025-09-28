# Data Directory

This directory contains sample datasets and data sources for the ML training.

## 📁 Directory Contents

### **Generated Data**
- Sample datasets are created automatically when running the notebooks
- SQLite databases for real-world data integration examples
- Synthetic customer, transaction, and product data

### **External Data Sources**
The training notebooks demonstrate how to connect to:
- **Databases**: SQLite examples with customer and transaction tables
- **APIs**: Public REST API integration examples
- **Web Scraping**: Simulated e-commerce product data
- **File Formats**: CSV, JSON, Excel, and Parquet examples

## 🎯 Data Overview

### **Customer Dataset**
- **Size**: 1,000 customers
- **Features**: Demographics, behavior, ratings
- **Use Case**: Classification and regression examples
- **Missing Data**: Realistic patterns for preprocessing practice

### **Transaction Dataset**
- **Size**: Variable (generated per session)
- **Features**: Amount, date, category, customer link
- **Use Case**: Time series and aggregation examples
- **Relationships**: Linked to customer data via foreign keys

### **Product Dataset**
- **Size**: Configurable (default 50-100 products)
- **Features**: Pricing, ratings, inventory, categories
- **Use Case**: Web scraping and data quality examples
- **Missing Data**: Simulated missing ratings and prices

## 🛠️ Data Generation

All datasets are generated programmatically to ensure:
- **Reproducibility**: Same data across different runs
- **Realism**: Realistic distributions and relationships
- **Educational Value**: Demonstrates common data challenges
- **Privacy**: No real customer or business data

## 📊 Data Quality

The synthetic datasets include realistic issues:
- **Missing Values**: 5-30% missing in various columns
- **Outliers**: Extreme values in spending and income
- **Inconsistencies**: Varied data types and formats
- **Relationships**: Realistic correlations between features

## 🔄 Refreshing Data

To generate new datasets:
```python
# Run the data generation cells in the notebooks
# Data will be automatically created with different random patterns
```

## 📋 Data Schema

### Customer Table
```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    registration_date DATE,
    country TEXT,
    subscription_tier TEXT
);
```

### Transaction Table
```sql
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    transaction_date DATETIME,
    product_category TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);
```

## 🚨 Important Notes

- **No Real Data**: All data is synthetic and safe for learning
- **Temporary Files**: Some data files are created temporarily during notebook execution
- **Size Limits**: Datasets are kept small for educational purposes
- **Local Only**: Data generation happens locally, no external dependencies required
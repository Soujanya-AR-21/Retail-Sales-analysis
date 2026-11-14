# 📊 Retail Sales Analysis

An end-to-end data analytics project using **Python, SQL, and Power BI** to analyze retail sales performance, profitability, customer segments, product categories, and regional trends.

## 📌 Project Overview

This project analyzes the Sample Superstore dataset containing 9,994 retail sales records. The objective is to transform raw sales data into meaningful business insights through data cleaning, exploratory data analysis, SQL queries, and interactive Power BI visualizations.

The project demonstrates a complete data analytics workflow, from raw data processing to business intelligence reporting.

## 🎯 Project Objectives

- Analyze overall retail sales and profitability.
- Identify top-performing products and categories.
- Evaluate regional and customer segment performance.
- Understand monthly sales trends.
- Identify loss-making products and business opportunities.
- Build an interactive dashboard for business decision-making.

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data cleaning and exploratory analysis |
| Pandas | Data manipulation and processing |
| NumPy | Numerical operations |
| MySQL | SQL-based data analysis |
| Power BI | Interactive dashboard and reporting |
| DAX | KPI calculations and measures |
| Microsoft Excel | Data inspection and validation |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
retail-analysis/
│
├── data/
│   ├── raw/
│   │   └── Sample - Superstore.csv
│   │
│   └── processed/
│       ├── category_analysis.csv
│       ├── category_sales.png
│       ├── customer_analysis.csv
│       ├── data_quality_report.pdf
│       ├── loss_making_products.csv
│       ├── missing_values_report.csv
│       ├── monthly_analysis.csv
│       ├── monthly_sales_trend.png
│       ├── product_analysis.csv
│       ├── records_for_review.csv
│       ├── region_analysis.csv
│       ├── regional_sales.png
│       ├── subcategory_analysis.csv
│       ├── subcategory_profit.png
│       └── superstore_clean.csv
│
├── python/
│   ├── clean_data.py
│   └── exploratory_analysis.py
│
├── sql/
│   └── retail_analysis.sql
│
├── powerbi/
│   └── Retail_Analysis_Dashboard.pbix
│
├── presentation/
│   └── Retail_Executive_Presentation.pptx
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔄 Project Workflow

### 1. Data Cleaning – Python

- Loaded the raw Sample Superstore dataset.
- Checked missing values and duplicate records.
- Performed data validation and cleaning.
- Generated a cleaned dataset.
- Created data quality and missing-value reports.

### 2. Exploratory Data Analysis – Python

- Analyzed sales and profit distributions.
- Examined category and regional performance.
- Identified sales trends and patterns.
- Generated visualizations to understand business performance.

### 3. Data Analysis – SQL

Used MySQL to perform:

- Total sales and profit analysis.
- Category and subcategory analysis.
- Regional performance analysis.
- Monthly sales trend analysis.
- Top customers and products analysis.
- Loss-making product identification.
- Customer segment analysis.

### 4. Dashboard Development – Power BI

Created an interactive dashboard featuring:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Profit Margin
- Sales by Category
- Profit by Region
- Monthly Sales Trend
- Top 5 Products by Sales
- Interactive filters for Order Date, Category, Region, and Segment.

### 5. Executive Presentation

Prepared an executive presentation summarizing the project objectives, analysis approach, key findings, and business recommendations.

## 📈 Key Business Questions

- Which product categories generate the highest sales?
- Which regions contribute the most profit?
- How do sales change over time?
- Which products generate the highest revenue?
- Which products contribute to business losses?
- Which customer segments perform best?

## 📊 Dataset Information

- **Dataset:** Sample Superstore
- **Total Records:** 9,994
- **Total Columns:** 21
- **Data Type:** Retail Sales Data

The dataset contains information about orders, customers, products, sales, discounts, quantities, and profits.

## 💡 Skills Demonstrated

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- SQL Query Writing
- Data Modeling and KPI Development
- DAX Measures
- Interactive Dashboard Development
- Data Visualization
- Business and Sales Analysis
- Insight Generation and Reporting

## 🚀 How to Run the Project

### Prerequisites

Install the following tools:

- Python 3.x
- MySQL
- Power BI Desktop
- Visual Studio Code (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/soujanya-AR-21/retail-analysis.git
```

### Step 2: Navigate to the Project Folder

```bash
cd retail-analysis
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```
### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Data Cleaning

```bash
python python/clean_data.py
```

### Step 6: Run Exploratory Data Analysis

```bash
python python/exploratory_analysis.py
```

### Step 7: Run SQL Analysis

Import the dataset into MySQL and execute the queries available in:

```text
sql/retail_analysis.sql
```

### Step 8: Open the Power BI Dashboard

Open:

```text
powerbi/Retail_Analysis_Dashboard.pbix
```

Use Power BI Desktop to explore the interactive dashboard.

## 👩‍💻 Author

**Soujanya A R**

BCA Graduate | Aspiring Data Analyst

- **GitHub:** [soujanya-AR-21](https://github.com/soujanya-AR-21)
- **LinkedIn:** [Soujanya A R](https://linkedin.com/in/soujanya-a-r/)

---

⭐ If you find this project useful, feel free to explore the repository!



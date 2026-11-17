import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

CLEAN_FILE = (
    BASE_DIR / "data" / "processed" / "superstore_clean.csv"
)

OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 2. LOAD CLEAN DATASET
# --------------------------------------------------

if not CLEAN_FILE.exists():
    raise FileNotFoundError(f"Clean dataset not found: {CLEAN_FILE}" )

df = pd.read_csv(CLEAN_FILE)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

print("\n========== RETAIL EXPLORATORY DATA ANALYSIS ==========")

print("\nDATASET OVERVIEW")
print("Total records:", len(df))
print("Total columns:", len(df.columns))
print("Date range:", df["Order_Date"].min(), "to", df["Order_Date"].max())

# --------------------------------------------------
# 3. OVERALL BUSINESS PERFORMANCE
# --------------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()
total_products = df["Product_ID"].nunique()
total_quantity = df["Quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

print("\nOVERALL BUSINESS PERFORMANCE")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Total Products: {total_products:,}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Profit Margin: {profit_margin:.2f}%")

# --------------------------------------------------
# 4. CATEGORY PERFORMANCE
# --------------------------------------------------

category_analysis = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
)

category_analysis["Profit_Margin_Percent"] = (
    category_analysis["Total_Profit"]
    / category_analysis["Total_Sales"] * 100
)

category_analysis = category_analysis.sort_values(
    "Total_Sales",
    ascending=False
)

print("\nCATEGORY PERFORMANCE")
print(category_analysis.round(2).to_string(index=False))

category_analysis.to_csv(
    OUTPUT_DIR / "category_analysis.csv",
    index=False
)

# --------------------------------------------------
# 5. SUB-CATEGORY PERFORMANCE
# --------------------------------------------------

subcategory_analysis = (
    df.groupby("Sub_Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
    .sort_values("Total_Profit", ascending=False)
)

print("\nTOP 10 SUB-CATEGORIES BY PROFIT")
print(subcategory_analysis.head(10).round(2).to_string(index=False))

subcategory_analysis.to_csv(
    OUTPUT_DIR / "subcategory_analysis.csv",
    index=False
)

# --------------------------------------------------
# 6. MONTHLY SALES AND PROFIT TRENDS
# --------------------------------------------------

df["Order_Month"] = (
    df["Order_Date"].dt.to_period("M").astype(str)
)

monthly_analysis = (
    df.groupby("Order_Month")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order_ID", "nunique")
    )
    .reset_index()
)

print("\nMONTHLY SALES AND PROFIT")
print(monthly_analysis.to_string(index=False))

monthly_analysis.to_csv(
    OUTPUT_DIR / "monthly_analysis.csv",
    index=False
)

# --------------------------------------------------
# 7. REGIONAL PERFORMANCE
# --------------------------------------------------

region_analysis = (
    df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order_ID", "nunique")
    )
    .reset_index()
    .sort_values("Total_Sales", ascending=False)
)

print("\nREGIONAL PERFORMANCE")
print(region_analysis.round(2).to_string(index=False))

region_analysis.to_csv(
    OUTPUT_DIR / "region_analysis.csv",
    index=False
)

# --------------------------------------------------
# 8. TOP 10 CUSTOMERS BY SALES
# --------------------------------------------------

customer_analysis = (
    df.groupby("Customer_ID")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order_ID", "nunique")
    )
    .reset_index()
    .sort_values("Total_Sales", ascending=False)
)

print("\nTOP 10 CUSTOMERS BY SALES")
print(customer_analysis.head(10).round(2).to_string(index=False))

customer_analysis.to_csv(
    OUTPUT_DIR / "customer_analysis.csv",
    index=False
)

# --------------------------------------------------
# 9. TOP 10 PRODUCTS BY SALES
# --------------------------------------------------

product_analysis = (
    df.groupby(["Product_ID", "Product_Name"])
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
    .sort_values("Total_Sales", ascending=False)
)

print("\nTOP 10 PRODUCTS BY SALES")
print(product_analysis.head(10).round(2).to_string(index=False))

product_analysis.to_csv(
    OUTPUT_DIR / "product_analysis.csv",
    index=False
)

# --------------------------------------------------
# 10. LOSS-MAKING PRODUCTS
# --------------------------------------------------

loss_products = product_analysis[
    product_analysis["Total_Profit"] < 0
].sort_values("Total_Profit")

print("\nTOP 10 LOSS-MAKING PRODUCTS")
print(loss_products.head(10).round(2).to_string(index=False))

loss_products.to_csv(
    OUTPUT_DIR / "loss_making_products.csv",
    index=False
)

# --------------------------------------------------
# 11. VISUALIZATION SETTINGS
# --------------------------------------------------

sns.set_theme(style="whitegrid")

# --------------------------------------------------
# 12. CATEGORY SALES CHART
# --------------------------------------------------

plt.figure(figsize=(9, 5))

sns.barplot(
    data=category_analysis,
    x="Category",
    y="Total_Sales",
    color=sns.color_palette("deep")[0]
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "category_sales.png",
    dpi=300
)

plt.show()
plt.close()

# --------------------------------------------------
# 13. MONTHLY SALES TREND
# --------------------------------------------------

plt.figure(figsize=(12, 5))

sns.lineplot(
    data=monthly_analysis,
    x="Order_Month",
    y="Total_Sales",
    marker="o",
    color=sns.color_palette("deep")[2]
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_sales_trend.png",
    dpi=300
)

plt.show()
plt.close()

# --------------------------------------------------
# 14. REGIONAL SALES CHART
# --------------------------------------------------

plt.figure(figsize=(9, 5))

sns.barplot(
    data=region_analysis,
    x="Region",
    y="Total_Sales",
    color=sns.color_palette("deep")[1]
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "regional_sales.png",
    dpi=300
)

plt.show()
plt.close()

# --------------------------------------------------
# 15. PROFIT BY SUB-CATEGORY
# --------------------------------------------------

profit_chart = subcategory_analysis.sort_values(
    "Total_Profit",
    ascending=True
)

plt.figure(figsize=(11, 8))

sns.barplot(
    data=profit_chart,
    x="Total_Profit",
    y="Sub_Category",
    color=sns.color_palette("deep")[0]
)

plt.title("Profit by Sub-Category")
plt.xlabel("Profit ($)")
plt.ylabel("Sub-Category")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "subcategory_profit.png",
    dpi=300
)

plt.show()
plt.close()

# --------------------------------------------------
# 16. FINAL SUMMARY
# --------------------------------------------------

print("\n========== EDA COMPLETED ==========")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Profit Margin:", round(profit_margin, 2), "%")

print("\nAnalysis files saved in:")
print(OUTPUT_DIR)

print("\nEXPLORATORY DATA ANALYSIS COMPLETED SUCCESSFULLY")

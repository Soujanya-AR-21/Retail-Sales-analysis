import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "Sample - Superstore.csv"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

CLEAN_FILE = PROCESSED_DIR / "superstore_clean.csv"
MISSING_REPORT = PROCESSED_DIR / "missing_values_report.csv"
REVIEW_REPORT = PROCESSED_DIR / "records_for_review.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 2. LOAD RAW DATASET
# --------------------------------------------------

if not RAW_FILE.exists():
    raise FileNotFoundError(f"Dataset not found: {RAW_FILE}")

df = pd.read_csv(RAW_FILE, encoding="latin1")

original_rows = len(df)

# Add original source row number for tracking
df.insert(
    0,
    "Source_Row_Number",
    range(2, len(df) + 2)
)

print("\n========== RETAIL DATA CLEANING ==========")
print("Original records:", original_rows)

# --------------------------------------------------
# 3. STANDARDIZE COLUMN NAMES
# --------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_", regex=False)
    .str.replace("-", "_", regex=False)
)

# --------------------------------------------------
# 4. CLEAN TEXT COLUMNS
# --------------------------------------------------

text_columns = df.select_dtypes(
    include=["object", "string"]
).columns

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

# --------------------------------------------------
# 5. REMOVE EXACT DUPLICATES
# --------------------------------------------------

duplicate_mask = df.drop(
    columns=["Source_Row_Number"]
).duplicated(keep="first")

duplicates_removed = int(duplicate_mask.sum())

df = df.loc[~duplicate_mask].copy()

print("Duplicate records removed:", duplicates_removed)

# --------------------------------------------------
# 6. CONVERT DATE COLUMNS
# --------------------------------------------------

date_columns = ["Order_Date", "Ship_Date"]

for column in date_columns:
    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column],
            format="%m/%d/%Y",
            errors="coerce"
        )

# --------------------------------------------------
# 7. CONVERT NUMERIC COLUMNS
# --------------------------------------------------

numeric_columns = [
    "Row_ID",
    "Postal_Code",
    "Sales",
    "Quantity",
    "Discount",
    "Profit"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

# --------------------------------------------------
# 8. IDENTIFY RECORDS FOR REVIEW
# --------------------------------------------------

review_reasons = pd.Series( "",
    index=df.index,
    dtype="object"
)

# Missing values
missing_mask = df.isnull().any(axis=1)

review_reasons.loc[missing_mask] += "Missing values; "

# Invalid dates
for column in date_columns:
    if column in df.columns:
        invalid_dates = df[column].isna()

        review_reasons.loc[invalid_dates] += (
            f"Invalid or missing {column}; "
        )

# Invalid numeric values
for column in numeric_columns:
    if column in df.columns:
        invalid_numeric = df[column].isna()

        review_reasons.loc[invalid_numeric] += (
            f"Invalid or missing {column}; "
        )

# Negative sales
if "Sales" in df.columns:
    negative_sales = df["Sales"] < 0

    review_reasons.loc[negative_sales] += (
        "Negative sales; "
    )

# Zero or negative quantity
if "Quantity" in df.columns:
    invalid_quantity = df["Quantity"] <= 0

    review_reasons.loc[invalid_quantity] += (
        "Non-positive quantity; "
    )

# Discount outside the valid range
if "Discount" in df.columns:
    invalid_discount = (
        (df["Discount"] < 0) |
        (df["Discount"] > 1)
    )

    review_reasons.loc[invalid_discount] += (
        "Discount outside 0 to 1; "
    )

# Missing important identifiers
key_columns = [
    "Order_ID",
    "Customer_ID",
    "Product_ID"
]

for column in key_columns:
    if column in df.columns:
        missing_key = df[column].isna() | (
            df[column].astype("string").str.strip() == ""
        )

        review_reasons.loc[missing_key] += (
            f"Missing {column}; "
        )

# --------------------------------------------------
# 9. EXPORT RECORDS FOR REVIEW
# --------------------------------------------------

review_mask = review_reasons.ne("")

records_for_review = df.loc[review_mask].copy()

records_for_review["Review_Reason"] = (
    review_reasons.loc[review_mask]
)

records_for_review.to_csv(
    REVIEW_REPORT,
    index=False
)

# --------------------------------------------------
# 10. CREATE CLEAN MASTER DATASET
# --------------------------------------------------

essential_columns = [
    "Order_ID",
    "Order_Date",
    "Ship_Date",
    "Customer_ID",
    "Product_ID",
    "Sales",
    "Quantity",
    "Discount",
    "Profit"
]

available_essential = [
    column for column in essential_columns
    if column in df.columns
]

clean_df = df.dropna(
    subset=available_essential
).copy()

# Remove records with invalid business values
if "Sales" in clean_df.columns:
    clean_df = clean_df[
        clean_df["Sales"] >= 0
    ]

if "Quantity" in clean_df.columns:
    clean_df = clean_df[
        clean_df["Quantity"] > 0
    ]

if "Discount" in clean_df.columns:
    clean_df = clean_df[
        (clean_df["Discount"] >= 0) &
        (clean_df["Discount"] <= 1)
    ]

# --------------------------------------------------
# 11. GENERATE MISSING VALUES REPORT
# --------------------------------------------------

missing_report = pd.DataFrame({
    "Column_Name": df.columns,
    "Missing_Count": df.isnull().sum().values,
    "Missing_Percentage": (
        df.isnull().mean().values * 100
    ).round(2)
})

missing_report.to_csv(
    MISSING_REPORT,
    index=False
)

# --------------------------------------------------
# 12. SAVE CLEAN DATASET
# --------------------------------------------------

clean_df.to_csv(
    CLEAN_FILE,
    index=False,
    date_format="%Y-%m-%d"
)

# --------------------------------------------------
# 13. FINAL SUMMARY
# --------------------------------------------------

print("\n========== CLEANING SUMMARY ==========")

print("Original records:", original_rows)
print("Duplicate records removed:", duplicates_removed)
print("Records requiring review:", len(records_for_review))
print("Final clean records:", len(clean_df))
print("Records excluded from clean dataset:", original_rows - len(clean_df))

print("\n========== FILES GENERATED ==========")

print("Clean dataset:", CLEAN_FILE)
print("Missing values report:", MISSING_REPORT)
print("Records for review:", REVIEW_REPORT)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY")

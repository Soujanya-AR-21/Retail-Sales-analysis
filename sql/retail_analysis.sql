
CREATE DATABASE IF NOT EXISTS retail_analysis;

USE retail_analysis;

CREATE TABLE orders (
    Source_Row_Number INT,
    Row_ID INT,
    Order_ID VARCHAR(30),
    Order_Date DATE,
    Ship_Date DATE,
    Ship_Mode VARCHAR(50),
    Customer_ID VARCHAR(30),
    Customer_Name VARCHAR(150),
    Segment VARCHAR(50),
    Country VARCHAR(100),
    City VARCHAR(100),
    State VARCHAR(100),
    Postal_Code VARCHAR(20),
    Region VARCHAR(50),
    Product_ID VARCHAR(50),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Product_Name VARCHAR(255),
    Sales DECIMAL(12,2),
    Quantity INT,
    Discount DECIMAL(5,2),
    Profit DECIMAL(12,2)
);


USE retail_analysis;

SELECT COUNT(*) AS total_records
FROM orders;

SELECT *
FROM orders
LIMIT 10;


USE retail_analysis;

SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    COUNT(DISTINCT Product_ID) AS Total_Products,
    SUM(Quantity) AS Total_Quantity,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Sales), 0) * 100,
        2
    ) AS Profit_Margin_Percentage
FROM orders;

SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;



SELECT
    YEAR(Order_Date) AS Sales_Year,
    MONTH(Order_Date) AS Sales_Month,
    MONTHNAME(Order_Date) AS Month_Name,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY
    YEAR(Order_Date),
    MONTH(Order_Date),
    MONTHNAME(Order_Date)
ORDER BY Sales_Year, Sales_Month;

SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM orders
GROUP BY Region
ORDER BY Total_Sales DESC;



SELECT
    YEAR(Order_Date) AS Sales_Year,
    MONTH(Order_Date) AS Sales_Month,
    MONTHNAME(Order_Date) AS Month_Name,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY
    YEAR(Order_Date),
    MONTH(Order_Date),
    MONTHNAME(Order_Date)
ORDER BY Sales_Year, Sales_Month;



SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM orders
GROUP BY Region
ORDER BY Total_Sales DESC;


SELECT
    Customer_ID,
    MAX(Customer_Name) AS Customer_Name,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Customer_ID
ORDER BY Total_Sales DESC
LIMIT 10;



SELECT
    Product_ID,
    MAX(Product_Name) AS Product_Name,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Product_ID
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT
    Product_ID,
    MAX(Product_Name) AS Product_Name,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Product_ID
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC;


SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT Customer_ID) AS Total_Customers
FROM orders
GROUP BY Segment
ORDER BY Total_Sales DESC;




-- index


USE retail_analysis;

-- Index for order date analysis
CREATE INDEX idx_order_date
ON orders(Order_Date);

-- Index for customer analysis
CREATE INDEX idx_customer_id
ON orders(Customer_ID);

-- Index for product analysis
CREATE INDEX idx_product_id
ON orders(Product_ID);

-- Index for category analysis
CREATE INDEX idx_category
ON orders(Category);

-- Index for regional analysis
CREATE INDEX idx_region
ON orders(Region);


SHOW INDEX FROM orders;


-- Total records
SELECT COUNT(*) AS Total_Records
FROM orders;

-- Check missing important values
SELECT
    SUM(Order_ID IS NULL) AS Missing_Order_ID,
    SUM(Customer_ID IS NULL) AS Missing_Customer_ID,
    SUM(Product_ID IS NULL) AS Missing_Product_ID
FROM orders;

-- Check date range
SELECT
    MIN(Order_Date) AS First_Order,
    MAX(Order_Date) AS Last_Order
FROM orders;

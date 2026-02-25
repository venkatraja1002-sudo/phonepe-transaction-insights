-- 1. Create Table
CREATE TABLE aggregated_transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

-- 2. Top 10 States
SELECT state, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;

-- 3. Year Wise Growth
SELECT year, SUM(transaction_amount)
FROM aggregated_transaction
GROUP BY year;
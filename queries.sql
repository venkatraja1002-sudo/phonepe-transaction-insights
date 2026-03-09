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

CREATE TABLE map_transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(150),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

CREATE TABLE top_transaction_pincode (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    pincode VARCHAR(20),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

-- Top performing states
SELECT state,
       SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;

-- Top performing districts
SELECT district,
       state,
       SUM(transaction_amount) AS total_amount
FROM map_transaction
GROUP BY district, state
ORDER BY total_amount DESC
LIMIT 10;

-- Top performing pincodes
SELECT pincode,
       state,
       SUM(transaction_amount) AS total_amount
FROM top_transaction_pincode
GROUP BY pincode, state
ORDER BY total_amount DESC
LIMIT 10;

-- Payment category totals
SELECT transaction_type,
       SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_amount DESC;


-- Year Wise Growth
SELECT year, SUM(transaction_amount)
FROM aggregated_transaction
GROUP BY year;

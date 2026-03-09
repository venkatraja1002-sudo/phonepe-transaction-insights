import os
import json
import mysql.connector

# =========================
# Database connection
# =========================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Venkat@123",
    database="phonepe"
)
cursor = conn.cursor()

# =========================
# Insert helpers
# =========================
def insert_aggregated(state, year, quarter, txn_type, txn_count, txn_amount):
    cursor.execute("""
        INSERT INTO aggregated_transaction
        (state, year, quarter, transaction_type, transaction_count, transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (state, year, quarter, txn_type, txn_count, txn_amount))


def insert_map(state, year, quarter, district, txn_count, txn_amount):
    cursor.execute("""
        INSERT INTO map_transaction
        (state, year, quarter, district, transaction_count, transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (state, year, quarter, district, txn_count, txn_amount))


def insert_pincode(state, year, quarter, pincode, txn_count, txn_amount):
    cursor.execute("""
        INSERT INTO top_transaction_pincode
        (state, year, quarter, pincode, transaction_count, transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (state, year, quarter, pincode, txn_count, txn_amount))


# =========================
# Paths
# =========================
aggregated_path = "data/aggregated/transaction/country/india/state/"
map_path = "data/map/transaction/hover/country/india/state/"
top_path = "data/top/transaction/country/india/state/"


# =========================
# Load aggregated transaction data
# =========================
def load_aggregated():
    if not os.path.exists(aggregated_path):
        print(f"Path not found: {aggregated_path}")
        return

    for state in os.listdir(aggregated_path):
        state_path = os.path.join(aggregated_path, state)
        if not os.path.isdir(state_path):
            continue

        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            if not os.path.isdir(year_path):
                continue

            for file in os.listdir(year_path):
                if not file.endswith(".json"):
                    continue

                quarter = file.replace(".json", "")
                file_path = os.path.join(year_path, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    transactions = data.get("data", {}).get("transactionData", [])

                    for item in transactions:
                        txn_type = item.get("name")
                        instruments = item.get("paymentInstruments", [])

                        if instruments:
                            txn_count = instruments[0].get("count", 0)
                            txn_amount = instruments[0].get("amount", 0.0)

                            insert_aggregated(
                                state=state,
                                year=int(year),
                                quarter=int(quarter),
                                txn_type=txn_type,
                                txn_count=txn_count,
                                txn_amount=txn_amount
                            )
                except Exception as e:
                    print(f"Aggregated load failed: {file_path} -> {e}")


# =========================
# Load district-level map transaction data
# =========================
def load_map():
    if not os.path.exists(map_path):
        print(f"Path not found: {map_path}")
        return

    for state in os.listdir(map_path):
        state_path = os.path.join(map_path, state)
        if not os.path.isdir(state_path):
            continue

        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            if not os.path.isdir(year_path):
                continue

            for file in os.listdir(year_path):
                if not file.endswith(".json"):
                    continue

                quarter = file.replace(".json", "")
                file_path = os.path.join(year_path, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    hover_list = data.get("data", {}).get("hoverDataList", [])

                    for item in hover_list:
                        district = item.get("name")
                        metric = item.get("metric", [])

                        if metric:
                            txn_count = metric[0].get("count", 0)
                            txn_amount = metric[0].get("amount", 0.0)

                            insert_map(
                                state=state,
                                year=int(year),
                                quarter=int(quarter),
                                district=district,
                                txn_count=txn_count,
                                txn_amount=txn_amount
                            )
                except Exception as e:
                    print(f"Map load failed: {file_path} -> {e}")


# =========================
# Load pincode-level top transaction data
# =========================
def load_top_pincode():
    if not os.path.exists(top_path):
        print(f"Path not found: {top_path}")
        return

    for state in os.listdir(top_path):
        state_path = os.path.join(top_path, state)
        if not os.path.isdir(state_path):
            continue

        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            if not os.path.isdir(year_path):
                continue

            for file in os.listdir(year_path):
                if not file.endswith(".json"):
                    continue

                quarter = file.replace(".json", "")
                file_path = os.path.join(year_path, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    pincodes = data.get("data", {}).get("pincodes", [])

                    for item in pincodes:
                        pincode = item.get("name") or item.get("entityName")
                        metric = item.get("metric", {})

                        if isinstance(metric, list) and len(metric) > 0:
                            txn_count = metric[0].get("count", 0)
                            txn_amount = metric[0].get("amount", 0.0)
                        else:
                            txn_count = metric.get("count", 0)
                            txn_amount = metric.get("amount", 0.0)

                        insert_pincode(
                            state=state,
                            year=int(year),
                            quarter=int(quarter),
                            pincode=str(pincode),
                            txn_count=txn_count,
                            txn_amount=txn_amount
                        )
                except Exception as e:
                    print(f"Top pincode load failed: {file_path} -> {e}")


# =========================
# Run all loaders
# =========================
if __name__ == "__main__":
    print("Loading aggregated transaction data...")
    load_aggregated()

    print("Loading district map transaction data...")
    load_map()

    print("Loading top pincode transaction data...")
    load_top_pincode()

    conn.commit()
    cursor.close()
    conn.close()

    print("All data loaded successfully.")
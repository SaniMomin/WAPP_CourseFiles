# -----------------------
# 1. Integration Section
# -----------------------
import csv
import json

def read_csv(filename):
    with open(filename, newline='') as f:
        return {row['product_id']: row for row in csv.DictReader(f)}

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def merge_data(csv_data, json_data):
    merged = []
    for pid, row in csv_data.items():
        merged_row = {**row, **json_data.get(pid, {})}
        merged.append(merged_row)
    return merged

# -----------------------------
# 2. Data Transformation Section
# -----------------------------
def export_to_csv(data, filename):
    with open(filename, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# -----------------------
# 3. Error Handling Section
# -----------------------
def handle_errors(csv_data, json_data):
    for pid in csv_data:
        if pid not in json_data:
            print(f"Warning: Product ID {pid} missing in JSON")

# -----------------------
# 4. Data Validation Section
# -----------------------
def validate_data(data):
    for item in data:
        if not item.get('product_id'):
            print("Invalid record: Missing product_id")
        try:
            if float(item.get('price', 0)) <= 0:
                print(f"Invalid price for product_id {item['product_id']}")
        except ValueError:
            print(f"Non-numeric price for product_id {item['product_id']}")

# -----------------------
# Main Script
# -----------------------
if __name__ == "__main__":
    csv_data = read_csv("products.csv")
    json_data = read_json("products.json")
    
    handle_errors(csv_data, json_data)
    merged = merge_data(csv_data, json_data)
    validate_data(merged)
    export_to_csv(merged, "merged_output.csv")
    print("✅ Data merged and exported successfully.")

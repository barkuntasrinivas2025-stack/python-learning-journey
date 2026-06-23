csv_data = """alice ,  24,  Hyderabad
  BOB , 30 ,Secunderabad
charlie,  28, Cyber City"""

rows = csv_data.split("\n")
print(rows)

cleaned_csv_rows = []

for row in rows:
    items = row.split(",")
    name = items[0].strip().upper()
    age = items[1].strip()
    city = items[2].strip()

    clean_row = ",".join([name,age,city])

    cleaned_csv_rows.append(clean_row)



final_clean_csv = "\n".join(cleaned_csv_rows)

print("Original Messy String:\n", csv_data)
print("\n" + "="*30 + "\n")
print("Cleaned CSV Output:\n", final_clean_csv)

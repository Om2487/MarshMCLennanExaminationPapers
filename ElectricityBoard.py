num = int(input("Enter the number of connection records to be added:\n"))
electricity_map = {}

print("Enter the connection records (ConnectionId:Connectiontype):")
for _ in range(num):
    record = input()
    conn_id, conn_type = record.split(":")
    electricity_map[conn_id.strip()] = conn_type.strip()

search_type = input("Enter the Connection type to be searched:\n")
count = 0
for conn_type in electricity_map.values():
    if conn_type.lower() == search_type.lower():
        count += 1

if count == 0:
    print(f"No Connection Ids were found for {search_type}")
else:
    print(f"The count of connection Ids based on {search_type.upper()} are {count}")


search_type2 = input("Enter the Connection type to identify the Connection Ids:\n")
matched_ids = []
for conn_id, conn_type in electricity_map.items():
    if conn_type.lower() == search_type2.lower():
        matched_ids.append(conn_id)

if not matched_ids:
    print(f"No Connection Ids were found for the {search_type2}")
else:
    print(f"Connection Ids based on the {search_type2.upper()} are")
    for conn_id in matched_ids:
        print(conn_id)

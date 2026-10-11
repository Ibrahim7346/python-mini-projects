rules = []

while True:
    print("\n--- Firewall Menu ---")
    print("1. Block IP")
    print("2. View Rules")
    print("3. check IP")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        ip = input ("Enter IP to block: ")
        rules.append(ip)
        print(f"{ip} blocked.")

    elif choice == "2":
        print("\nBlocked IPs:")
        for rule in rules:
            print(rule)

    elif choice == "3":
        ip = input("Enter IP to check: ")

        if ip in rules:
            print("Access Denied")
        else:
            print("Access Allowed")

    elif choice == "4":
        break

    else:
        print("Invalid option")

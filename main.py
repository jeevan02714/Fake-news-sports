import csv

FILE = "news_data.csv"

trusted_sources = ["espn", "bbc", "cricbuzz"]

def view_news():
    print("\n--- All News ---")
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def verify_news():
    title = input("Enter news title: ")
    source = input("Enter source: ").lower()

    if source in trusted_sources:
        status = "Verified"
    elif source == "unknown":
        status = "Fake"
    else:
        status = "Partially Verified"

    print(f"Status: {status}")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, source, "Checked manually", status])

def search_news():
    keyword = input("Enter keyword: ").lower()

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if keyword in row[0].lower():
                print(row)

def menu():
    while True:
        print("\n--- Fake News Detection System ---")
        print("1. View News")
        print("2. Verify News")
        print("3. Search News")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_news()
        elif choice == "2":
            verify_news()
        elif choice == "3":
            search_news()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()

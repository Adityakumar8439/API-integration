import requests

# -------------------------------
# Function to fetch data from API
# -------------------------------
def fetch_data():
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)

        # Check if request is successful
        if response.status_code == 200:
            data = response.json()  # Convert JSON to Python list
            print("Data fetched successfully\n")
            return data
        else:
            print("Failed to fetch data. Status Code:", response.status_code)
            return []

    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        return []

# -------------------------------
# Function to display all posts
# -------------------------------
def show_all_posts(data):
    for post in data[:5]:  # show only first 5 posts
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print("-" * 40)

# -------------------------------
# Function to search post by keyword
# -------------------------------
def search_posts(data, keyword):
    found = False
    for post in data:
        if keyword.lower() in post['title'].lower():
            print(f"\n Found Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
            print("-" * 40)
            found = True

    if not found:
        print("No matching posts found")

# -------------------------------
# Function to filter posts by userId
# -------------------------------
def filter_by_user(data, user_id):
    filtered = [post for post in data if post['userId'] == user_id]

    if filtered:
        for post in filtered:
            print(f"\nUser {user_id} Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print("-" * 40)
    else:
        print("No posts found for this user")

# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    data = fetch_data()

    if not data:
        print("No data available. Exiting...")
        return

    while True:
        print("\nMENU")
        print("1. Show All Posts")
        print("2. Search Post by Keyword")
        print("3. Filter by User ID")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_posts(data)

        elif choice == '2':
            keyword = input("Enter keyword to search: ")
            search_posts(data, keyword)

        elif choice == '3':
            try:
                user_id = int(input("Enter User ID (1-10): "))
                filter_by_user(data, user_id)
            except ValueError:
                print("Please enter a valid number")

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again!")

# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()
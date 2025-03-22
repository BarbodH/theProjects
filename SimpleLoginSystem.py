import hashlib
import os

# File to store user credentials
USER_FILE = "users.txt"

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register():
    username = input("Enter a new username: ").strip()
    password = input("Enter a new password: ").strip()

    # Check if user already exists
    if user_exists(username):
        print("❌ Username already taken. Try again.")
        return
    
    # Hash the password and save to file
    hashed_password = hash_password(password)
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{hashed_password}\n")
    
    print("✅ Registration successful!")

# Function to check if a username exists
def user_exists(username):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(",")
            if stored_username == username:
                return True
    return False

# Function to login
def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    hashed_password = hash_password(password)

    if not os.path.exists(USER_FILE):
        print("❌ No users registered yet.")
        return

    with open(USER_FILE, "r") as file:
        for line in file:
            stored_username, stored_hashed_password = line.strip().split(",")
            if stored_username == username and stored_hashed_password == hashed_password:
                print("✅ Login successful!")
                return

    print("❌ Invalid username or password.")

# Main menu
while True:
    print("\n1️⃣ Register\n2️⃣ Login\n3️⃣ Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
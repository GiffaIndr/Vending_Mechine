import json 
import os

AUTH_FILE = 'data/users.json'

def load_users():
    if not os.path.exists(AUTH_FILE):
        return {}
    with open(AUTH_FILE, 'r') as file:
        return json.load(file)
    
def save_users(data):
    with open(AUTH_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def register():
    users = load_users()
    username = input("Username: ")
    if username in users:
        print("Username sudah terdaftar.")
        return None
    password = input("password: ")
    role = input("Role (admin/user): ").lower()
    if role not in ['admin', 'user']:
        print("Role tidak valid.")
        return None
    users[username] = {
        'password': password,
        'role': role
    }
    save_users(users)
    print(f"User '{username}' dengan role '{role}' berhasil terdaftar.")
    return username, role

def login():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")
    user = users.get(username)
    if user and user['password'] == password:
        print(f"Login berhasil sebagai {username} ({user['role']})")
        return username, user['role']
    else:
        print("Username atau password salah.")
        return None
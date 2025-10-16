"""
Password Hashing Utility
This script hashes plain text passwords in the users.csv file
Run this ONCE before starting the application
"""

import pandas as pd
from werkzeug.security import generate_password_hash
import os


def hash_user_passwords():
    """
    Read users.csv, hash all plain text passwords, and save back to file.
    Creates a backup of the original file.
    """
    users_file = 'data/users.csv'
    backup_file = 'data/users_backup.csv'
    
    # Check if file exists
    if not os.path.exists(users_file):
        print(f"Error: {users_file} not found!")
        return
    
    # Load the users data
    print("Loading users data...")
    users_df = pd.read_csv(users_file)
    
    # Create backup
    print(f"Creating backup at {backup_file}...")
    users_df.to_csv(backup_file, index=False)
    
    # Hash passwords
    print("Hashing passwords...")
    hashed_passwords = []
    
    for index, row in users_df.iterrows():
        plain_password = str(row['PasswordHash'])  # Current plain text password
        hashed_password = generate_password_hash(plain_password)
        hashed_passwords.append(hashed_password)
        print(f"  - User: {row['Username']} | Password hashed successfully")
    
    # Update the dataframe
    users_df['PasswordHash'] = hashed_passwords
    
    # Save back to file
    print(f"Saving hashed passwords to {users_file}...")
    users_df.to_csv(users_file, index=False)
    
    print("\n✅ Password hashing complete!")
    print(f"✅ Backup saved at: {backup_file}")
    print(f"✅ Updated file saved at: {users_file}")
    print("\n📋 User credentials (for testing):")
    print("-" * 50)
    
    # Read the backup to show original passwords
    backup_df = pd.read_csv(backup_file)
    for index, row in backup_df.iterrows():
        print(f"Username: {row['Username']} | Password: {row['PasswordHash']}")
    
    print("-" * 50)
    print("\n⚠️  Keep the backup file safe and delete it after testing!")


if __name__ == '__main__':
    print("=" * 50)
    print("PASSWORD HASHING UTILITY")
    print("=" * 50)
    print("\nThis script will:")
    print("1. Create a backup of users.csv")
    print("2. Hash all plain text passwords")
    print("3. Update users.csv with hashed passwords")
    print("\n" + "=" * 50)
    
    response = input("\nDo you want to continue? (yes/no): ").lower()
    
    if response in ['yes', 'y']:
        hash_user_passwords()
    else:
        print("Operation cancelled.")
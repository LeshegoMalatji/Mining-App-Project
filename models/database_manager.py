"""
Database Manager Module
Handles all CSV file operations for the mining application
"""

import pandas as pd
import os
from werkzeug.security import generate_password_hash, check_password_hash


class DatabaseManager:
    """
    Manages all database operations for CSV files.
    Provides methods to read, write, and query data from CSV files.
    """
    
    def __init__(self, data_folder='data'):
        """
        Initialize the DatabaseManager with the path to the data folder.
        
        Args:
            data_folder (str): Path to the folder containing CSV files
        """
        self.data_folder = data_folder
        self.users_file = os.path.join(data_folder, 'users.csv')
        self.roles_file = os.path.join(data_folder, 'roles.csv')
        self.countries_file = os.path.join(data_folder, 'countries.csv')
        self.minerals_file = os.path.join(data_folder, 'minerals.csv')
        self.production_stats_file = os.path.join(data_folder, 'production_stats.csv')
        self.sites_file = os.path.join(data_folder, 'sites.csv')
    
    def load_users(self):
        """
        Load all users from the users CSV file.
        
        Returns:
            DataFrame: Pandas DataFrame containing user data
        """
        try:
            return pd.read_csv(self.users_file)
        except FileNotFoundError:
            print(f"Error: {self.users_file} not found.")
            return pd.DataFrame()
    
    def load_roles(self):
        """
        Load all roles from the roles CSV file.
        
        Returns:
            DataFrame: Pandas DataFrame containing role data
        """
        try:
            return pd.read_csv(self.roles_file)
        except FileNotFoundError:
            print(f"Error: {self.roles_file} not found.")
            return pd.DataFrame()
    
    def load_countries(self):
        """
        Load all countries from the countries CSV file.
        
        Returns:
            DataFrame: Pandas DataFrame containing country data
        """
        try:
            return pd.read_csv(self.countries_file)
        except FileNotFoundError:
            print(f"Error: {self.countries_file} not found.")
            return pd.DataFrame()
    
    def load_minerals(self):
        """
        Load all minerals from the minerals CSV file.
        
        Returns:
            DataFrame: Pandas DataFrame containing mineral data
        """
        try:
            return pd.read_csv(self.minerals_file)
        except FileNotFoundError:
            print(f"Error: {self.minerals_file} not found.")
            return pd.DataFrame()
    
    def load_production_stats(self):
        """
        Load all production statistics from the production_stats CSV file.
        
        Returns:
            DataFrame: Pandas DataFrame containing production statistics
        """
        try:
            return pd.read_csv(self.production_stats_file)
        except FileNotFoundError:
            print(f"Error: {self.production_stats_file} not found.")
            return pd.DataFrame()
    
    def load_sites(self):
        """
        Load all mining sites from the sites CSV file.
        
        Returns:
            DataFrame: Pandas DataFrame containing site data
        """
        try:
            return pd.read_csv(self.sites_file)
        except FileNotFoundError:
            print(f"Error: {self.sites_file} not found.")
            return pd.DataFrame()
    
    def get_user_by_username(self, username):
        """
        Retrieve a specific user by username.
        
        Args:
            username (str): The username to search for
            
        Returns:
            Series or None: User data if found, None otherwise
        """
        users_df = self.load_users()
        user = users_df[users_df['Username'] == username]
        
        if not user.empty:
            return user.iloc[0]
        return None
    
    def verify_password(self, stored_hash, provided_password):
        """
        Verify a password against its hash.
        
        Args:
            stored_hash (str): The stored password hash
            provided_password (str): The password to verify
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return check_password_hash(stored_hash, provided_password)
    
    def hash_password(self, password):
        """
        Generate a hash for a password.
        
        Args:
            password (str): The password to hash
            
        Returns:
            str: The hashed password
        """
        return generate_password_hash(password)
    
    def get_role_by_id(self, role_id):
        """
        Retrieve a specific role by its ID.
        
        Args:
            role_id (int): The role ID to search for
            
        Returns:
            Series or None: Role data if found, None otherwise
        """
        roles_df = self.load_roles()
        role = roles_df[roles_df['RoleID'] == role_id]
        
        if not role.empty:
            return role.iloc[0]
        return None
    
    def get_country_by_id(self, country_id):
        """
        Retrieve a specific country by its ID.
        
        Args:
            country_id (int): The country ID to search for
            
        Returns:
            Series or None: Country data if found, None otherwise
        """
        countries_df = self.load_countries()
        country = countries_df[countries_df['CountryID'] == country_id]
        
        if not country.empty:
            return country.iloc[0]
        return None
    
    def get_mineral_by_id(self, mineral_id):
        """
        Retrieve a specific mineral by its ID.
        
        Args:
            mineral_id (int): The mineral ID to search for
            
        Returns:
            Series or None: Mineral data if found, None otherwise
        """
        minerals_df = self.load_minerals()
        mineral = minerals_df[minerals_df['MineralID'] == mineral_id]
        
        if not mineral.empty:
            return mineral.iloc[0]
        return None
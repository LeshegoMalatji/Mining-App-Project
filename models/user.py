"""
User Model Module
Represents a user in the mining application system
"""


class User:
    """
    Represents a user with authentication and role information.
    """
    
    def __init__(self, user_id, username, password_hash, role_id, email):
        """
        Initialize a User object.
        
        Args:
            user_id (int): Unique identifier for the user
            username (str): Username for login
            password_hash (str): Hashed password
            role_id (int): ID of the user's role
            email (str): User's email address
        """
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.role_id = role_id
        self.email = email
    
    def get_id(self):
        """
        Get the user's ID.
        
        Returns:
            int: User ID
        """
        return self.user_id
    
    def get_username(self):
        """
        Get the username.
        
        Returns:
            str: Username
        """
        return self.username
    
    def get_role_id(self):
        """
        Get the user's role ID.
        
        Returns:
            int: Role ID
        """
        return self.role_id
    
    def get_email(self):
        """
        Get the user's email.
        
        Returns:
            str: Email address
        """
        return self.email
    
    def to_dict(self):
        """
        Convert user object to dictionary.
        
        Returns:
            dict: Dictionary representation of the user
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'role_id': self.role_id,
            'email': self.email
        }
    
    def __repr__(self):
        """
        String representation of the User object.
        
        Returns:
            str: User representation
        """
        return f"User(id={self.user_id}, username='{self.username}', role_id={self.role_id})"
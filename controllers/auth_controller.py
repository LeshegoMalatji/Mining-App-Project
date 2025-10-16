"""
Authentication Controller Module
Handles user authentication, login, logout, and session management
"""

from models.database_manager import DatabaseManager
from models.user import User
from models.role import Role


class AuthController:
    """
    Controller for handling authentication operations.
    """
    
    def __init__(self):
        """
        Initialize the AuthController with a DatabaseManager instance.
        """
        self.db_manager = DatabaseManager()
    
    def authenticate_user(self, username, password):
        """
        Authenticate a user with username and password.
        
        Args:
            username (str): The username provided
            password (str): The password provided
            
        Returns:
            User or None: User object if authentication successful, None otherwise
        """
        # Get user from database
        user_data = self.db_manager.get_user_by_username(username)
        
        if user_data is None:
            return None
        
        # Verify password
        if self.db_manager.verify_password(user_data['PasswordHash'], password):
            # Create and return User object
            user = User(
                user_id=user_data['UserID'],
                username=user_data['Username'],
                password_hash=user_data['PasswordHash'],
                role_id=user_data['RoleID'],
                email=user_data['Email']
            )
            return user
        
        return None
    
    def get_user_role(self, role_id):
        """
        Get the role information for a given role ID.
        
        Args:
            role_id (int): The role ID
            
        Returns:
            Role or None: Role object if found, None otherwise
        """
        role_data = self.db_manager.get_role_by_id(role_id)
        
        if role_data is None:
            return None
        
        # Create and return Role object
        role = Role(
            role_id=role_data['RoleID'],
            role_name=role_data['RoleName'],
            permissions=role_data['Permissions']
        )
        return role
    
    def validate_session(self, session_data):
        """
        Validate if a user session is valid.
        
        Args:
            session_data (dict): Session data containing user information
            
        Returns:
            bool: True if session is valid, False otherwise
        """
        if not session_data:
            return False
        
        # Check if required session keys exist
        required_keys = ['user_id', 'username', 'role_id']
        for key in required_keys:
            if key not in session_data:
                return False
        
        return True
    
    def check_permission(self, role_id, required_permission):
        """
        Check if a role has a specific permission.
        
        Args:
            role_id (int): The role ID to check
            required_permission (str): The permission required
            
        Returns:
            bool: True if role has permission, False otherwise
        """
        role = self.get_user_role(role_id)
        
        if role is None:
            return False
        
        return role.has_permission(required_permission)
    
    def get_all_users(self):
        """
        Get all users from the database (Admin only function).
        
        Returns:
            list: List of User objects
        """
        users_df = self.db_manager.load_users()
        users_list = []
        
        for _, user_data in users_df.iterrows():
            user = User(
                user_id=user_data['UserID'],
                username=user_data['Username'],
                password_hash=user_data['PasswordHash'],
                role_id=user_data['RoleID'],
                email=user_data['Email']
            )
            users_list.append(user)
        
        return users_list
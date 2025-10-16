"""
Role Model Module
Represents a user role with associated permissions
"""


class Role:
    """
    Represents a role in the system with specific permissions.
    """
    
    def __init__(self, role_id, role_name, permissions):
        """
        Initialize a Role object.
        
        Args:
            role_id (int): Unique identifier for the role
            role_name (str): Name of the role (e.g., Administrator, Investor)
            permissions (str): Comma-separated permissions for the role
        """
        self.role_id = role_id
        self.role_name = role_name
        self.permissions = permissions
    
    def get_id(self):
        """
        Get the role's ID.
        
        Returns:
            int: Role ID
        """
        return self.role_id
    
    def get_name(self):
        """
        Get the role name.
        
        Returns:
            str: Role name
        """
        return self.role_name
    
    def get_permissions(self):
        """
        Get the role's permissions.
        
        Returns:
            str: Permissions string
        """
        return self.permissions
    
    def get_permissions_list(self):
        """
        Get permissions as a list.
        
        Returns:
            list: List of individual permissions
        """
        if self.permissions:
            return [p.strip() for p in self.permissions.split(',')]
        return []
    
    def has_permission(self, permission):
        """
        Check if the role has a specific permission.
        
        Args:
            permission (str): Permission to check
            
        Returns:
            bool: True if role has the permission, False otherwise
        """
        permissions_list = self.get_permissions_list()
        return permission in permissions_list
    
    def to_dict(self):
        """
        Convert role object to dictionary.
        
        Returns:
            dict: Dictionary representation of the role
        """
        return {
            'role_id': self.role_id,
            'role_name': self.role_name,
            'permissions': self.permissions
        }
    
    def __repr__(self):
        """
        String representation of the Role object.
        
        Returns:
            str: Role representation
        """
        return f"Role(id={self.role_id}, name='{self.role_name}')"
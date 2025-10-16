"""
Mineral Model Module
Represents a critical mineral with market information
"""


class Mineral:
    """
    Represents a critical mineral with description and market price.
    """
    
    def __init__(self, mineral_id, mineral_name, description, market_price_usd_per_tonne):
        """
        Initialize a Mineral object.
        
        Args:
            mineral_id (int): Unique identifier for the mineral
            mineral_name (str): Name of the mineral
            description (str): Description of the mineral
            market_price_usd_per_tonne (float): Current market price in USD per tonne
        """
        self.mineral_id = mineral_id
        self.mineral_name = mineral_name
        self.description = description
        self.market_price_usd_per_tonne = market_price_usd_per_tonne
    
    def get_id(self):
        """
        Get the mineral's ID.
        
        Returns:
            int: Mineral ID
        """
        return self.mineral_id
    
    def get_name(self):
        """
        Get the mineral name.
        
        Returns:
            str: Mineral name
        """
        return self.mineral_name
    
    def get_description(self):
        """
        Get the mineral description.
        
        Returns:
            str: Mineral description
        """
        return self.description
    
    def get_market_price(self):
        """
        Get the current market price.
        
        Returns:
            float: Market price in USD per tonne
        """
        return self.market_price_usd_per_tonne
    
    def get_formatted_price(self):
        """
        Get formatted market price with currency symbol.
        
        Returns:
            str: Formatted price string
        """
        return f"${self.market_price_usd_per_tonne:,.2f} per tonne"
    
    def to_dict(self):
        """
        Convert mineral object to dictionary.
        
        Returns:
            dict: Dictionary representation of the mineral
        """
        return {
            'mineral_id': self.mineral_id,
            'mineral_name': self.mineral_name,
            'description': self.description,
            'market_price_usd_per_tonne': self.market_price_usd_per_tonne
        }
    
    def __repr__(self):
        """
        String representation of the Mineral object.
        
        Returns:
            str: Mineral representation
        """
        return f"Mineral(id={self.mineral_id}, name='{self.mineral_name}', price=${self.market_price_usd_per_tonne}/tonne)"
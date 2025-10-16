"""
Country Model Module
Represents a mineral-producing country with economic data
"""


class Country:
    """
    Represents a country with GDP, mining revenue, and key projects information.
    """
    
    def __init__(self, country_id, country_name, gdp_billion_usd, mining_revenue_billion_usd, key_projects):
        """
        Initialize a Country object.
        
        Args:
            country_id (int): Unique identifier for the country
            country_name (str): Name of the country
            gdp_billion_usd (float): GDP in billions USD
            mining_revenue_billion_usd (float): Mining revenue in billions USD
            key_projects (str): Description of key mining projects
        """
        self.country_id = country_id
        self.country_name = country_name
        self.gdp_billion_usd = gdp_billion_usd
        self.mining_revenue_billion_usd = mining_revenue_billion_usd
        self.key_projects = key_projects
    
    def get_id(self):
        """
        Get the country's ID.
        
        Returns:
            int: Country ID
        """
        return self.country_id
    
    def get_name(self):
        """
        Get the country name.
        
        Returns:
            str: Country name
        """
        return self.country_name
    
    def get_gdp(self):
        """
        Get the country's GDP.
        
        Returns:
            float: GDP in billions USD
        """
        return self.gdp_billion_usd
    
    def get_mining_revenue(self):
        """
        Get the mining revenue.
        
        Returns:
            float: Mining revenue in billions USD
        """
        return self.mining_revenue_billion_usd
    
    def get_mining_contribution_percentage(self):
        """
        Calculate mining's contribution to GDP as a percentage.
        
        Returns:
            float: Percentage of GDP from mining
        """
        if self.gdp_billion_usd > 0:
            return (self.mining_revenue_billion_usd / self.gdp_billion_usd) * 100
        return 0.0
    
    def get_key_projects(self):
        """
        Get key mining projects.
        
        Returns:
            str: Key projects description
        """
        return self.key_projects
    
    def to_dict(self):
        """
        Convert country object to dictionary.
        
        Returns:
            dict: Dictionary representation of the country
        """
        return {
            'country_id': self.country_id,
            'country_name': self.country_name,
            'gdp_billion_usd': self.gdp_billion_usd,
            'mining_revenue_billion_usd': self.mining_revenue_billion_usd,
            'key_projects': self.key_projects,
            'mining_contribution_pct': self.get_mining_contribution_percentage()
        }
    
    def __repr__(self):
        """
        String representation of the Country object.
        
        Returns:
            str: Country representation
        """
        return f"Country(id={self.country_id}, name='{self.country_name}', GDP=${self.gdp_billion_usd}B)"
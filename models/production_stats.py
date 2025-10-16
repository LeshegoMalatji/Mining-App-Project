"""
Production Statistics Model Module
Represents production statistics for a specific mineral in a country for a given year
"""


class ProductionStats:
    """
    Represents production statistics linking country, mineral, year, and export data.
    """
    
    def __init__(self, stat_id, year, country_id, mineral_id, production_tonnes, export_value_billion_usd):
        """
        Initialize a ProductionStats object.
        
        Args:
            stat_id (int): Unique identifier for the statistic
            year (int): Year of production
            country_id (int): ID of the producing country
            mineral_id (int): ID of the mineral produced
            production_tonnes (int): Production volume in tonnes
            export_value_billion_usd (float): Export value in billions USD
        """
        self.stat_id = stat_id
        self.year = year
        self.country_id = country_id
        self.mineral_id = mineral_id
        self.production_tonnes = production_tonnes
        self.export_value_billion_usd = export_value_billion_usd
    
    def get_id(self):
        """
        Get the statistic's ID.
        
        Returns:
            int: Stat ID
        """
        return self.stat_id
    
    def get_year(self):
        """
        Get the production year.
        
        Returns:
            int: Year
        """
        return self.year
    
    def get_country_id(self):
        """
        Get the country ID.
        
        Returns:
            int: Country ID
        """
        return self.country_id
    
    def get_mineral_id(self):
        """
        Get the mineral ID.
        
        Returns:
            int: Mineral ID
        """
        return self.mineral_id
    
    def get_production(self):
        """
        Get the production volume.
        
        Returns:
            int: Production in tonnes
        """
        return self.production_tonnes
    
    def get_export_value(self):
        """
        Get the export value.
        
        Returns:
            float: Export value in billions USD
        """
        return self.export_value_billion_usd
    
    def get_average_price_per_tonne(self):
        """
        Calculate average price per tonne based on export value and production.
        
        Returns:
            float: Average price per tonne in USD
        """
        if self.production_tonnes > 0:
            # Convert billion USD to USD and divide by tonnes
            return (self.export_value_billion_usd * 1_000_000_000) / self.production_tonnes
        return 0.0
    
    def to_dict(self):
        """
        Convert production stats object to dictionary.
        
        Returns:
            dict: Dictionary representation of the production statistics
        """
        return {
            'stat_id': self.stat_id,
            'year': self.year,
            'country_id': self.country_id,
            'mineral_id': self.mineral_id,
            'production_tonnes': self.production_tonnes,
            'export_value_billion_usd': self.export_value_billion_usd,
            'avg_price_per_tonne': self.get_average_price_per_tonne()
        }
    
    def __repr__(self):
        """
        String representation of the ProductionStats object.
        
        Returns:
            str: ProductionStats representation
        """
        return f"ProductionStats(year={self.year}, country_id={self.country_id}, mineral_id={self.mineral_id}, production={self.production_tonnes}t)"
"""
Site Model Module
Represents a mining site with geographical location
"""


class Site:
    """
    Represents a mining site with location and production information.
    """
    
    def __init__(self, site_id, site_name, country_id, mineral_id, latitude, longitude, production_tonnes):
        """
        Initialize a Site object.
        
        Args:
            site_id (int): Unique identifier for the site
            site_name (str): Name of the mining site
            country_id (int): ID of the country where site is located
            mineral_id (int): ID of the mineral extracted
            latitude (float): Latitude coordinate
            longitude (float): Longitude coordinate
            production_tonnes (int): Annual production in tonnes
        """
        self.site_id = site_id
        self.site_name = site_name
        self.country_id = country_id
        self.mineral_id = mineral_id
        self.latitude = latitude
        self.longitude = longitude
        self.production_tonnes = production_tonnes
    
    def get_id(self):
        """
        Get the site's ID.
        
        Returns:
            int: Site ID
        """
        return self.site_id
    
    def get_name(self):
        """
        Get the site name.
        
        Returns:
            str: Site name
        """
        return self.site_name
    
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
    
    def get_coordinates(self):
        """
        Get the geographical coordinates.
        
        Returns:
            tuple: (latitude, longitude)
        """
        return (self.latitude, self.longitude)
    
    def get_latitude(self):
        """
        Get the latitude.
        
        Returns:
            float: Latitude
        """
        return self.latitude
    
    def get_longitude(self):
        """
        Get the longitude.
        
        Returns:
            float: Longitude
        """
        return self.longitude
    
    def get_production(self):
        """
        Get the production volume.
        
        Returns:
            int: Production in tonnes
        """
        return self.production_tonnes
    
    def to_dict(self):
        """
        Convert site object to dictionary.
        
        Returns:
            dict: Dictionary representation of the site
        """
        return {
            'site_id': self.site_id,
            'site_name': self.site_name,
            'country_id': self.country_id,
            'mineral_id': self.mineral_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'production_tonnes': self.production_tonnes
        }
    
    def __repr__(self):
        """
        String representation of the Site object.
        
        Returns:
            str: Site representation
        """
        return f"Site(id={self.site_id}, name='{self.site_name}', coords=({self.latitude}, {self.longitude}))"
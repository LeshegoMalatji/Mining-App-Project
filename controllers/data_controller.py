"""
Data Controller Module
Handles all data operations for minerals, countries, production stats, and sites
"""

from models.database_manager import DatabaseManager
from models.country import Country
from models.mineral import Mineral
from models.production_stats import ProductionStats
from models.site import Site
import pandas as pd


class DataController:
    """
    Controller for managing data operations across all entities.
    """
    
    def __init__(self):
        """
        Initialize the DataController with a DatabaseManager instance.
        """
        self.db_manager = DatabaseManager()
    
    # ==================== Country Operations ====================
    
    def get_all_countries(self):
        """
        Get all countries from the database.
        
        Returns:
            list: List of Country objects
        """
        countries_df = self.db_manager.load_countries()
        countries_list = []
        
        for _, country_data in countries_df.iterrows():
            country = Country(
                country_id=country_data['CountryID'],
                country_name=country_data['CountryName'],
                gdp_billion_usd=country_data['GDP_BillionUSD'],
                mining_revenue_billion_usd=country_data['MiningRevenue_BillionUSD'],
                key_projects=country_data['KeyProjects']
            )
            countries_list.append(country)
        
        return countries_list
    
    def get_country_by_id(self, country_id):
        """
        Get a specific country by ID.
        
        Args:
            country_id (int): The country ID
            
        Returns:
            Country or None: Country object if found, None otherwise
        """
        country_data = self.db_manager.get_country_by_id(country_id)
        
        if country_data is None:
            return None
        
        country = Country(
            country_id=country_data['CountryID'],
            country_name=country_data['CountryName'],
            gdp_billion_usd=country_data['GDP_BillionUSD'],
            mining_revenue_billion_usd=country_data['MiningRevenue_BillionUSD'],
            key_projects=country_data['KeyProjects']
        )
        return country
    
    def get_country_by_name(self, country_name):
        """
        Get a country by name.
        
        Args:
            country_name (str): The country name
            
        Returns:
            Country or None: Country object if found, None otherwise
        """
        countries_df = self.db_manager.load_countries()
        country_data = countries_df[countries_df['CountryName'] == country_name]
        
        if country_data.empty:
            return None
        
        country_data = country_data.iloc[0]
        country = Country(
            country_id=country_data['CountryID'],
            country_name=country_data['CountryName'],
            gdp_billion_usd=country_data['GDP_BillionUSD'],
            mining_revenue_billion_usd=country_data['MiningRevenue_BillionUSD'],
            key_projects=country_data['KeyProjects']
        )
        return country
    
    # ==================== Mineral Operations ====================
    
    def get_all_minerals(self):
        """
        Get all minerals from the database.
        
        Returns:
            list: List of Mineral objects
        """
        minerals_df = self.db_manager.load_minerals()
        minerals_list = []
        
        for _, mineral_data in minerals_df.iterrows():
            mineral = Mineral(
                mineral_id=mineral_data['MineralID'],
                mineral_name=mineral_data['MineralName'],
                description=mineral_data['Description'],
                market_price_usd_per_tonne=mineral_data['MarketPriceUSD_per_tonne']
            )
            minerals_list.append(mineral)
        
        return minerals_list
    
    def get_mineral_by_id(self, mineral_id):
        """
        Get a specific mineral by ID.
        
        Args:
            mineral_id (int): The mineral ID
            
        Returns:
            Mineral or None: Mineral object if found, None otherwise
        """
        mineral_data = self.db_manager.get_mineral_by_id(mineral_id)
        
        if mineral_data is None:
            return None
        
        mineral = Mineral(
            mineral_id=mineral_data['MineralID'],
            mineral_name=mineral_data['MineralName'],
            description=mineral_data['Description'],
            market_price_usd_per_tonne=mineral_data['MarketPriceUSD_per_tonne']
        )
        return mineral
    
    # ==================== Production Statistics Operations ====================
    
    def get_all_production_stats(self):
        """
        Get all production statistics from the database.
        
        Returns:
            list: List of ProductionStats objects
        """
        stats_df = self.db_manager.load_production_stats()
        stats_list = []
        
        for _, stat_data in stats_df.iterrows():
            stat = ProductionStats(
                stat_id=stat_data['StatID'],
                year=stat_data['Year'],
                country_id=stat_data['CountryID'],
                mineral_id=stat_data['MineralID'],
                production_tonnes=stat_data['Production_tonnes'],
                export_value_billion_usd=stat_data['ExportValue_BillionUSD']
            )
            stats_list.append(stat)
        
        return stats_list
    
    def get_production_by_country(self, country_id):
        """
        Get production statistics for a specific country.
        
        Args:
            country_id (int): The country ID
            
        Returns:
            list: List of ProductionStats objects for the country
        """
        stats_df = self.db_manager.load_production_stats()
        country_stats = stats_df[stats_df['CountryID'] == country_id]
        stats_list = []
        
        for _, stat_data in country_stats.iterrows():
            stat = ProductionStats(
                stat_id=stat_data['StatID'],
                year=stat_data['Year'],
                country_id=stat_data['CountryID'],
                mineral_id=stat_data['MineralID'],
                production_tonnes=stat_data['Production_tonnes'],
                export_value_billion_usd=stat_data['ExportValue_BillionUSD']
            )
            stats_list.append(stat)
        
        return stats_list
    
    def get_production_by_mineral(self, mineral_id):
        """
        Get production statistics for a specific mineral.
        
        Args:
            mineral_id (int): The mineral ID
            
        Returns:
            list: List of ProductionStats objects for the mineral
        """
        stats_df = self.db_manager.load_production_stats()
        mineral_stats = stats_df[stats_df['MineralID'] == mineral_id]
        stats_list = []
        
        for _, stat_data in mineral_stats.iterrows():
            stat = ProductionStats(
                stat_id=stat_data['StatID'],
                year=stat_data['Year'],
                country_id=stat_data['CountryID'],
                mineral_id=stat_data['MineralID'],
                production_tonnes=stat_data['Production_tonnes'],
                export_value_billion_usd=stat_data['ExportValue_BillionUSD']
            )
            stats_list.append(stat)
        
        return stats_list
    
    # ==================== Site Operations ====================
    
    def get_all_sites(self):
        """
        Get all mining sites from the database.
        
        Returns:
            list: List of Site objects
        """
        sites_df = self.db_manager.load_sites()
        sites_list = []
        
        for _, site_data in sites_df.iterrows():
            site = Site(
                site_id=site_data['SiteID'],
                site_name=site_data['SiteName'],
                country_id=site_data['CountryID'],
                mineral_id=site_data['MineralID'],
                latitude=site_data['Latitude'],
                longitude=site_data['Longitude'],
                production_tonnes=site_data['Production_tonnes']
            )
            sites_list.append(site)
        
        return sites_list
    
    def get_sites_by_country(self, country_id):
        """
        Get all mining sites for a specific country.
        
        Args:
            country_id (int): The country ID
            
        Returns:
            list: List of Site objects in the country
        """
        sites_df = self.db_manager.load_sites()
        country_sites = sites_df[sites_df['CountryID'] == country_id]
        sites_list = []
        
        for _, site_data in country_sites.iterrows():
            site = Site(
                site_id=site_data['SiteID'],
                site_name=site_data['SiteName'],
                country_id=site_data['CountryID'],
                mineral_id=site_data['MineralID'],
                latitude=site_data['Latitude'],
                longitude=site_data['Longitude'],
                production_tonnes=site_data['Production_tonnes']
            )
            sites_list.append(site)
        
        return sites_list
    
    def get_sites_by_mineral(self, mineral_id):
        """
        Get all mining sites for a specific mineral.
        
        Args:
            mineral_id (int): The mineral ID
            
        Returns:
            list: List of Site objects producing the mineral
        """
        sites_df = self.db_manager.load_sites()
        mineral_sites = sites_df[sites_df['MineralID'] == mineral_id]
        sites_list = []
        
        for _, site_data in mineral_sites.iterrows():
            site = Site(
                site_id=site_data['SiteID'],
                site_name=site_data['SiteName'],
                country_id=site_data['CountryID'],
                mineral_id=site_data['MineralID'],
                latitude=site_data['Latitude'],
                longitude=site_data['Longitude'],
                production_tonnes=site_data['Production_tonnes']
            )
            sites_list.append(site)
        
        return sites_list
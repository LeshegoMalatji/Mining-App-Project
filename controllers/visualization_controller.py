"""
Visualization Controller Module
Handles creation of interactive charts and maps for data visualization
"""

import plotly.graph_objects as go
import plotly.express as px
import folium
from folium import plugins
import pandas as pd
from controllers.data_controller import DataController


class VisualizationController:
    """
    Controller for generating interactive visualizations using Plotly and Folium.
    """
    
    def __init__(self):
        """
        Initialize the VisualizationController with a DataController instance.
        """
        self.data_controller = DataController()
    
    # ==================== Plotly Chart Methods ====================
    
    def create_production_trend_chart(self, mineral_id=None, country_id=None):
        """
        Create a line chart showing production trends over years.
        
        Args:
            mineral_id (int, optional): Filter by specific mineral
            country_id (int, optional): Filter by specific country
            
        Returns:
            str: HTML representation of the Plotly chart
        """
        # Get production statistics
        if mineral_id:
            stats = self.data_controller.get_production_by_mineral(mineral_id)
        elif country_id:
            stats = self.data_controller.get_production_by_country(country_id)
        else:
            stats = self.data_controller.get_all_production_stats()
        
        # Prepare data
        years = [stat.get_year() for stat in stats]
        production = [stat.get_production() for stat in stats]
        
        # Create figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=production,
            mode='lines+markers',
            name='Production',
            line=dict(color='#0d6efd', width=3),
            marker=dict(size=8)
        ))
        
        # Update layout
        fig.update_layout(
            title='Production Trend Over Years',
            xaxis_title='Year',
            yaxis_title='Production (tonnes)',
            hovermode='x unified',
            template='plotly_white',
            height=400
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    def create_export_value_chart(self, mineral_id=None, country_id=None):
        """
        Create a bar chart showing export values.
        
        Args:
            mineral_id (int, optional): Filter by specific mineral
            country_id (int, optional): Filter by specific country
            
        Returns:
            str: HTML representation of the Plotly chart
        """
        # Get production statistics
        if mineral_id:
            stats = self.data_controller.get_production_by_mineral(mineral_id)
        elif country_id:
            stats = self.data_controller.get_production_by_country(country_id)
        else:
            stats = self.data_controller.get_all_production_stats()
        
        # Prepare data
        years = [stat.get_year() for stat in stats]
        export_values = [stat.get_export_value() for stat in stats]
        
        # Create figure
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=years,
            y=export_values,
            name='Export Value',
            marker_color='#198754'
        ))
        
        # Update layout
        fig.update_layout(
            title='Export Value by Year',
            xaxis_title='Year',
            yaxis_title='Export Value (Billion USD)',
            template='plotly_white',
            height=400
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    def create_mineral_price_comparison_chart(self):
        """
        Create a bar chart comparing market prices of different minerals.
        
        Returns:
            str: HTML representation of the Plotly chart
        """
        # Get all minerals
        minerals = self.data_controller.get_all_minerals()
        
        # Prepare data
        mineral_names = [mineral.get_name() for mineral in minerals]
        prices = [mineral.get_market_price() for mineral in minerals]
        
        # Create figure
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=mineral_names,
            y=prices,
            marker_color=['#0d6efd', '#198754', '#ffc107', '#dc3545'],
            text=prices,
            texttemplate='$%{text:,.0f}',
            textposition='outside'
        ))
        
        # Update layout
        fig.update_layout(
            title='Mineral Market Price Comparison',
            xaxis_title='Mineral',
            yaxis_title='Price (USD per tonne)',
            template='plotly_white',
            height=450,
            showlegend=False
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    def create_country_gdp_chart(self):
        """
        Create a bar chart showing GDP and mining revenue for countries.
        
        Returns:
            str: HTML representation of the Plotly chart
        """
        # Get all countries
        countries = self.data_controller.get_all_countries()
        
        # Prepare data
        country_names = [country.get_name() for country in countries]
        gdp_values = [country.get_gdp() for country in countries]
        mining_revenues = [country.get_mining_revenue() for country in countries]
        
        # Create figure
        fig = go.Figure()
        
        # Add GDP bars
        fig.add_trace(go.Bar(
            name='GDP',
            x=country_names,
            y=gdp_values,
            marker_color='#0d6efd'
        ))
        
        # Add Mining Revenue bars
        fig.add_trace(go.Bar(
            name='Mining Revenue',
            x=country_names,
            y=mining_revenues,
            marker_color='#198754'
        ))
        
        # Update layout
        fig.update_layout(
            title='Country GDP vs Mining Revenue',
            xaxis_title='Country',
            yaxis_title='Value (Billion USD)',
            barmode='group',
            template='plotly_white',
            height=450,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    def create_production_by_country_pie_chart(self, mineral_id):
        """
        Create a pie chart showing production distribution by country for a mineral.
        
        Args:
            mineral_id (int): The mineral ID
            
        Returns:
            str: HTML representation of the Plotly chart
        """
        # Get production statistics for the mineral
        stats = self.data_controller.get_production_by_mineral(mineral_id)
        
        # Aggregate production by country
        country_production = {}
        for stat in stats:
            country_id = stat.get_country_id()
            if country_id not in country_production:
                country_production[country_id] = 0
            country_production[country_id] += stat.get_production()
        
        # Get country names
        countries = []
        productions = []
        for country_id, production in country_production.items():
            country = self.data_controller.get_country_by_id(country_id)
            if country:
                countries.append(country.get_name())
                productions.append(production)
        
        # Create figure
        fig = go.Figure()
        fig.add_trace(go.Pie(
            labels=countries,
            values=productions,
            hole=0.3,
            marker=dict(colors=['#0d6efd', '#198754', '#ffc107', '#dc3545'])
        ))
        
        # Update layout
        fig.update_layout(
            title='Production Distribution by Country',
            template='plotly_white',
            height=400
        )
        
        return fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    # ==================== Folium Map Methods ====================
    
    def create_mining_sites_map(self, center_lat=-28.5, center_lon=24.5, zoom_start=5):
        """
        Create an interactive map showing all mining sites.
        
        Args:
            center_lat (float): Center latitude for the map
            center_lon (float): Center longitude for the map
            zoom_start (int): Initial zoom level
            
        Returns:
            str: HTML representation of the Folium map
        """
        # Create base map
        mining_map = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=zoom_start,
            tiles='OpenStreetMap'
        )
        
        # Get all sites
        sites = self.data_controller.get_all_sites()
        
        # Add markers for each site
        for site in sites:
            # Get mineral name for popup
            mineral = self.data_controller.get_mineral_by_id(site.get_mineral_id())
            mineral_name = mineral.get_name() if mineral else "Unknown"
            
            # Get country name
            country = self.data_controller.get_country_by_id(site.get_country_id())
            country_name = country.get_name() if country else "Unknown"
            
            # Create popup content
            popup_html = f"""
            <div style="font-family: Arial; width: 200px;">
                <h5 style="color: #0d6efd; margin-bottom: 10px;">{site.get_name()}</h5>
                <p style="margin: 5px 0;"><strong>Country:</strong> {country_name}</p>
                <p style="margin: 5px 0;"><strong>Mineral:</strong> {mineral_name}</p>
                <p style="margin: 5px 0;"><strong>Production:</strong> {site.get_production():,} tonnes</p>
                <p style="margin: 5px 0;"><strong>Coordinates:</strong> ({site.get_latitude():.4f}, {site.get_longitude():.4f})</p>
            </div>
            """
            
            # Choose marker color based on production volume
            if site.get_production() > 500000:
                marker_color = 'red'
                icon = 'star'
            elif site.get_production() > 200000:
                marker_color = 'orange'
                icon = 'certificate'
            else:
                marker_color = 'blue'
                icon = 'map-marker'
            
            # Add marker
            folium.Marker(
                location=[site.get_latitude(), site.get_longitude()],
                popup=folium.Popup(popup_html, max_width=250),
                tooltip=site.get_name(),
                icon=folium.Icon(color=marker_color, icon=icon, prefix='fa')
            ).add_to(mining_map)
        
        # Add marker cluster for better visualization
        marker_cluster = plugins.MarkerCluster().add_to(mining_map)
        
        # Add layer control
        folium.LayerControl().add_to(mining_map)
        
        return mining_map._repr_html_()
    
    def create_country_sites_map(self, country_id):
        """
        Create a map showing mining sites for a specific country.
        
        Args:
            country_id (int): The country ID
            
        Returns:
            str: HTML representation of the Folium map
        """
        # Get sites for the country
        sites = self.data_controller.get_sites_by_country(country_id)
        
        if not sites:
            return "<p>No mining sites found for this country.</p>"
        
        # Calculate center of map based on sites
        avg_lat = sum(site.get_latitude() for site in sites) / len(sites)
        avg_lon = sum(site.get_longitude() for site in sites) / len(sites)
        
        # Create map
        country_map = folium.Map(
            location=[avg_lat, avg_lon],
            zoom_start=6,
            tiles='OpenStreetMap'
        )
        
        # Add markers for each site
        for site in sites:
            mineral = self.data_controller.get_mineral_by_id(site.get_mineral_id())
            mineral_name = mineral.get_name() if mineral else "Unknown"
            
            popup_html = f"""
            <div style="font-family: Arial; width: 200px;">
                <h5 style="color: #198754;">{site.get_name()}</h5>
                <p><strong>Mineral:</strong> {mineral_name}</p>
                <p><strong>Production:</strong> {site.get_production():,} tonnes</p>
            </div>
            """
            
            folium.Marker(
                location=[site.get_latitude(), site.get_longitude()],
                popup=folium.Popup(popup_html, max_width=250),
                tooltip=site.get_name(),
                icon=folium.Icon(color='green', icon='industry', prefix='fa')
            ).add_to(country_map)
        
        return country_map._repr_html_()
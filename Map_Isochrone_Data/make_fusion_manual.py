import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import imageio.v2 as imageio
import os
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Origin Coordinates (Cl Om 16)
center_point = (41.321254, 2.074613)

# Define the points from your Smappen screenshot
# Note: These are estimated based on your map visualization
manual_points = [
    {"name": "Origin (Cl Om 16)", "lat": 41.321254, "lon": 2.074613, "color": "#ff0000"}, # Red
    {"name": "Point 2 (Purple Zone)", "lat": 41.3235, "lon": 2.0830, "color": "#a020f0"}, # Purple
    {"name": "Point 3 (Blue Zone)", "lat": 41.3250, "lon": 2.0880, "color": "#0000ff"},   # Blue
    {"name": "Point 4 (Orange Zone)", "lat": 41.3180, "lon": 2.0850, "color": "#ffa500"}  # Orange
]

def create_fusion_animation(mode="walking", travel_speed=75, trip_times=range(1, 31, 2)):
    print(f"--- Starting Manual Fusion Animation ({mode}) ---")
    
    # 1. Create GeoDataFrame from manual points
    df = pd.DataFrame(manual_points)
    geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
    gdf_poi = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
    
    # 2. Download Network
    max_dist = max(trip_times) * travel_speed
    print(f"Downloading {mode} network...")
    G = ox.graph_from_point(center_point, dist=max_dist, network_type="walk" if mode=="walking" else "drive")
    G_proj = ox.project_graph(G)
    center_node = ox.distance.nearest_nodes(G, X=center_point[1], Y=center_point[0])
    
    # Project POIs to match map
    gdf_poi = gdf_poi.to_crs(G_proj.graph['crs'])

    # 3. Calculate Time Weights
    for u, v, k, data in G_proj.edges(data=True, keys=True):
        data['time'] = data['length'] / travel_speed
        
    os.makedirs(f"frames_fusion", exist_ok=True)
    frames = []
    
    # 4. Generate Frames
    for i, t in enumerate(trip_times):
        subgraph_nodes = nx.ego_graph(G_proj, center_node, radius=t, distance='time').nodes()
        
        nc = ['#00ffff' if node in subgraph_nodes else 'none' for node in G_proj.nodes()]
        ns = [15 if node in subgraph_nodes else 0 for node in G_proj.nodes()]
        
        fig, ax = ox.plot_graph(G_proj, node_color=nc, node_size=ns, edge_color='#333333', 
                                edge_linewidth=0.5, show=False, close=False, bgcolor='black', figsize=(12, 12))
        
        # Overlay the manual points from Smappen
        for _, row in gdf_poi.iterrows():
            ax.scatter(row.geometry.x, row.geometry.y, c=row['color'], s=150, edgecolors='white', linewidth=1, zorder=5)
            ax.annotate(row['name'], (row.geometry.x, row.geometry.y), color='white', fontsize=8, alpha=0.8, xytext=(5,5), textcoords='offset points')

        ax.set_title(f"Thesis Fusion: {t} min Walking\nIsochrone + Smappen Indicators", color='white', fontsize=18)
        
        filename = f"frames_fusion/frame_{i:03d}.png"
        fig.savefig(filename, facecolor='black', dpi=100, bbox_inches='tight')
        frames.append(imageio.imread(filename))
        plt.close(fig)
        
    # 5. Save GIF
    output_name = "thesis_smappen_fusion.gif"
    imageio.mimsave(output_name, frames, duration=0.4)
    print(f"Success! Saved to {output_name}")

if __name__ == "__main__":
    create_fusion_animation()

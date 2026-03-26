import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
import logging
import warnings
warnings.filterwarnings("ignore")

ox.settings.log_console=True

center_point = (41.321254, 2.074613)

def create_isochrone(mode, travel_speed, trip_times, network_type):
    print(f"Downloading {network_type} network for {mode}...")
    max_dist = max(trip_times) * travel_speed
    G = ox.graph_from_point(center_point, dist=max_dist, network_type=network_type)
    
    print(f"Finding center node...")
    center_node = ox.distance.nearest_nodes(G, X=center_point[1], Y=center_point[0])
    
    G_proj = ox.project_graph(G)
    
    for u, v, k, data in G_proj.edges(data=True, keys=True):
        data['time'] = data['length'] / travel_speed
        
    os.makedirs(f"frames_{mode}", exist_ok=True)
    frames = []
    print(f"Generating frames for {mode}...")
    
    for i, t in enumerate(trip_times):
        subgraph_nodes = nx.ego_graph(G_proj, center_node, radius=t, distance='time').nodes()
        nc = ['#00ffff' if node in subgraph_nodes else 'none' for node in G_proj.nodes()]
        ns = [15 if node in subgraph_nodes else 0 for node in G_proj.nodes()]
        
        # 降低背景街道亮度：從 #999999 改為較淡的 #333333
        fig, ax = ox.plot_graph(G_proj, node_color=nc, node_size=ns, edge_color='#333333', 
                                edge_linewidth=0.7, show=False, close=False, bgcolor='black', figsize=(10,10))
        ax.set_title(f"{mode.capitalize()} from Base - {t} minutes", color='white', fontsize=20, pad=10)
        
        filename = f"frames_{mode}/frame_{i:03d}.png"
        fig.savefig(filename, facecolor='black', dpi=150, bbox_inches='tight')
        frames.append(imageio.imread(filename))
        plt.close(fig)
        
    gif_name = f"{mode}_isochrone.gif"
    imageio.mimsave(gif_name, frames, duration=0.4)
    print(f"Saved {gif_name}!")

times = list(range(1, 31, 2)) # 1 to 30 mins
create_isochrone("walking", travel_speed=75, trip_times=times, network_type="walk")
create_isochrone("biking", travel_speed=250, trip_times=times, network_type="bike")

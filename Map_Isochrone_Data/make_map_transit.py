import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
import warnings
warnings.filterwarnings("ignore")

ox.settings.log_console=True

center_point = (41.321254, 2.074613)
trip_times = list(range(1, 31, 2))
max_dist = max(trip_times) * 600 # Assume transit can go up to 600m/min -> 18km max

print("Downloading walking network...")
G_walk = ox.graph_from_point(center_point, dist=max_dist, network_type="walk")

print("Downloading railway network...")
try:
    G_rail = ox.graph_from_point(center_point, dist=max_dist, custom_filter='["railway"~"subway|tram|light_rail|rail"]')
except Exception as e:
    print("No railway found, falling back to just walk.")
    G_rail = nx.MultiDiGraph()

# Project both to UTM
G_walk_proj = ox.project_graph(G_walk)
if len(G_rail) > 0:
    G_rail_proj = ox.project_graph(G_rail, to_crs=G_walk_proj.graph['crs'])
else:
    G_rail_proj = nx.MultiDiGraph()
    G_rail_proj.graph['crs'] = G_walk_proj.graph['crs']

# Calculate time for walking edges (75 m/min)
for u, v, k, data in G_walk_proj.edges(data=True, keys=True):
    data['time'] = data['length'] / 75.0
    data['is_rail'] = False

# Calculate time for rail edges (assume 40km/h = 666 m/min)
for u, v, k, data in G_rail_proj.edges(data=True, keys=True):
    if 'length' not in data:
        data['length'] = 100 # fallback
    data['time'] = data['length'] / 666.0
    data['is_rail'] = True

# Compose graphs
G_transit = nx.compose(G_walk_proj, G_rail_proj)

# Connect rail nodes to walk nodes (representing stations)
if len(G_rail) > 0:
    print("Connecting stations to walking network...")
    rail_nodes = list(G_rail_proj.nodes(data=True))
    # We need to find nearest walk nodes for all rail nodes
    # For speed, let's just do it for nodes that represent actual stations or just all rail nodes
    X = [data['x'] for n, data in rail_nodes]
    Y = [data['y'] for n, data in rail_nodes]
    nearest_walk_nodes = ox.distance.nearest_nodes(G_walk_proj, X=X, Y=Y)
    
    for (rail_node, data), walk_node in zip(rail_nodes, nearest_walk_nodes):
        # Add bidirectional edge with 3 minutes waiting/transfer penalty
        G_transit.add_edge(walk_node, rail_node, time=3.0, length=0, is_rail=False)
        G_transit.add_edge(rail_node, walk_node, time=0.5, length=0, is_rail=False) # exiting is fast

print("Finding center node...")
center_point_proj = ox.projection.project_geometry(
    ox.utils_geo.bbox_from_point(center_point, dist=1)[0].centroid,
    to_crs=G_transit.graph['crs']
)
center_node = ox.distance.nearest_nodes(G_transit, X=center_point_proj[0].x, Y=center_point_proj[0].y)

os.makedirs("frames_transit", exist_ok=True)
frames = []
print("Generating frames for transit...")

# Plotting settings
node_x = [data['x'] for n, data in G_transit.nodes(data=True)]
node_y = [data['y'] for n, data in G_transit.nodes(data=True)]
bbox = (min(node_y), max(node_y), max(node_x), min(node_x))

for i, t in enumerate(trip_times):
    subgraph_nodes = nx.ego_graph(G_transit, center_node, radius=t, distance='time').nodes()
    nc = ['#00ff00' if node in subgraph_nodes else 'none' for node in G_transit.nodes()]
    ns = [15 if node in subgraph_nodes else 0 for node in G_transit.nodes()]
    
    fig, ax = ox.plot_graph(G_transit, node_color=nc, node_size=ns, edge_color='#222222', edge_linewidth=0.5, show=False, close=False, bgcolor='black', figsize=(10,10))
    ax.set_title(f"Public Transport from Base - {t} minutes\n(Walk + Wait 3m + Rail)", color='white', fontsize=18, pad=10)
    
    filename = f"frames_transit/frame_{i:03d}.png"
    fig.savefig(filename, facecolor='black', dpi=150, bbox_inches='tight')
    frames.append(imageio.imread(filename))
    plt.close(fig)
    
gif_name = "transit_isochrone.gif"
imageio.mimsave(gif_name, frames, duration=0.4)
print(f"Saved {gif_name}!")

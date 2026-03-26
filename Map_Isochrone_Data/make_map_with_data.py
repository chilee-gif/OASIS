import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import imageio.v2 as imageio
import os
import warnings

# 忽略警告以保持輸出整潔
warnings.filterwarnings("ignore")

# 設定中心點 (El Prat de Llobregat, Barcelona)
center_point = (41.321254, 2.074613)

def create_isochrone_with_data(mode, travel_speed, trip_times, network_type, dataset_csv=None):
    """
    生成包含外部數據點（如 Smappen 導出的 POI）的等時線動畫。
    
    :param mode: 模式名稱 (e.g., 'walking_with_poi')
    :param travel_speed: 速度 (meters/minute)
    :param trip_times: 時間切片列表 (minutes)
    :param network_type: OSM 網路類型 ('walk', 'bike', 'drive')
    :param dataset_csv: Smappen 導出的 CSV 檔案路徑
    """
    print(f"--- 正在啟動 {mode} 整合模式 ---")
    
    # 1. 準備外部數據 (Dataset)
    gdf_poi = None
    if dataset_csv and os.path.exists(dataset_csv):
        print(f"讀取數據集: {dataset_csv}")
        df = pd.read_csv(dataset_csv)
        # 假設 CSV 包含 'latitude' 和 'longitude' 欄位
        if 'latitude' in df.columns and 'longitude' in df.columns:
            geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
            gdf_poi = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
            print(f"成功加載 {len(gdf_poi)} 個數據點。")
    
    # 2. 下載街道網路
    max_dist = max(trip_times) * travel_speed
    print(f"從 OSM 下載 {network_type} 網路 (範圍: {max_dist}m)...")
    G = ox.graph_from_point(center_point, dist=max_dist, network_type=network_type)
    G_proj = ox.project_graph(G)
    center_node = ox.distance.nearest_nodes(G, X=center_point[1], Y=center_point[0])
    
    # 如果有 POI 數據，將其轉換為與地圖一致的投影坐標 (UTM)
    if gdf_poi is not None:
        gdf_poi = gdf_poi.to_crs(G_proj.graph['crs'])

    # 3. 計算權重 (Time)
    for u, v, k, data in G_proj.edges(data=True, keys=True):
        data['time'] = data['length'] / travel_speed
        
    os.makedirs(f"frames_{mode}", exist_ok=True)
    frames = []
    
    # 4. 生成每一幀
    print(f"開始渲染動畫幀...")
    for i, t in enumerate(trip_times):
        # 獲取當前時間可達的節點
        subgraph_nodes = nx.ego_graph(G_proj, center_node, radius=t, distance='time').nodes()
        
        # 設定節點顏色 (賽博龐克風格)
        nc = ['#00ffff' if node in subgraph_nodes else 'none' for node in G_proj.nodes()]
        ns = [15 if node in subgraph_nodes else 0 for node in G_proj.nodes()]
        
        # 繪製地圖基礎
        fig, ax = ox.plot_graph(G_proj, node_color=nc, node_size=ns, edge_color='#222222', 
                                edge_linewidth=0.5, show=False, close=False, bgcolor='black', figsize=(12, 12))
        
        # 5. 整合 Dataset：繪製 POI 數據點
        if gdf_poi is not None:
            # 只有在可達區域內的點才亮起，或者全部顯示但用不同顏色
            gdf_poi.plot(ax=ax, color='#ff00ff', markersize=30, alpha=0.7, label='Dataset POIs')
        
        # 加入標題與統計資訊
        reachable_count = 0
        if gdf_poi is not None:
            # 簡單計算當前時間內覆蓋了多少點 (可選功能)
            reachable_count = len(gdf_poi) # 這裡可以細化為空間查詢
            
        ax.set_title(f"Isochrone: {t} min ({mode.split('_')[0]})\nCenter: El Prat de Llobregat", 
                     color='white', fontsize=18, pad=10)
        
        # 保存幀
        filename = f"frames_{mode}/frame_{i:03d}.png"
        fig.savefig(filename, facecolor='black', dpi=120, bbox_inches='tight')
        frames.append(imageio.imread(filename))
        plt.close(fig)
        
    # 6. 合成 GIF
    gif_name = f"{mode}_fusion.gif"
    imageio.mimsave(gif_name, frames, duration=0.4)
    print(f"✨ 整合完畢！動畫已儲存為: {gif_name}")

if __name__ == "__main__":
    # 範例執行：你可以將 'your_smappen_data.csv' 替換成實際檔名
    times = list(range(1, 31, 2))
    # 如果你已經有 CSV，請取消下面這行的註釋並修改路徑
    # create_isochrone_with_data("walking_data", travel_speed=75, trip_times=times, network_type="walk", dataset_csv="data.csv")
    print("腳本已就緒。請確保數據 CSV 檔案與此腳本放在同一目錄，或提供完整路徑。")

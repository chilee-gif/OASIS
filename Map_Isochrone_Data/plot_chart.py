import matplotlib.pyplot as plt
import numpy as np
import os

# 設置賽博龐克暗色風格
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# 時間 X 軸 (分鐘) 0 到 30 分鐘
t = np.linspace(0, 30, 300)

# 設定三種交通工具的速度 (公里/小時 -> 公尺/分鐘)
# 步行: 4.5 km/h -> 75 m/min
# 單車: 15 km/h -> 250 m/min
# 汽車: 36 km/h -> 600 m/min
speed_walk = 75
speed_bike = 250
speed_car = 600

# 計算每個時間點可以到達的最大距離 (公尺)
dist_walk = speed_walk * t
dist_bike = speed_bike * t
dist_car = speed_car * t

# 畫出這三條線 (對應你草圖左下角的概念，但我們將 X 軸放時間，Y 軸放距離，更符合直覺閱讀)
# 顏色對應剛剛的地圖動畫
ax.plot(t, dist_walk, label='Walking (4.5 km/h)', color='#00ffff', linewidth=2.5)  # 螢光青
ax.plot(t, dist_bike, label='Cycling (15 km/h)', color='#ffcc00', linewidth=2.5)   # 螢光黃
ax.plot(t, dist_car, label='Driving (36 km/h)', color='#ff00ff', linewidth=2.5)    # 螢光粉紅

# 大眾運輸 (Public Transport) 模擬：
# 假設前 5 分鐘都在走路去車站 (速度 = 步行)，等了 3 分鐘車
# 上車後速度極快 (假設 50 km/h = 833 m/min)
dist_transit = np.zeros_like(t)
for i, time_val in enumerate(t):
    if time_val <= 5:
        # 走去車站
        dist_transit[i] = speed_walk * time_val
    elif time_val <= 8:
        # 等車 (距離不變)
        dist_transit[i] = speed_walk * 5
    else:
        # 上車狂飆
        dist_transit[i] = (speed_walk * 5) + 833 * (time_val - 8)

ax.plot(t, dist_transit, label='Public Transport (Walk 5m + Wait 3m + Train)', color='#00ff00', linewidth=2.5, linestyle='--') # 螢光綠虛線

# 美化圖表
ax.set_title('Time vs. Reachable Distance by Transport Mode', color='white', fontsize=18, pad=15)
ax.set_xlabel('Time (Minutes)', color='lightgray', fontsize=14)
ax.set_ylabel('Max Reachable Distance (Meters)', color='lightgray', fontsize=14)

# 加上格線
ax.grid(True, color='#333333', linestyle=':', linewidth=1)

# 圖例
legend = ax.legend(facecolor='black', edgecolor='#555555', fontsize=12)
for text in legend.get_texts():
    text.set_color("white")

# 隱藏上方和右方的邊框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#555555')
ax.spines['left'].set_color('#555555')

# 儲存圖表
output_path = os.path.expanduser('~/workspace/map_animation/transport_chart.png')
plt.savefig(output_path, bbox_inches='tight')
print(f"Chart saved to {output_path}")

import os

def generate_enhanced_website():
    # 路徑設定
    base_dir = "/media/chi/ai_/Thesis_Oasis/Map_Isochrone_Data"
    gif_name = "thesis_smappen_fusion.gif"
    chart_name = "transport_chart.png"
    
    # 確保圖片存在（或使用替代方案）
    gif_path = gif_name if os.path.exists(os.path.join(base_dir, gif_name)) else ""
    chart_path = chart_name if os.path.exists(os.path.join(base_dir, chart_name)) else ""

    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Highline Oasis | 畢業論文研究展示</title>
    <style>
        :root {{
            --bg-color: #050505;
            --card-bg: #111111;
            --text-main: #e0e0e0;
            --text-dim: #999;
            --accent-cyan: #00ffff;
            --accent-pink: #ff00ff;
            --accent-gold: #ffcc00;
        }}
        body {{
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'PingFang TC', 'Microsoft JhengHei', sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.7;
        }}
        header {{
            height: 60vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: linear-gradient(to bottom, rgba(0,255,255,0.1), transparent), url('https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
            text-align: center;
            border-bottom: 1px solid var(--accent-cyan);
        }}
        h1 {{
            font-size: 4rem;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 5px;
            text-shadow: 0 0 20px var(--accent-cyan);
        }}
        .subtitle {{
            font-size: 1.5rem;
            color: var(--accent-cyan);
            margin-top: 10px;
            font-weight: 300;
        }}
        .container {{
            max-width: 1000px;
            margin: -50px auto 50px;
            padding: 0 20px;
        }}
        .section {{
            background: var(--card-bg);
            padding: 40px;
            border-radius: 15px;
            margin-bottom: 40px;
            border: 1px solid #222;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .section-title {{
            font-size: 2rem;
            color: var(--accent-pink);
            margin-bottom: 25px;
            display: flex;
            align-items: center;
        }}
        .section-title::before {{
            content: '';
            width: 5px;
            height: 30px;
            background: var(--accent-pink);
            margin-right: 15px;
            display: inline-block;
        }}
        .visual-container {{
            width: 100%;
            margin: 30px 0;
            text-align: center;
            border: 1px solid #333;
            border-radius: 10px;
            overflow: hidden;
            background: #000;
        }}
        .visual-container img {{
            max-width: 100%;
            display: block;
            margin: 0 auto;
        }}
        .caption {{
            padding: 15px;
            background: #151515;
            color: var(--text-dim);
            font-size: 0.9rem;
            font-style: italic;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }}
        .tag {{
            display: inline-block;
            padding: 3px 10px;
            background: rgba(0,255,255,0.1);
            color: var(--accent-cyan);
            border-radius: 5px;
            font-size: 0.8rem;
            margin-right: 10px;
            border: 1px solid var(--accent-cyan);
        }}
        footer {{
            text-align: center;
            padding: 50px;
            color: #444;
            font-size: 0.8rem;
        }}
        .logic-list {{
            list-style: none;
            padding: 0;
        }}
        .logic-list li {{
            margin-bottom: 15px;
            padding-left: 25px;
            position: relative;
        }}
        .logic-list li::before {{
            content: '▹';
            position: absolute;
            left: 0;
            color: var(--accent-gold);
        }}
    </style>
</head>
<body>

<header>
    <h1>The Highline Oasis</h1>
    <div class="subtitle">參數化微藻基礎設施與多模態樞紐</div>
    <p>El Prat de Llobregat, Barcelona</p>
</header>

<div class="container">
    
    <div class="section">
        <h2 class="section-title">01. 核心分析：多模態等時線融合</h2>
        <p>本研究利用 Python 空間分析工具，整合了 <b>OpenStreetMap (OSM)</b> 的街道網絡與 <b>Smappen</b> 的地點數據集。地圖展示了從基地中心出發，步行 1 至 30 分鐘的動態擴散範圍。</p>
        
        <div class="visual-container">
            <img src="{gif_path}" alt="Isochrone Fusion Animation">
            <div class="caption">圖：Isochrone + Smappen 數據融合動畫 (Cyberpunk 風格渲染)</div>
        </div>
        
        <ul class="logic-list">
            <li><span class="tag">OSMnx</span> 抓取真實城市街道結構，區分步行、單車與汽車路徑。</li>
            <li><span class="tag">NetworkX</span> 計算最短路徑演算法，實現真實時間的可達性分析。</li>
            <li><span class="tag">Smappen</span> 數據標註關鍵城市機能點位，評估設施覆蓋率。</li>
        </ul>
    </div>

    <div class="section">
        <h2 class="section-title">02. 建築設計邏輯</h2>
        <p>設計分為兩個核心拓撲層級，旨在解決城市連通性與環境永續：</p>
        <div class="grid">
            <div style="background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px;">
                <h3 style="color: var(--accent-cyan);">上層：Skywalk (空中步道)</h3>
                <p>靈感來自紐約 High Line，作為連續的參數化遮篷，打破地面層的交通障礙，串連城市綠廊。</p>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px;">
                <h3 style="color: var(--accent-gold);">下層：Programmatic Base (機能基座)</h3>
                <p>配置微藻生物反應器牆面 (Bio-Market)、工匠工坊與美食廣場。地面層高度滲透，邀請民眾自發互動。</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2 class="section-title">03. 數據驅動的空間決策</h2>
        <div class="visual-container">
            <img src="{chart_path}" alt="Transport Analysis Chart">
            <div class="caption">圖：不同交通模式的時間/距離可達性定量分析圖表</div>
        </div>
        <p>透過等時線數據，我們精確定位了「5分鐘步行圈」內的空間需求，並據此調整了市場入口的導向，確保建築與周邊社區的無縫對接。</p>
    </div>

</div>

<footer>
    <p>畢業論文專案 | ETSAV. UPC | 指導老師：Nelly ♓ (AI Assistant)</p>
</footer>

</body>
</html>
"""

    output_path = os.path.join(base_dir, "Thesis_Showcase.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # 同時複製到下載資料夾方便打開
    download_path = "/home/chi/Downloads/Thesis_Showcase.html"
    with open(download_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"網頁已儲存至: {output_path}")
    print(f"副本已傳送至下載資料夾: {download_path}")

if __name__ == "__main__":
    generate_enhanced_website()

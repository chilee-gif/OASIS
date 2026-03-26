import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Highline Oasis | Architectural Concept</title>
    <style>
        :root {
            --bg-color: #0d0d0d;
            --text-color: #f0f0f0;
            --accent-cyan: #00ffff;
            --accent-pink: #ff00ff;
            --accent-yellow: #ffcc00;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        header {
            background: linear-gradient(135deg, #111, #222);
            padding: 100px 20px;
            text-align: center;
            border-bottom: 2px solid var(--accent-cyan);
        }
        h1 {
            font-size: 4rem;
            margin: 0;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        h2 {
            color: var(--accent-cyan);
            font-weight: 300;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 50px 20px;
        }
        .section-title {
            font-size: 2.5rem;
            margin-bottom: 30px;
            border-left: 5px solid var(--accent-pink);
            padding-left: 15px;
        }
        p {
            font-size: 1.2rem;
            color: #ccc;
            margin-bottom: 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin-top: 50px;
        }
        .card {
            background: #1a1a1a;
            padding: 30px;
            border-radius: 8px;
            border: 1px solid #333;
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            border-color: var(--accent-yellow);
        }
        .image-placeholder {
            width: 100%;
            height: 300px;
            background: #222;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #555;
            font-style: italic;
            border: 1px dashed #444;
            margin-bottom: 20px;
        }
        .diagram-container {
            width: 100%;
            text-align: center;
            margin: 50px 0;
        }
        .diagram-container img {
            max-width: 100%;
            border: 1px solid var(--accent-cyan);
            border-radius: 8px;
        }
        footer {
            text-align: center;
            padding: 30px;
            background: #000;
            color: #666;
            margin-top: 50px;
            border-top: 1px solid #333;
        }
    </style>
</head>
<body>

<header>
    <h1>The Highline Oasis</h1>
    <h2>Parametric Microalgal Infrastructure & Multimodal Hub</h2>
    <p>El Prat de Llobregat, Barcelona (41.321254, 2.074613)</p>
</header>

<div class="container">
    
    <div class="diagram-container">
        <div class="image-placeholder">[Insert Architectural Section / Elevation Here]</div>
        <p><i>Figure 1: Main Architectural Section demonstrating the upper Skywalk and lower functional zones.</i></p>
    </div>

    <h3 class="section-title">01. Architectural Concept & Dual-Layer Topology</h3>
    <p>The architectural strategy is fundamentally divided into two distinct topological layers, creating a dynamic interplay between movement and stasis, public domain and programmatic function.</p>
    <p><strong>The Upper Level (The Skywalk):</strong> Inspired by the High Line in New York, the undulating roof structure functions as a continuous, elevated pedestrian corridor. It is a continuous, parametric canopy that gracefully swoops over the site, providing panoramic views and acting as a connective tissue across the urban fabric. This layer prioritizes flow, recreation, and atmospheric experience.</p>
    <p><strong>The Lower Level (The Programmatic Base):</strong> Sheltered beneath the sweeping canopy are the functional zones. The ground plane is highly porous. The areas left without specific color-coding in the plan are designed as extensive open public spaces—urban plazas that invite spontaneous interaction. Embedded within these open spaces are distinct, enclosed programmatic volumes (the "Markets"), catering to diverse community needs.</p>

    <h3 class="section-title">02. Spatial Synergy with Isochrone Data</h3>
    <p>This design is not an isolated object but a responsive node deeply rooted in its urban context. Building upon our recent multimodal isochrone analysis (Walking, Cycling, and Driving radii from the site center), the ground-level open spaces are strategically oriented toward the primary pedestrian approaches identified in the 5-minute and 10-minute walkability networks.</p>
    <p>The "Highline" skywalk effectively bridges the infrastructural barriers highlighted in the isochrone maps, expanding the site's accessibility and serving as a major attractor for both local residents and cyclists.</p>
    
    <div class="diagram-container">
        <div class="image-placeholder">[Insert Transport Isochrone Chart Here]</div>
        <p><i>Figure 2: Time vs. Reachable Distance by Transport Mode (Data Analysis from Previous Phase)</i></p>
    </div>

    <h3 class="section-title">03. Market Typologies (Plans, Elevations, Sections)</h3>
    <p>The lower level hosts several "Market" typologies. Each is treated as a distinct architectural volume beneath the unifying roof, allowing for independent environmental control and unique spatial identities.</p>
    
    <div class="grid">
        <div class="card">
            <h2 style="color: var(--accent-cyan);">Typology A: The Bio-Market</h2>
            <div class="image-placeholder">[Plan/Section of Bio-Market]</div>
            <p><strong>Concept:</strong> Integrated with the 3D-printed PETG Microalgal Reactor facade. This zone requires high sunlight exposure and water infrastructure.</p>
            <p><strong>Architecture:</strong> Open-plan layout with highly transparent, bio-reactive enclosures. The section reveals the integration of the algae tubes with the structural space frame.</p>
        </div>
        
        <div class="card">
            <h2 style="color: var(--accent-pink);">Typology B: The Artisan Hub</h2>
            <div class="image-placeholder">[Plan/Section of Artisan Hub]</div>
            <p><strong>Concept:</strong> A dense, highly partitioned area for local creators and craftsmen, demanding flexible, modular spatial divisions.</p>
            <p><strong>Architecture:</strong> Lower ceiling heights for intimacy, utilizing cross-ventilation drawn from the adjacent open public spaces. The elevation features dynamic shading devices.</p>
        </div>

        <div class="card">
            <h2 style="color: var(--accent-yellow);">Typology C: The Gastronomy Plaza</h2>
            <div class="image-placeholder">[Plan/Section of Gastronomy Plaza]</div>
            <p><strong>Concept:</strong> The social anchor. Requires large seating areas that seamlessly bleed into the un-colored, open public space.</p>
            <p><strong>Architecture:</strong> The section here is double-height, pushing up into the belly of the Skywalk structure, creating a dramatic, luminous dining hall.</p>
        </div>
        
        <div class="card">
            <h2 style="color: #fff;">Open Public Space (The Void)</h2>
            <div class="image-placeholder">[Plan/Section of Open Public Space]</div>
            <p><strong>Concept:</strong> The connective tissue. The "uncolored" areas that define the flow between the markets.</p>
            <p><strong>Architecture:</strong> Characterized by hardscaping, integrated seating, and landscape elements that respond to the shadow patterns cast by the parametric roof above.</p>
        </div>
    </div>
</div>

<footer>
    <p>Made_ ETSAV. UPC | Advanced Architectural Design Studio</p>
</footer>

</body>
</html>
"""

os.makedirs(os.path.expanduser('~/Desktop/Thesis_Presentation'), exist_ok=True)
output_path = os.path.expanduser('~/Desktop/Thesis_Presentation/index.html')

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Website saved to {output_path}")

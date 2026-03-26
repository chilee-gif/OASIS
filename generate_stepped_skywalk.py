import trimesh
import numpy as np
import os

def create_stepped_skywalk(input_path, output_path):
    print(f"Loading {input_path}...")
    scene_or_mesh = trimesh.load(input_path)
    
    if isinstance(scene_or_mesh, trimesh.Scene):
        mesh = scene_or_mesh.dump(concatenate=True)
    else:
        mesh = scene_or_mesh

    print("Analyzing structure for panel transformation...")
    
    # Get current bounds
    vertices = mesh.vertices.copy()
    faces = mesh.faces.copy()
    
    # Define parameters for the 'stepped' effect seen in screenshot
    amplitude = 6.0    # Vertical range
    freq = 0.08        # Frequency of the 'hill'
    step_height = 2.5  # Height of each stair/level
    
    # 1. Undulate vertices
    # We apply a sine wave based on Y coordinate (assuming it's the long axis)
    # Adding some X variation to make it more 'topographic'
    z_wave = amplitude * np.sin(vertices[:, 0] * freq) * np.cos(vertices[:, 1] * freq)
    vertices[:, 2] += z_wave
    
    # 2. Snap to Steps (quantization)
    # This creates the horizontal levels connected by vertical 'jumps'
    vertices[:, 2] = np.round(vertices[:, 2] / step_height) * step_height
    
    # 3. Create a thick slab effect (like the screenshot panels)
    # We duplicate vertices and shift them down to create volume
    thickness = 0.5
    bottom_vertices = vertices.copy()
    bottom_vertices[:, 2] -= thickness
    
    # Combine top and bottom
    all_vertices = np.vstack([vertices, bottom_vertices])
    
    # Adjust faces for new vertex indices
    bottom_faces = faces + len(vertices)
    # (Simplified: just using original faces for top/bottom shells)
    all_faces = np.vstack([faces, bottom_faces[:, ::-1]]) # Bottom faces oriented inward
    
    # Create new mesh
    new_mesh = trimesh.Trimesh(vertices=all_vertices, faces=all_faces)
    
    # 4. Optional: Bridge the vertical gaps to look like stairs
    # Since we snapped to step_height, there are vertical 'tears' in the mesh
    # We can keep these or weld them. For 'panels' look, we keep the stepped look.
    
    print(f"Saving modified model to {output_path}...")
    new_mesh.export(output_path)
    print("Done!")

if __name__ == "__main__":
    input_file = "/media/chi/ai_/Thesis_Oasis/assets/up.obj"
    output_file = "/media/chi/ai_/Thesis_Oasis/assets/up_skywalk_stepped.obj"
    create_stepped_skywalk(input_file, output_file)

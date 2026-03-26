import trimesh
import os

input_file = "/media/chi/ai_/Thesis_Oasis/assets/base.obj"
output_file = "/media/chi/ai_/Thesis_Oasis/assets/base_compressed.obj"

print(f"Loading {input_file}...")
mesh = trimesh.load(input_file)

# If it's a scene, get the main mesh
if isinstance(mesh, trimesh.Scene):
    print("Detected Scene, merging into single mesh...")
    mesh = mesh.dump(concatenate=True)

print(f"Original face count: {len(mesh.faces)}")

# Decimate mesh (simplify to 20% of original)
# Target faces to be well under 100MB limit, aiming for around 20-30MB
target_faces = int(len(mesh.faces) * 0.15) 
print(f"Targeting {target_faces} faces for compression...")

try:
    mesh_simplified = mesh.simplify_quadratic_decimation(target_faces)
    print(f"Simplified face count: {len(mesh_simplified.faces)}")
    mesh_simplified.export(output_file)
    print(f"Exported to {output_file}")
except Exception as e:
    print(f"Simplification failed: {e}")
    # Fallback: just try to export as a different format or lower precision
    mesh.export(output_file)

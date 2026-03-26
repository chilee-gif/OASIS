import trimesh
import numpy as np
import os

input_file = "/media/chi/ai_/Thesis_Oasis/assets/up.obj"
output_file = "/media/chi/ai_/Thesis_Oasis/assets/up_skywalk.obj"

print(f"Loading {input_file}...")
mesh = trimesh.load(input_file)

if isinstance(mesh, trimesh.Scene):
    mesh = mesh.dump(concatenate=True)

print("Transforming panels into undulating skywalk...")

# Get vertex positions
vertices = mesh.vertices.copy()

# 1. Apply Sine wave for undulating (上下起伏)
# We assume the skywalk stretches along one horizontal axis (e.g., Y or X)
# Let's use a combination of X and Y to be safe
freq = 0.05 # frequency of waves
amplitude = 15.0 # height of waves
z_offset = amplitude * np.sin(vertices[:, 0] * freq) * np.cos(vertices[:, 1] * freq)
vertices[:, 2] += z_offset

# 2. Create "Stepped" effect (樓梯感)
# Use a floor function to snap Z coordinates to specific height levels
step_height = 2.0
vertices[:, 2] = np.round(vertices[:, 2] / step_height) * step_height

# Update mesh vertices
mesh.vertices = vertices

# Save modified mesh
print(f"Saving to {output_file}...")
mesh.export(output_file)
print("Transformation complete!")

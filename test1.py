import pyvista as pv
import numpy as np
from PIL import Image

# Load your STL file (replace 'your_model.stl' with your STL file)
mesh = pv.read("C://Users//Akash//OneDrive//Desktop//Mini Project//Me 1//Test Output//Demo//stitched_model (2).stl")

# Load the image for texture mapping (replace 'your_image.jpg' with your image file)
image_path = "C://Users//Akash//OneDrive//Desktop//Mini Project//Me 1//Test Output//Demo//demo.jpg"
texture = pv.read_texture(image_path)

# Apply texture mapping to the mesh
mesh.texture_map_to_plane(inplace=True)

# Plot the textured mesh
plotter = pv.Plotter()
plotter.add_mesh(mesh, texture=texture)  # Use the texture directly here
plotter.show()
# output_path = "E:\\textured_birds.ply"
# mesh.save(output_path)
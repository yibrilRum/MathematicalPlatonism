import numpy as np
from mayavi import mlab

# --- Unit Conversion ---
def inches_to_meters(inches):
    """Converts inches to meters"""
    return inches * 0.0254

def feet_to_meters(feet):
    """Converts feet to meters"""
    return feet * 0.3048

# --- Drawing Functions ---
def draw_cube(edge_length_m):
    """Draw a cube based on edge length in meters"""
    x, y, z = np.mgrid[0:edge_length_m:2j, 0:edge_length_m:2j, 0:edge_length_m:2j]
    scalars = x * y * z
    mlab.contour3d(x, y, z, scalars)
    mlab.show()

def draw_sphere(radius_m):
    """Draw a sphere based on radius in meters"""
    phi, theta = np.mgrid[0:np.pi:100j, 0:2*np.pi:100j]
    x = radius_m * np.sin(phi) * np.cos(theta)
    y = radius_m * np.sin(phi) * np.sin(theta)
    z = radius_m * np.cos(phi)
    mlab.mesh(x, y, z)
    mlab.show()

def draw_cylinder(radius_m, height_m):
    """Draw a cylinder based on radius and height in meters"""
    phi, z = np.mgrid[0:2*np.pi:100j, 0:height_m:100j]
    x = radius_m * np.cos(phi)
    y = radius_m * np.sin(phi)
    mlab.mesh(x, y, z)
    mlab.show()

# --- Main Drawing Prompt Function ---
def prompt_and_draw_shape():
    shape = input("Choose a shape to draw (cube, sphere, cylinder): ").strip().lower()

    if shape == "cube":
        edge = float(input("Enter edge length (in inches): "))
        edge_m = inches_to_meters(edge)
        print(f"Drawing a cube with edge {edge_m} meters.")
        draw_cube(edge_m)
    
    elif shape == "sphere":
        radius = float(input("Enter radius (in inches): "))
        radius_m = inches_to_meters(radius)
        print(f"Drawing a sphere with radius {radius_m} meters.")
        draw_sphere(radius_m)
    
    elif shape == "cylinder":
        radius = float(input("Enter radius (in inches): "))
        height = float(input("Enter height (in inches): "))
        radius_m = inches_to_meters(radius)
        height_m = inches_to_meters(height)
        print(f"Drawing a cylinder with radius {radius_m} meters and height {height_m} meters.")
        draw_cylinder(radius_m, height_m)

    else:
        print("Shape not recognized. Please try again.")
        prompt_and_draw_shape()

# Run the function for testing
if __name__ == "__main__":
    prompt_and_draw_shape()

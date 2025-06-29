# You may need to install plotly and numpy using pip.
# pip install numpy
# pip install plotly
import plotly.graph_objects as go
import numpy as np

# Define the 10x10x10 grid (each small cube is 0.1 m = 10 cm)
n = 10  # Divisions per side
size = 1.0  # Side length of the large cube (1 meter)
step = size / n  # Size of each small cube (0.1 m)

# Generate grid points
x = np.linspace(0, size, n + 1)
y = np.linspace(0, size, n + 1)
z = np.linspace(0, size, n + 1)
X, Y, Z = np.meshgrid(x, y, z)

# Flatten arrays for scatter plot
x_flat = X.flatten()
y_flat = Y.flatten()
z_flat = Z.flatten()

# Create scatter plot for grid points
scatter = go.Scatter3d(
    x=x_flat,
    y=y_flat,
    z=z_flat,
    mode='markers',
    marker=dict(size=2, color='blue'),
    name='Grid Points'
)

# Create lines to outline the small cubes (for clarity)
lines = []
for i in range(n + 1):
    for j in range(n + 1):
        # Lines along z-axis
        lines.append(go.Scatter3d(
            x=[x[i], x[i]],
            y=[y[j], y[j]],
            z=[0, size],
            mode='lines',
            line=dict(color='gray', width=1),
            showlegend=False
        ))
        # Lines along y-axis
        lines.append(go.Scatter3d(
            x=[x[i], x[i]],
            y=[0, size],
            z=[z[j], z[j]],
            mode='lines',
            line=dict(color='gray', width=1),
            showlegend=False
        ))
    for k in range(n + 1):
        # Lines along x-axis
        lines.append(go.Scatter3d(
            x=[0, size],
            y=[y[i], y[i]],
            z=[z[k], z[k]],
            mode='lines',
            line=dict(color='gray', width=1),
            showlegend=False
        ))

# Highlight one small cube (e.g., at position (0,0,0))
cube_vertices = [
    [0, 0, 0], [step, 0, 0], [step, step, 0], [0, step, 0],  # Bottom face
    [0, 0, step], [step, 0, step], [step, step, step], [0, step, step]  # Top face
]
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]
cube_lines = []
for edge in cube_edges:
    x_edge = [cube_vertices[edge[0]][0], cube_vertices[edge[1]][0]]
    y_edge = [cube_vertices[edge[0]][1], cube_vertices[edge[1]][1]]
    z_edge = [cube_vertices[edge[0]][2], cube_vertices[edge[1]][2]]
    cube_lines.append(go.Scatter3d(
        x=x_edge,
        y=y_edge,
        z=z_edge,
        mode='lines',
        line=dict(color='red', width=4),
        name='Sample Cube'
    ))

# Create the figure
fig = go.Figure(data=[scatter] + lines + cube_lines)

# Update layout with corrected annotation
fig.update_layout(
    title="3D Cube Divided into 10x10x10 Grid (1,000 Small Cubes)",
    scene=dict(
        xaxis_title="X (meters)",
        yaxis_title="Y (meters)",
        zaxis_title="Z (meters)",
        aspectmode='cube',
        annotations=[
            dict(
                x=0.5,
                y=0.5,
                z=1.2,  # Place above the cube
                text="1-meter cube divided into 10x10x10 = 1,000 small cubes<br>"
                     "Each small cube is 10 cm x 10 cm x 10 cm<br>"
                     "To reach 1 billion pieces, divide each small cube into 1,000 smaller 1-mm cubes<br>"
                     "Red cube: One small cube (1 of 1,000 shown)",
                showarrow=False,
                font=dict(size=10)
            )
        ]
    ),
    showlegend=True
)

# Show the plot
fig.show()

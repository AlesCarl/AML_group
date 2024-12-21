import numpy as np
import pyvista as pv

def convert_obj_to_npz(obj_path, npz_path):
    vertices, faces = read_obj(obj_path)
    np.savez(npz_path, vertices=vertices, faces=faces)
    print(f"Converted {obj_path} to {npz_path}")


def read_obj(file_path):
    vertices = []
    faces = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):  # Vertex
                vertices.append(list(map(float, line.split()[1:])))
            elif line.startswith('f '):  # Face
                face = [int(part.split('/')[0]) - 1 for part in line.split()[1:]]
                faces.append(face)
    return np.array(vertices), np.array(faces)

def visualize(filename):
    # Load point cloud data
    data = np.load(filename)
    points = data['vertices']

    # Create a PyVista PolyData object
    cloud = pv.PolyData(points)

    # Visualize
    plotter = pv.Plotter()
    plotter.add_mesh(cloud, color='black', point_size=5)
    plotter.show()


if __name__ == '__main__':
    # Convert .obj to .npz
    # convert_obj_to_npz('./data/horse.obj', './data/point_clouds/horse.npz')
    # convert_obj_to_npz('./data/candle.obj', './data/point_clouds/candle.npz')
    # convert_obj_to_npz('./data/dog.obj', './data/point_clouds/dog.npz')

    visualize('./data/point_clouds/horse.npz')

    pass
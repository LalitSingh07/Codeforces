#Anton and Polyhedrons

n = int(input())
faces = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
total_faces = 0
for _ in range(n):
    total_faces += faces[input()]

print(total_faces)
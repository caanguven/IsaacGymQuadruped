"""
Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
NVIDIA CORPORATION and its licensors retain all intellectual property
and proprietary rights in and to this software, related documentation
and any modifications thereto. Any use, reproduction, disclosure or
distribution of this software and related documentation without an express
license agreement from NVIDIA CORPORATION is strictly prohibited.

Tet file generation example for Isaac Gym Soft Body meshes using fTetWild

"""

mesh_file = open("/home/can/Downloads/Body/body_v2.mesh", "r")
tet_output = open("body_v2.tet", "w")

mesh_lines = list(mesh_file)
mesh_lines = [line.strip('\n') for line in mesh_lines]
vertices_start = mesh_lines.index('Vertices')
num_vertices = mesh_lines[vertices_start + 1]

vertices = mesh_lines[vertices_start + 2: vertices_start + 2 + int(num_vertices)]

tetrahedra_start = mesh_lines.index('Tetrahedra')
num_tetrahedra = mesh_lines[tetrahedra_start + 1]
tetrahedra = mesh_lines[tetrahedra_start + 2 : tetrahedra_start + 2 + int(num_tetrahedra)]

print(num_vertices, num_tetrahedra)

# Write to tet output
tet_output.write("# Tetrahedral mesh generated using\n\n")
tet_output.write("# " + num_vertices + " vertices\n")
for v in vertices:
	tet_output.write("v " + v + "\n")
tet_output.write("\n")
tet_output.write("# " + num_tetrahedra + " tetrahedra\n")
for t in tetrahedra:
	l = t.split(' 0')[0]
	l = l.split(" ")
	l = [str(int(k) - 1) for k in l]
	l_text = ' '.join(l)
	tet_output.write("t " + l_text + "\n")


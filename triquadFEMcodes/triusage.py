from triquadglobalstiffnessmatrix import connectivity
from triquadglobalforce import traction_force_triangle
from triquaddisplacement import disp
from triquadstressstrain import element_strain
from triquadplot import plotting
from triquadplot import plotting_mesh
from triquadplot import display_tri
import meshio
import numpy as np
import matplotlib.pyplot as plt
def triangular_elements():
    mesh = meshio.read('tri.msh')
    nodes = mesh.points
    triangle = mesh.get_cells_type("triangle") 
    return nodes,triangle
nodes,elements=triangular_elements()
elements=np.array(elements)
print(elements)
nodes=nodes[:,[0,1]]
E = 1e7
v = 0.3
t = [0,-1e5]
num_processes=8
def eqn(y):
    return 2
displacements={0:[0,0],3:[0,0],11:[0,0]}
loads={0:[0,0],3:[0,0],11:[0,0]}
if __name__=='__main__':
    plotting_mesh(nodes,elements)
    k_global=connectivity(nodes, elements, v,E,num_processes)
    f1=traction_force_triangle(nodes,elements,10,t,[0,0.5],y = None,x=eqn)
    f2=traction_force_triangle(nodes,elements,16,t,[0.5,1],y = None,x=eqn)
    U=disp(displacements,loads,nodes,elements,v,E,num_processes,[10,16],forces=[f1,f2])
    total_force=np.dot(k_global,U)
    e,s=element_strain(nodes,elements,v,E,U)
    plotting(nodes,elements,U)
    dp=display_tri(nodes,U,elements,e[0,:])
    plt.show()


# nodes = np.array([[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]])
# elements = [[1,2,4],[2,5,4],[2,3,5],[3,6,5], [6,9,8],[5,6,8],[5,8,7],[4,5,7]]
# elements = np.array(elements)-1
# t =[1,0]
# v=0
# E=1
# num_processes=8
# def eqn(y):
#     return 2
# displacements={0:[0,0],3:[0,0],6:[0,0]}
# loads={0:[0,0],3:[0,0],6:[0,0]}
# if __name__=='__main__':
#     k_global=connectivity(nodes, elements, v,E,num_processes)
#     f1=traction_force_triangle(nodes,elements,3,t,[0,1],y = None,x=eqn)
#     f2=traction_force_triangle(nodes,elements,4,t,[1,2],y = None,x=eqn)
#     U=disp(displacements,loads,nodes,elements,v,E,num_processes,[3,4],forces=[f1,f2])
#     total_force=np.dot(k_global,U)
#     e,s=element_strain(nodes,elements,v,E,U)
#     plotting(nodes,elements,U)
#     dp=display_tri(nodes,U,elements,e[0,:])
#     plt.show()
    


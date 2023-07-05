from triquadglobalstiffnessmatrix import connectivity
from triquadglobalforce import boundary_forces_quad
from triquaddisplacement import disp
from triquadstressstrain import element_strain
from triquadplot import plotting
from triquadplot import plotting_mesh
from triquadplot import display_quad
import meshio
import numpy as np
import matplotlib.pyplot as plt

def quadrilateral_elements():
    mesh = meshio.read('quad.msh')
    nodes = mesh.points
    quads = mesh.get_cells_type("quad")
    return nodes,quads
nodes,elements=quadrilateral_elements()
elements=np.array(elements)
nodes=nodes[:,[0,1]]
# nodes = np.array([[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]])
# elements=[[1,2,5,4],[2,3,6,5],[5,6,9,8],[4,5,8,7]]
# elements=np.array(elements)-1
E=1
t=[1,0]
num_processes=8
v=0.3
displacements={0:[0,0],3:[0,0],11:[0,0]}
loads={0:[0,0],3:[0,0],11:[0,0]}
if __name__=='__main__':
    plotting_mesh(nodes,elements)
    k_global=connectivity(nodes, elements, v,E,num_processes)
    # f1=boundary_forces_quad(nodes,elements,t,traction_element=7,psi = 1, eta = 0)
    f2=boundary_forces_quad(nodes,elements,t,traction_element=8,psi = 0, eta = 1)
    f3=boundary_forces_quad(nodes,elements,t,traction_element=9,psi = -1, eta = 0)
    U=disp(displacements,loads,nodes,elements,v,E,num_processes,[8,9],forces=[f2,f3])
    total_force=np.dot(k_global,U)
    e,s=element_strain(nodes,elements,v,E,U)
    print(e)
    plotting(nodes,elements,U)
    plt.show()
    _,ax1= plt.subplots()
    # _,ax2 = plt.subplots()
    display_quad(nodes,elements,ax1,s[:,0,:])
    # display_quad(nodes,elements,ax2,s[:,0,:])

    plt.show()
   

from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.05, exposure=2)
scene.set_directional_light((1, 1, 1), 0.01, (1, 1, 1))
scene.set_background_color((0.3, 0.4, 0.6))
scene.set_floor(-20/64, (1, 1, 1))

@ti.kernel
def initialize_voxels():
    for i, j, k in ti.ndrange((0, 81), (0, 81), (0, 81)):
        draw = True
        for x in ti.static([3, 9, 27, 81]):
            if int((i%x)//(x//3)==1)+int((j%x)//(x//3)==1)+int((k%x)//(x//3)==1) >= 2:
                draw = False
        if draw:
            scene.set_voxel(vec3(i-20, j-20, k-20), 1, vec3(0.9, 0.3, 0.3))

initialize_voxels()
scene.finish()

import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from phong import material_phong

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glLightfv(GL_LIGHT0, GL_POSITION, [3, 3, 3, 1])

    material_phong([0.2]*4, [0.8]*4, [1, 1, 1, 1], 50)
    glutSolidTeapot(1)

    glutSwapBuffers()

glutInit(sys.argv)  # 🔴 ESSENCIAL
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Phong")

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)

glutDisplayFunc(display)
glutMainLoop()

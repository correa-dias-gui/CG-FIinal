from OpenGL.GL import *

def material_phong(amb, diff, spec, shininess):
    glMaterialfv(GL_FRONT, GL_AMBIENT, amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diff)
    glMaterialfv(GL_FRONT, GL_SPECULAR, spec)
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)

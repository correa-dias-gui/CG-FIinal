"""
Exercício 5 - Modelo de Iluminação de Phong
Renderiza três objetos 3D (torus, esfera, teapot) com diferentes materiais
e múltiplas fontes de luz, com interação do usuário para rotação.
"""

import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from phong import material_phong

# Variáveis globais para rotação
rotation_x = 0.0
rotation_y = 0.0
mouse_x = 0
mouse_y = 0
mouse_pressed = False

def setup_lights():
    """Configura múltiplas fontes de luz (direcional e pontual)"""
    
    # Luz 0 - Pontual (branca)
    glEnable(GL_LIGHT0)
    light0_pos = [3.0, 3.0, 3.0, 1.0]  # w=1.0 para luz pontual
    light0_ambient = [0.2, 0.2, 0.2, 1.0]
    light0_diffuse = [0.8, 0.8, 0.8, 1.0]
    light0_specular = [1.0, 1.0, 1.0, 1.0]
    
    glLightfv(GL_LIGHT0, GL_POSITION, light0_pos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light0_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light0_specular)
    
    # Luz 1 - Direcional (azulada)
    glEnable(GL_LIGHT1)
    light1_dir = [-1.0, -0.5, -1.0, 0.0]  # w=0.0 para luz direcional
    light1_ambient = [0.1, 0.1, 0.2, 1.0]
    light1_diffuse = [0.3, 0.3, 0.6, 1.0]
    light1_specular = [0.5, 0.5, 1.0, 1.0]
    
    glLightfv(GL_LIGHT1, GL_POSITION, light1_dir)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light1_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light1_specular)
    
    # Luz 2 - Pontual vermelha (mais fraca)
    glEnable(GL_LIGHT2)
    light2_pos = [-2.0, 1.0, 2.0, 1.0]
    light2_ambient = [0.1, 0.0, 0.0, 1.0]
    light2_diffuse = [0.4, 0.1, 0.1, 1.0]
    light2_specular = [0.8, 0.2, 0.2, 1.0]
    
    glLightfv(GL_LIGHT2, GL_POSITION, light2_pos)
    glLightfv(GL_LIGHT2, GL_AMBIENT, light2_ambient)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_diffuse)
    glLightfv(GL_LIGHT2, GL_SPECULAR, light2_specular)

def material_metalico():
    """Material metálico para o torus"""
    ambient = [0.2, 0.2, 0.2, 1.0]
    diffuse = [0.6, 0.6, 0.6, 1.0]
    specular = [0.9, 0.9, 0.9, 1.0]
    shininess = 100.0
    material_phong(ambient, diffuse, specular, shininess)

def material_ceramico():
    """Material cerâmico para o teapot"""
    ambient = [0.1, 0.05, 0.0, 1.0]
    diffuse = [0.7, 0.4, 0.2, 1.0]
    specular = [0.3, 0.3, 0.3, 1.0]
    shininess = 20.0
    material_phong(ambient, diffuse, specular, shininess)

def material_plastico():
    """Material plástico para a esfera"""
    ambient = [0.0, 0.1, 0.1, 1.0]
    diffuse = [0.2, 0.7, 0.7, 1.0]
    specular = [0.8, 0.8, 0.8, 1.0]
    shininess = 60.0
    material_phong(ambient, diffuse, specular, shininess)

def draw_torus():
    """Desenha torus com material metálico"""
    glPushMatrix()
    glTranslatef(-3.0, 0.0, 0.0)
    glRotatef(rotation_x * 0.5, 1, 0, 0)
    glRotatef(rotation_y * 0.5, 0, 1, 0)
    material_metalico()
    glutSolidTorus(0.3, 1.0, 20, 20)
    glPopMatrix()

def draw_sphere():
    """Desenha esfera com material plástico"""
    glPushMatrix()
    glTranslatef(3.0, 0.0, 0.0)
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)
    material_plastico()
    glutSolidSphere(1.0, 30, 30)
    glPopMatrix()

def draw_teapot():
    """Desenha teapot com material cerâmico"""
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(rotation_x * 0.8, 1, 0, 0)
    glRotatef(rotation_y * 0.8, 0, 1, 0)
    material_ceramico()
    glutSolidTeapot(1.0)
    glPopMatrix()

def display():
    """Função de renderização principal"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Configurar câmera
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 2.0, 8.0,  # posição da câmera
              0.0, 0.0, 0.0,  # olhando para
              0.0, 1.0, 0.0)  # vetor up
    
    # Configurar luzes
    setup_lights()
    
    # Desenhar objetos
    draw_torus()     # À esquerda - Material metálico
    draw_teapot()    # Centro - Material cerâmico  
    draw_sphere()    # À direita - Material plástico
    
    glutSwapBuffers()

def reshape(width, height):
    """Redimensionamento da janela"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, width/height, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

def mouse_motion(x, y):
    """Movimento do mouse para rotação"""
    global rotation_x, rotation_y, mouse_x, mouse_y, mouse_pressed
    
    if mouse_pressed:
        dx = x - mouse_x
        dy = y - mouse_y
        rotation_y += dx * 0.5
        rotation_x += dy * 0.5
        
        # Limitar rotação vertical
        if rotation_x > 90:
            rotation_x = 90
        if rotation_x < -90:
            rotation_x = -90
            
        glutPostRedisplay()
    
    mouse_x = x
    mouse_y = y

def mouse_click(button, state, x, y):
    """Clique do mouse"""
    global mouse_pressed, mouse_x, mouse_y
    
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            mouse_pressed = True
            mouse_x = x
            mouse_y = y
        else:
            mouse_pressed = False

def keyboard(key, x, y):
    """Teclado para controles adicionais"""
    global rotation_x, rotation_y
    
    if key == b'r':  # Reset rotação
        rotation_x = 0.0
        rotation_y = 0.0
        glutPostRedisplay()
    elif key == b'q' or key == b'\x1b':  # ESC para sair
        sys.exit()

def idle():
    """Função idle para animação suave"""
    glutPostRedisplay()

def init_opengl():
    """Inicialização do OpenGL"""
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_NORMALIZE)  # Normalizar vetores normais
    glEnable(GL_COLOR_MATERIAL)
    
    # Cor de fundo
    glClearColor(0.1, 0.1, 0.2, 1.0)
    
    # Modelo de sombreamento suave
    glShadeModel(GL_SMOOTH)

def main():
    """Função principal"""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1024, 768)
    glutInitWindowPosition(100, 100)
    window = glutCreateWindow(b"Exercicio 5 - Modelo de Iluminacao de Phong")
    
    init_opengl()
    
    # Registrar callbacks
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMotionFunc(mouse_motion)
    glutMouseFunc(mouse_click)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    
    # Instruções
    print("=== Exercício 5 - Modelo de Iluminação de Phong ===")
    print("Objetos renderizados:")
    print("- Torus (esquerda): Material metálico")
    print("- Teapot (centro): Material cerâmico")
    print("- Esfera (direita): Material plástico")
    print("\nControles:")
    print("- Arraste com mouse esquerdo: Rotacionar objetos")
    print("- Tecla 'r': Reset rotação")
    print("- Tecla 'q' ou ESC: Sair")
    print("\nFontes de luz:")
    print("- Luz 0: Pontual branca (principal)")
    print("- Luz 1: Direcional azulada")
    print("- Luz 2: Pontual vermelha (acento)")
    
    glutMainLoop()

if __name__ == "__main__":
    main()

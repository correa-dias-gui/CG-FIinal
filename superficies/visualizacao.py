"""
Módulo de visualização que suporta OpenGL e matplotlib
Usa OpenGL por padrão, com matplotlib como fallback
"""

import sys
import numpy as np

def use_matplotlib():
    """Verifica se deve usar matplotlib baseado nos argumentos"""
    return 'matplotlib' in sys.argv

def plot_curves_2d(curves_data, title="Curvas de Bézier", window_size=(800, 600)):
    """
    Plota curvas 2D usando OpenGL ou matplotlib
    
    curves_data: lista de dicionários com:
        - 'points': array de pontos
        - 'label': string do rótulo
        - 'color': tuple RGB (0-1)
        - 'line_style': 'solid' ou 'dashed'
        - 'point_style': 'scatter' ou None
    """
    
    if use_matplotlib():
        _plot_curves_2d_matplotlib(curves_data, title)
    else:
        _plot_curves_2d_opengl(curves_data, title, window_size)

def plot_surface_3d(points, title="Superfície 3D", window_size=(1024, 768)):
    """
    Plota superfície 3D usando OpenGL ou matplotlib
    
    points: array Nx3 de pontos 3D
    """
    
    if use_matplotlib():
        _plot_surface_3d_matplotlib(points, title)
    else:
        _plot_surface_3d_opengl(points, title, window_size)

def _plot_curves_2d_matplotlib(curves_data, title):
    """Implementação matplotlib para curvas 2D"""
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    
    for curve in curves_data:
        points = curve['points']
        label = curve.get('label', '')
        color = curve.get('color', (0, 0, 1))
        line_style = '--' if curve.get('line_style') == 'dashed' else '-'
        
        if curve.get('point_style') == 'scatter':
            plt.scatter(points[:,0], points[:,1], 
                       color=color, label=label, s=80)
        else:
            plt.plot(points[:,0], points[:,1], 
                    line_style, color=color, label=label, linewidth=2)
    
    plt.legend()
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.show()

def _plot_surface_3d_matplotlib(points, title):
    """Implementação matplotlib para superfície 3D"""
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(points[:,0], points[:,1], points[:,2], 
               c=points[:,2], cmap='viridis', s=5)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y') 
    ax.set_zlabel('Z')
    ax.set_title(title)
    
    plt.show()

def _plot_curves_2d_opengl(curves_data, title, window_size):
    """Implementação OpenGL para curvas 2D"""
    try:
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
        import OpenGL.GLUT as glut
    except ImportError:
        print("OpenGL não disponível, usando matplotlib...")
        return _plot_curves_2d_matplotlib(curves_data, title)
    
    # Variáveis globais para OpenGL
    global gl_curves_data, gl_title
    gl_curves_data = curves_data
    gl_title = title
    
    def display_2d():
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glLoadIdentity()
        
        # Calcular bounds dos dados
        all_points = np.vstack([curve['points'] for curve in gl_curves_data])
        x_min, x_max = all_points[:,0].min(), all_points[:,0].max()
        y_min, y_max = all_points[:,1].min(), all_points[:,1].max()
        
        # Margem de 10%
        margin_x = (x_max - x_min) * 0.1
        margin_y = (y_max - y_min) * 0.1
        x_min -= margin_x; x_max += margin_x
        y_min -= margin_y; y_max += margin_y
        
        # Configurar projeção ortogonal
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluOrtho2D(x_min, x_max, y_min, y_max)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        
        # Desenhar as curvas
        for curve in gl_curves_data:
            points = curve['points']
            color = curve.get('color', (0, 0, 1))
            line_style = curve.get('line_style', 'solid')
            point_style = curve.get('point_style')
            
            gl.glColor3f(*color)
            
            if point_style == 'scatter':
                gl.glPointSize(8)
                gl.glBegin(gl.GL_POINTS)
                for point in points:
                    gl.glVertex2f(point[0], point[1])
                gl.glEnd()
            else:
                if line_style == 'dashed':
                    gl.glEnable(gl.GL_LINE_STIPPLE)
                    gl.glLineStipple(1, 0x00FF)
                
                gl.glLineWidth(2)
                gl.glBegin(gl.GL_LINE_STRIP)
                for point in points:
                    gl.glVertex2f(point[0], point[1])
                gl.glEnd()
                
                if line_style == 'dashed':
                    gl.glDisable(gl.GL_LINE_STIPPLE)
        
        glut.glutSwapBuffers()
    
    def keyboard_2d(key, x, y):
        if key == b'q' or key == b'\x1b':  # ESC para sair
            try:
                glut.glutLeaveMainLoop()
            except:
                sys.exit()
    
    def reshape_2d(width, height):
        gl.glViewport(0, 0, width, height)
    
    # Inicializar GLUT
    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(*window_size)
    glut.glutInitWindowPosition(100, 100)
    glut.glutCreateWindow(title.encode())
    
    # Configurar OpenGL
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)  # Fundo branco
    gl.glEnable(gl.GL_LINE_SMOOTH)
    gl.glEnable(gl.GL_POINT_SMOOTH)
    
    # Registrar callbacks
    glut.glutDisplayFunc(display_2d)
    glut.glutReshapeFunc(reshape_2d)
    glut.glutKeyboardFunc(keyboard_2d)
    
    print(f"=== {title} ===")
    print("Pressione 'q' ou ESC para sair")
    
    glut.glutMainLoop()

def _plot_surface_3d_opengl(points, title, window_size):
    """Implementação OpenGL para superfície 3D"""
    try:
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
        import OpenGL.GLUT as glut
    except ImportError:
        print("OpenGL não disponível, usando matplotlib...")
        return _plot_surface_3d_matplotlib(points, title)
    
    # Variáveis globais para OpenGL
    global gl_points, gl_rotation_x, gl_rotation_y, gl_mouse_x, gl_mouse_y, gl_mouse_pressed
    gl_points = points
    gl_rotation_x = 20.0
    gl_rotation_y = 45.0
    gl_mouse_x = 0
    gl_mouse_y = 0
    gl_mouse_pressed = False
    
    def display_3d():
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()
        
        # Posicionar câmera
        x_center = np.mean(gl_points[:,0])
        y_center = np.mean(gl_points[:,1])
        z_center = np.mean(gl_points[:,2])
        
        # Calcular distância apropriada
        ranges = [gl_points[:,i].max() - gl_points[:,i].min() for i in range(3)]
        max_range = max(ranges)
        distance = max_range * 2
        
        glu.gluLookAt(x_center, y_center, z_center + distance,
                  x_center, y_center, z_center,
                  0.0, 1.0, 0.0)
        
        # Aplicar rotações
        gl.glTranslatef(x_center, y_center, z_center)
        gl.glRotatef(gl_rotation_x, 1, 0, 0)
        gl.glRotatef(gl_rotation_y, 0, 1, 0)
        gl.glTranslatef(-x_center, -y_center, -z_center)
        
        # Normalizar cores baseado na coordenada Z
        z_min, z_max = gl_points[:,2].min(), gl_points[:,2].max()
        z_range = z_max - z_min if z_max != z_min else 1
        
        # Desenhar pontos coloridos
        gl.glPointSize(3)
        gl.glBegin(gl.GL_POINTS)
        for point in gl_points:
            # Cor baseada na altura (z)
            normalized_z = (point[2] - z_min) / z_range
            color_val = normalized_z * 0.8 + 0.2  # Entre 0.2 e 1.0
            gl.glColor3f(0.2, color_val, 1.0 - color_val * 0.5)
            gl.glVertex3f(point[0], point[1], point[2])
        gl.glEnd()
        
        glut.glutSwapBuffers()
    
    def mouse_motion_3d(x, y):
        global gl_rotation_x, gl_rotation_y, gl_mouse_x, gl_mouse_y, gl_mouse_pressed
        
        if gl_mouse_pressed:
            dx = x - gl_mouse_x
            dy = y - gl_mouse_y
            gl_rotation_y += dx * 0.5
            gl_rotation_x += dy * 0.5
            
            # Limitar rotação vertical
            if gl_rotation_x > 90:
                gl_rotation_x = 90
            if gl_rotation_x < -90:
                gl_rotation_x = -90
                
            glut.glutPostRedisplay()
        
        gl_mouse_x = x
        gl_mouse_y = y
    
    def mouse_click_3d(button, state, x, y):
        global gl_mouse_pressed, gl_mouse_x, gl_mouse_y
        
        if button == glut.GLUT_LEFT_BUTTON:
            if state == glut.GLUT_DOWN:
                gl_mouse_pressed = True
                gl_mouse_x = x
                gl_mouse_y = y
            else:
                gl_mouse_pressed = False
    
    def keyboard_3d(key, x, y):
        global gl_rotation_x, gl_rotation_y
        
        if key == b'r':  # Reset rotação
            gl_rotation_x = 20.0
            gl_rotation_y = 45.0
            glut.glutPostRedisplay()
        elif key == b'q' or key == b'\x1b':  # ESC para sair
            try:
                glut.glutLeaveMainLoop()
            except:
                sys.exit()
    
    def reshape_3d(width, height):
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(45.0, width/height, 1.0, 1000.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
    
    # Inicializar GLUT
    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(*window_size)
    glut.glutInitWindowPosition(100, 100)
    glut.glutCreateWindow(title.encode())
    
    # Configurar OpenGL
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glEnable(gl.GL_POINT_SMOOTH)
    gl.glClearColor(0.1, 0.1, 0.2, 1.0)  # Fundo azul escuro
    
    # Registrar callbacks
    glut.glutDisplayFunc(display_3d)
    glut.glutReshapeFunc(reshape_3d)
    glut.glutMotionFunc(mouse_motion_3d)
    glut.glutMouseFunc(mouse_click_3d)
    glut.glutKeyboardFunc(keyboard_3d)
    
    print(f"=== {title} ===")
    print("Arraste com mouse para rotacionar")
    print("Pressione 'r' para reset, 'q' ou ESC para sair")
    
    glut.glutMainLoop()
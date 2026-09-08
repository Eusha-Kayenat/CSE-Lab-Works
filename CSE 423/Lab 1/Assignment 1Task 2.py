from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

w_size, h_size = 500, 500
dot_list = []       #pos,dir,clr
pace = 0.05       
is_locked = False  
flash_on = False    
flash_clk = 0     

def fix_coords(x_in, y_in):
    return x_in, h_size - y_in
def mouse_clicks(btn, state, mx, my):
    global dot_list, flash_on
    if is_locked:
        return
    if btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        gx, gy = fix_coords(mx, my)
        h_dir = random.choice([-1.0, 1.0])
        v_dir = random.choice([-1.0, 1.0])
        rgb_color = [random.random(), random.random(), random.random()]
        
        dot_list.append([[gx, gy], [h_dir, v_dir], rgb_color])
    elif btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flash_on = not flash_on
        
    glutPostRedisplay()

def engine_loop():
    global dot_list, flash_clk
    if not is_locked:
        if flash_on:
            flash_clk = (flash_clk + 1) % 60 
        for item in dot_list:
            pos = item[0]
            vec = item[1]
            pos[0] += vec[0] * pace
            pos[1] += vec[1] * pace
            
            if pos[0] <= 0 or pos[0] >= w_size:
                vec[0] = -vec[0]
            if pos[1] <= 0 or pos[1] >= h_size:
                vec[1] = -vec[1]
                
        glutPostRedisplay()

def draw_canvas():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, w_size, h_size)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, float(w_size), 0.0, float(h_size), 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_visible = True
    if flash_on and flash_clk > 30:
        draw_visible = False

    for item in dot_list:
        pos, _, rgb = item     
        glPointSize(6.0)
        glBegin(GL_POINTS)

        if draw_visible:
            glColor3f(rgb[0], rgb[1], rgb[2])
        else:
            glColor3f(0.0, 0.0, 0.0)            
        glVertex2f(pos[0], pos[1])
        glEnd()
        
    glutSwapBuffers()

def regular_keys(key, mx, my):
    global is_locked
    if key == b' ':
        is_locked = not is_locked
    glutPostRedisplay()
def arrow_keys(key, mx, my):
    global pace
    if is_locked:
        return      
    if key == GLUT_KEY_UP:
        pace *= 1.5
    elif key == GLUT_KEY_DOWN:
        pace = max(0.005, pace / 1.5)       
    glutPostRedisplay()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(w_size, h_size)
    glutInitWindowPosition(150, 150)
    glutCreateWindow(b"The Amazing Box")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(draw_canvas)
    glutIdleFunc(engine_loop)
    glutKeyboardFunc(regular_keys)
    glutSpecialFunc(arrow_keys)
    glutMouseFunc(mouse_clicks)
    glutMainLoop()
if __name__ == "__main__":
    main()
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

w_size = 600
h_size = 600
sky_fade = 0.0     
wind_run = 0.0      
drops = []        #x,y,speed

for _ in range(150):
    dx = random.uniform(-300, 900)
    dy = random.uniform(0, 800)
    ds = random.uniform(3.8, 6.2)
    drops.append([dx, dy, ds])

def draw_scene():
    glColor3f(0.35, 0.25, 0.1) #brown
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0); glVertex2f(600, 0); glVertex2f(600, 210)
    glVertex2f(0, 0); glVertex2f(600, 210); glVertex2f(0, 210)
    glEnd()

    glColor3f(0.05, 0.4, 0.15) #green
    for t in range(0, 600, 65):
        glBegin(GL_TRIANGLES)
        glVertex2f(t, 185)
        glVertex2f(t + 32, 275)
        glVertex2f(t + 64, 185)
        glEnd()

    glColor3f(0.85, 0.85, 0.85)#GREY
    glBegin(GL_TRIANGLES)
    glVertex2f(140, 95); glVertex2f(460, 95); glVertex2f(460, 285)
    glVertex2f(140, 95); glVertex2f(460, 285); glVertex2f(140, 285)
    glEnd()

    glColor3f(0.65, 0.15, 0.15)#ROOF
    glBegin(GL_TRIANGLES)
    glVertex2f(300, 400)
    glVertex2f(110, 285)
    glVertex2f(490, 285)
    glEnd()

    glColor3f(0.15, 0.35, 0.55)#DOOR
    glBegin(GL_TRIANGLES)
    glVertex2f(255, 95); glVertex2f(345, 95); glVertex2f(345, 215)
    glVertex2f(255, 95); glVertex2f(345, 215); glVertex2f(255, 215)
    glEnd()

    glPointSize(8)#DOOR KNOB
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(335, 155)
    glEnd()

    glColor3f(0.2, 0.5, 0.7)#WINDOW SQUARES
    glBegin(GL_TRIANGLES)
  
    glVertex2f(175, 165); glVertex2f(225, 165); glVertex2f(225, 215)
    glVertex2f(175, 165); glVertex2f(225, 215); glVertex2f(175, 215)
    glVertex2f(375, 165); glVertex2f(425, 165); glVertex2f(425, 215)
    glVertex2f(375, 165); glVertex2f(425, 215); glVertex2f(375, 215)
    glEnd() #GRIDS

    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(175, 190); glVertex2f(225, 190)
    glVertex2f(200, 165); glVertex2f(200, 215)
    glVertex2f(375, 190); glVertex2f(425, 190)
    glVertex2f(400, 165); glVertex2f(400, 215)
    glEnd()

def move_rain():
    global wind_run
    for p in drops:
        p[0] += wind_run * 4.8   
        p[1] -= p[2]             
        if p[1] < 0 or p[0] < -300 or p[0] > 900:
            p[0] = random.uniform(-300, 900)
            p[1] = random.uniform(600, 760)           
    glutPostRedisplay()

def show_screen():
    glClearColor(sky_fade, sky_fade, sky_fade + 0.04, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, w_size, h_size)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600.0, 0.0, 600.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    
    draw_scene()
    glLineWidth(2)
    glBegin(GL_LINES)
    for p in drops:
        if sky_fade > 0.45:#day
            glColor3f(0.15, 0.35, 0.65) #dark blue rain
        else:
            glColor3f(0.75, 0.9, 1.0)  #white rain 
        glVertex2f(p[0], p[1])
        glVertex2f(p[0] + wind_run * 13, p[1] - 15)
    glEnd()
    
    glutSwapBuffers()

def normal_keys(key, mx, my):
    global sky_fade
    if key == b'w' or key == b'W':
        sky_fade = min(0.92, sky_fade + 0.04)
    elif key == b's' or key == b'S':
        sky_fade = max(0.06, sky_fade - 0.04)
    glutPostRedisplay()

def special_keys(key, mx, my):
    global wind_run
    if key == GLUT_KEY_LEFT:
        wind_run -= 0.14    
    elif key == GLUT_KEY_RIGHT:
        wind_run += 0.14   
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(w_size, h_size)
    glutCreateWindow(b"Simulation Scene")
    glutDisplayFunc(show_screen)
    glutIdleFunc(move_rain)
    glutKeyboardFunc(normal_keys)
    glutSpecialFunc(special_keys)  
    glutMainLoop()
if __name__ == "__main__":
    main()
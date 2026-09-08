import sys
import random
import colorsys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

win_w = 500
win_h = 500
diamond_x = random.randint(-220, 220)
diamond_y = 220  
def get_bright_color():
    hue = random.random()
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return [r, g, b]
diamond_clr = get_bright_color()
velocity = 0.3
catcher=0
score = 0
paused = False
dead = False
cheat_mode = False  

def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def find_zone(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    zone_table = {
        (True,  True,  False): 0,
        (True,  True,  True):  1,
        (False, True,  True):  2,
        (False, True,  False): 3,
        (False, False, False): 4, 
        (False, False, True):  5,
        (True,  False, True):  6,
        (True,  False, False): 7,
    }
    return zone_table[(dx >= 0, dy >= 0, abs(dy) > abs(dx))]

def shift_to_zero(zone, x, y):
    transforms = (
        (x, y),    
        (y, x),   
        (y, -x),   
        (-x, y),   
        (-x, -y),  
        (-y, -x), 
        (-y, x),  
        (x, -y)   
    )
    return transforms[zone]

def shift_from_zero(zone, x, y):
    transforms = (
        (x, y),   
        (y, x),    
        (-y, x),   
        (-x, y),  
        (-x, -y), 
        (-y, -x), 
        (y, -x),   
        (x, -y)    
    )
    return transforms[zone]

def draw_grid_line(x1, y1, x2, y2, rgb):
    zone = find_zone(x1, y1, x2, y2)
    start_x, start_y = shift_to_zero(zone, x1, y1)
    end_x, end_y = shift_to_zero(zone, x2, y2)

    if start_x > end_x:
        start_x, end_x = end_x, start_x
        start_y, end_y = end_y, start_y
    dx = end_x - start_x
    dy = end_y - start_y
    d_param = (2 * dy) - dx
    e_step = 2 * dy
    ne_step = 2 * (dy - dx)
    curr_y = start_y

    glColor3f(rgb[0], rgb[1], rgb[2])
    for curr_x in range(int(start_x), int(end_x) + 1):
        orig_x, orig_y = shift_from_zero(zone, curr_x, curr_y)
        draw_pixel(orig_x, orig_y)
        if d_param > 0:
            d_param += ne_step
            curr_y += 1
        else:
            d_param += e_step

C_RED, C_WHITE, C_BLUE, C_AMBER = [1, 0, 0], [1, 1, 1], [0, 0.7, 1], [1, 0.8, 0]

def draw_segments(lines, color):
    for x1, y1, x2, y2 in lines:
        draw_grid_line(x1, y1, x2, y2, color)

def render_catcher():
    x = catcher
    c = C_RED if dead else C_WHITE
    draw_segments([(x-50, -210, x+50, -210), (x-30, -230, x+30, -230), 
                   (x-50, -210, x-30, -230), (x+50, -210, x+30, -230)], c)

def render_diamond():
    if not dead:
        x, y = diamond_x, diamond_y
        draw_segments([(x, y+15, x+12, y), (x+12, y, x, y-15), 
                       (x, y-15, x-12, y), (x-12, y, x, y+15)], diamond_clr)

def render_ui():
    draw_segments([(-220, 220, -195, 220), (-220, 220, -210, 230), (-220, 220, -210, 210)], C_BLUE)
    
    play_icon = [(-10, 235, -10, 205), (-10, 235, 15, 220), (-10, 205, 15, 220)]
    pause_icon = [(-5, 235, -5, 205), (10, 235, 10, 205)]
    freeze = play_icon if paused else pause_icon
    draw_segments(freeze, C_AMBER)
  
    draw_segments([(200, 235, 225, 210), (200, 210, 225, 235)], C_RED)

def reset_diamond():
    global diamond_x, diamond_y, diamond_clr
    diamond_x = random.randint(-220, 220)
    diamond_y = 220
    diamond_clr = get_bright_color() 
def game_loop():
    global diamond_y, dead, score, catcher, velocity
    glClear(GL_COLOR_BUFFER_BIT)
    render_ui()
    render_diamond()
    render_catcher()

    if paused or dead:
        glutSwapBuffers()
        return

    if cheat_mode:
        if catcher < diamond_x:
            catcher = min(200, catcher + 5)
        elif catcher > diamond_x:
            catcher = max(-200, catcher - 5)
    
    diamond_y -= velocity
    if diamond_y < -195:
        captured = abs(diamond_x - catcher) <= 55  #hitboundary
        if captured:
            score += 1
            velocity += 0.08
            print(f"Score: {score}")
            reset_diamond()
        else:
            dead = True
            print(f"Game Over! Score: {score}")
    glutSwapBuffers()

def handle_mouse(button, state, mouse_x, mouse_y):
    global paused, dead, score, velocity, diamond_y, catcher 
    if button != GLUT_LEFT_BUTTON or state != GLUT_DOWN:
        return
    gl_x = mouse_x - (win_w / 2) #opengl coordinate
    gl_y = (win_h / 2) - mouse_y
    if not (200 <= gl_y <= 245):
        return
    if -230 <= gl_x <= -185: 
        score, velocity, dead, paused,catcher = 0, 0.3, False, False,0
        reset_diamond()
        print("Starting Over!")     
    elif -20 <= gl_x <= 25 and not dead:
        paused = not paused      
    elif 190 <= gl_x <= 235:  
        print(f"Goodbye! Score: {score}")
        try:
            glutLeaveMainLoop()
        except:
            sys.exit(0)

def handle_special(key, x, y):
    global catcher
    if paused or dead or cheat_mode:
        return
    move_dir = {GLUT_KEY_LEFT: -25, GLUT_KEY_RIGHT: 25}
    if key in move_dir:
      new_position = catcher+move_dir[key]
      if new_position > 200:
         new_position = 200
      if new_position < -200:
         new_position = -200
    catcher = new_position
    
def handle_keyboard(key, x, y):
    global cheat_mode
    if key in (b'c', b'C', 'c', 'C'):
        cheat_mode = not cheat_mode
        print(f"Cheat Mode {'Activated' if cheat_mode else 'Deactivated'}")

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(win_w, win_h)
    glutCreateWindow(b"Catch the Diamonds!")
    glClearColor(0, 0, 0, 1)
    glOrtho(-250, 250, -250, 250, -1, 1)
    glutDisplayFunc(game_loop)
    glutIdleFunc(game_loop)
    glutMouseFunc(handle_mouse)
    glutSpecialFunc(handle_special)
    glutKeyboardFunc(handle_keyboard)
    glutMainLoop()
import math
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

grid = 10
step = 1
character = [0.0, 1.0, 0.0] 
rotation = 0.0 
bullets = []
enemies = []
kills = 0 
lifeline = 5
missed= 0 
dead= False 
pov = False  
cam_zoom= 13.0  
cam_angle = 0.0
cam_height = 9.0
quadric = None
cheat = False
gun_spin = 0.0
rapidfire = 0

def draw_cube(size=1.0):
    s = size/2.0
    glBegin(GL_QUADS)
    glVertex3f(-s, -s, s); glVertex3f(s, -s, s); glVertex3f(s, s, s); glVertex3f(-s, s, s)
    glVertex3f(-s, -s, -s); glVertex3f(-s, s, -s); glVertex3f(s, s, -s); glVertex3f(s, -s, -s)
    glVertex3f(-s, s, -s); glVertex3f(-s, s, s); glVertex3f(s, s, s); glVertex3f(s, s, -s)   
    glVertex3f(-s, -s, -s); glVertex3f(s, -s, -s); glVertex3f(s, -s, s); glVertex3f(-s, -s, s)
    glVertex3f(s, -s, -s); glVertex3f(s, s, -s); glVertex3f(s, s, s); glVertex3f(s, -s, s)
    glVertex3f(-s, -s, -s); glVertex3f(-s, -s, s); glVertex3f(-s, s, s); glVertex3f(-s, s, -s)
    glEnd()

def render_player():
    glPushMatrix()
    glTranslatef(character[0], character[1], character[2])

    if dead:
        glRotatef(90, 1, 0, 0)  
    glRotatef(rotation, 0, 1, 0)
    glColor3f(0.1, 0.5, 0.8)
    glPushMatrix()
    glScalef(0.6, 1.0, 0.4)
    draw_cube(1.0)
    glPopMatrix()

    glColor3f(0.9, 0.7, 0.5)
    glPushMatrix()
    glTranslatef(0.0, 0.75, 0.0)
    gluSphere(quadric, 0.25, 16, 16)
    glPopMatrix()

    glColor3f(0.9, 0.7, 0.5)
    for arm_off in [-0.4, 0.4]:
        glPushMatrix()
        glTranslatef(arm_off, 0.2, 0.0)
        glRotatef(90, 1, 0, 0)
        gluCylinder(quadric, 0.08, 0.08, 0.5, 12, 12)
        glPopMatrix()

    glColor3f(0.2, 0.2, 0.2)
    for leg_off in [-0.2, 0.2]:
        glPushMatrix()
        glTranslatef(leg_off, -0.5, 0.0)
        glRotatef(90, 1, 0, 0)
        gluCylinder(quadric, 0.09, 0.09, 0.5, 12, 12)
        glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3, 0.1, 0.2)
    glRotatef(gun_spin, 0, 1, 0)
    glColor3f(0.3, 0.3, 0.3)
    gluCylinder(quadric, 0.06, 0.04, 0.7, 12, 12)
    glPopMatrix()
    glPopMatrix()

def render_enemy(e):
    glPushMatrix()
    glTranslatef(e['pos'][0], e['pos'][1], e['pos'][2])
    glScalef(e['scale'], e['scale'], e['scale'])

    glColor3f(0.9, 0.1, 0.1)
    gluSphere(quadric, 0.4, 16, 16)

    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.0)
    gluSphere(quadric, 0.25, 16, 16)
    glPopMatrix()
    glPopMatrix()

def setup_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50.0, 800.0 / 600.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    yaw = rotation + gun_spin
    if pov:
        rad = math.radians(yaw)
        ex = character[0] + math.sin(rad) * 0.4
        ey = character[1] + 0.8
        ez = character[2] + math.cos(rad) * 0.4

        tx = ex + math.sin(rad) * 5.0
        ty = ey
        tz = ez + math.cos(rad) * 5.0

        gluLookAt(ex, ey, ez, tx, ty, tz, 0, 1, 0)
    else:
        rad = math.radians(cam_angle)
        cx = math.sin(rad) * cam_zoom
        cz = math.cos(rad) * cam_zoom
        gluLookAt(cx, cam_height, cz, 0, 0, 0, 0, 1, 0)

def draw_text(x, y, text):
    glColor3f(1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def render_grid_and_walls(): 
    glBegin(GL_QUADS)
    x = -grid
    while x < grid:
        z = -grid
        while z < grid:
            i=x+z
            if i % 2 == 0:
                glColor3f(1.0, 1.0, 1.0)
            else:
                glColor3f(0.8, 0.7, 0.95)
                
            glVertex3f(x, 0.0, z)
            glVertex3f(x + step, 0.0, z)
            glVertex3f(x + step, 0.0, z + step)
            glVertex3f(x, 0.0, z + step)           
            z += step
        x += step
    glEnd()

    walls = [
        (grid, 1.5, 0.0, 0.2, 3.0, grid * 2, (0.8, 0.2, 0.2)),
        (-grid, 1.5, 0.0, 0.2, 3.0, grid * 2, (0.2, 0.8, 0.2)),
        (0.0, 1.5, grid, grid * 2, 3.0, 0.2, (0.2, 0.2, 0.8)),
        (0.0, 1.5, -grid, grid * 2, 3.0, 0.2, (0.8, 0.8, 0.2))
    ]    
    for wx, wy, wz, sx, sy, sz, col in walls:
        glPushMatrix()
        glTranslatef(wx, wy, wz)
        glScalef(sx, sy, sz)
        glColor3f(col[0], col[1], col[2])
        draw_cube(1.0)
        glPopMatrix()

def init():
    global quadric
    quadric = gluNewQuadric()
    reset_game()

def reset_game():
    global character, rotation, gun_spin, bullets, enemies, kills, lifeline, missed, dead, cheat, pov, rapidfire

    character = [0.0, 1.0, 0.0]
    rotation = 0.0
    gun_spin = 0.0
    bullets.clear()
    enemies.clear()
    for i in range(5):
        spawn_enemy()
    kills = 0
    lifeline = 5
    missed = 0
    dead = False
    pov = False
    cheat = False
    rapidfire = 0

def spawn_enemy():
    x = random.uniform(-grid + 1.5, grid - 1.5)
    z = random.uniform(-grid + 1.5, grid - 1.5)

    while math.hypot(x - character[0], z - character[2]) < 4.0:
        x = random.uniform(-grid + 1.5, grid - 1.5)
        z = random.uniform(-grid + 1.5, grid - 1.5)
        
    enemies.append({
        'pos': [x, 0.8, z],
        'scale': 1.0,
        'growth': 0.01
    })

def render_bullet(b):
    glPushMatrix()
    glTranslatef(b['pos'][0], b['pos'][1], b['pos'][2])
    glColor3f(1.0, 0.0, 0.0)
    draw_cube(0.15)
    glPopMatrix()

def spawn_bullet():
    if dead:
        return
    rad = math.radians(rotation + gun_spin)
    bullets.append({
        'pos': [
            character[0] + math.sin(rad) * 0.8,
            character[1] + 0.1,
            character[2] + math.cos(rad) * 0.8
        ],
        'dir': [math.sin(rad) * 0.3, 0.0, math.cos(rad) * 0.3]
    })

def update_game_logic():
    global lifeline, kills, missed, dead, gun_spin, rapidfire

    if dead:
        return
    for b in bullets[:]:
        b['pos'][0] += b['dir'][0]
        b['pos'][2] += b['dir'][2]
        if abs(b['pos'][0]) >= grid or abs(b['pos'][2]) >= grid:
            bullets.remove(b)
            missed += 1
            if missed >= 10:
                dead = True
            continue

        for e in enemies[:]:
            d = math.hypot(b['pos'][0] - e['pos'][0], b['pos'][2] - e['pos'][2])
            if d < 0.6 * e['scale']:
                if b in bullets:
                    bullets.remove(b)
                enemies.remove(e)
                kills += 10
                spawn_enemy()
                break

    speed = 0.003
    for e in enemies:
        dx = character[0] - e['pos'][0]
        dz = character[2] - e['pos'][2]
        dist = math.hypot(dx, dz)

        if dist > 0.1:
            e['pos'][0] += (dx / dist) * speed
            e['pos'][2] += (dz / dist) * speed

        e['scale'] += e['growth']
        if e['scale'] > 1.3 or e['scale'] < 0.7:
           e['growth'] *= -1
        
        if dist < 0.7:
            lifeline-=1
            enemies.remove(e)
            spawn_enemy()
            if lifeline <= 0:
                dead = True
                break

    if cheat:
        gun_spin = (gun_spin + 5.0) % 360.0
        aim= math.radians(rotation + gun_spin)
        if rapidfire > 0:
            rapidfire -= 1
        else:
            for e in enemies:
                ex = e['pos'][0] - character[0]
                ez = e['pos'][2] - character[2]
                e_angle = math.atan2(ex, ez)

                diff = abs((e_angle - aim + math.pi) % (2 * math.pi) - math.pi)
                if diff < math.radians(8.0):
                    spawn_bullet()
                    rapidfire = 20
                    break

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    setup_camera()
    render_grid_and_walls()
    render_player()

    for e in enemies:
        render_enemy(e)
    for b in bullets:
        render_bullet(b)
    
    txt=f"Player Life Remaining: {lifeline} | Game Score: {kills} | Player Bullet Missed: {missed}"
    if dead:
        txt = f"Game is Over. Your Score is {kills}. Press "R" to RESTART the Game."
    draw_text(15, 570, txt)
    glutSwapBuffers()

def idle():
    update_game_logic()
    glutPostRedisplay()

def handle_keyboard(key, x, y):
    global rotation, cheat, pov, gun_spin
    try:
        ch = key.decode('utf-8').lower()
    except:
        ch = str(key).lower()

    if dead:
        if ch == 'r':
            reset_game()
        return

    movement_step = 0.5
    rad = math.radians(rotation)

    if ch == 'w':
        nx = character[0] + math.sin(rad) * movement_step
        nz = character[2] + math.cos(rad) * movement_step
        if abs(nx) < grid - 0.5: 
            character[0] = nx
        if abs(nz) < grid - 0.5: 
            character[2] = nz
    elif ch == 's':
        nx = character[0] - math.sin(rad) * movement_step
        nz = character[2] - math.cos(rad) * movement_step
        if abs(nx) < grid - 0.5: 
            character[0] = nx
        if abs(nz) < grid - 0.5: 
            character[2] = nz
    elif ch == 'a':
        rotation = (rotation + 5.0) % 360.0
    elif ch == 'd':
        rotation = (rotation - 5.0) % 360.0
    elif ch == 'c':
        cheat = not cheat
        if not cheat:
            gun_spin = 0.0
    elif ch == 'v':
        if cheat:
            pov = not pov
    elif ch == 'r':
        reset_game()

def handle_special(key, x, y):
    global cam_zoom, cam_angle
    if key == GLUT_KEY_UP:
        cam_zoom = max(5.0, cam_zoom - 0.5)
    elif key == GLUT_KEY_DOWN:
        cam_zoom = min(30.0, cam_zoom + 0.5)
    elif key == GLUT_KEY_LEFT:
        cam_angle -= 3.0
    elif key == GLUT_KEY_RIGHT:
        cam_angle += 3.0

def handle_mouse(button, state, x, y):
    global pov
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            spawn_bullet()
        elif button == GLUT_RIGHT_BUTTON:
            pov = not pov

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"3D Arena Shooter")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(handle_keyboard)
    glutSpecialFunc(handle_special)
    glutMouseFunc(handle_mouse)
    glutIdleFunc(idle)
    glutMainLoop()
if __name__ == "__main__":
    main()
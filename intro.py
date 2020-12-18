balloon = Actor('balloon')

WIDTH = 1683
HEIGHT = 1000

balloon.pos = 0, HEIGHT/2

def update():
    balloon.left += 3
    if balloon.left > WIDTH / 2 :
        balloon.top += 3

def draw():
    screen.fill((212, 111, 56))
    balloon.draw()
    
def set_balloon_happy():
    sounds.missed.play()
    balloon.image = 'balloon_missed'
    clock.schedule_unique(set_balloon_normal, 0.5)
    
def set_balloon_hurt():
    balloon.image = 'balloon_hit'
    sounds.hit.play()
    clock.schedule_unique(set_balloon_normal, 0.5)

def set_balloon_normal():
    balloon.image = 'balloon'
    
def on_mouse_down(pos):
    if balloon.collidepoint(pos):
        set_balloon_hurt()
    else:
       set_balloon_happy()


from random import randint

WIDTH = 1683
HEIGHT = 1000

# Tuk se zapiswat dwizhestite se obekti
actors = []

class MovableObject(Actor):

    def __init__(self, image, pos=None, anchor=None, **kwargs):
        super().__init__(image, pos, anchor)
        self.dx = randint(-3,3)
        self.dy = randint(-3,3)
        self.replicable = randint(0, 1)
        self.newPosition()

    def newPosition(self):
        xpos = randint(0, WIDTH - 1)
        ypos = randint(0, HEIGHT - 1)

        self.top = ypos
        self.left = xpos

    def update(self):
        self.left = self.left + self.dx
        self.top = self.top + self.dy

        if self.left < 0:
            self.newPosition()
        if self.left > WIDTH:
            self.newPosition()
        if self.top < 0:
            self.newPosition()
        if self.bottom > HEIGHT:
            self.newPosition()

    def set_happy(self):
        sounds.missed.play()
        self.image = 'balloon_missed'
        clock.schedule_unique(self.set_normal, 0.5)

    def set_hurt(self):
        self.image = 'balloon_hit'
        sounds.hit.play()
        if self.replicable:
            actors.append(MovableObject('balloon'))
        clock.schedule_unique(self.set_normal, 0.5)

    def set_normal(self):
        self.image = 'balloon'


# Tuk e osnownvata logica

for i in range(3):
    actors.append(MovableObject('balloon'))


def update():
    for actor in actors:
        actor.update()

def draw():
    screen.fill((212, 111, 56))
    for actor in actors:
        actor.draw()

def on_mouse_down(pos):
    for actor in actors:
        if actor.collidepoint(pos):
            actor.set_hurt()
        # else:
        #    actor.set_happy()

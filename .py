def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_circle((800 / 2, 600 / 2), 30, color=(0, 0, 255))
    import math

ship_x = 800 / 2
ship_y = 600 / 2
ship_angle = 0

def update(dt):
    global ship_angle

    if keyboard.right:
        ship_angle += 10 * dt

def draw():
    screen.fill((0, 0, 0))

    screen.draw.filled_circle((ship_x, ship_y), 30, color=(0, 0, 255))

    ship_circle_distance = 20
    screen.draw.filled_circle((
        ship_x + math.cos(ship_angle) * ship_circle_distance,
        ship_y + math.sin(ship_angle) * ship_circle_distance),
        5, color=(0, 255, 255)
    )

    # Temporary
    screen.draw.text('ship_angle: ' + str(ship_angle), (0, 0))
    def update(dt):
    global ship_angle

    turn_speed = 10

    if keyboard.right:
        ship_angle += turn_speed * dt

    if keyboard.left:
        ship_angle -= turn_speed * dt
        ef update(dt):
    # etc.

    ship_angle %= 2 * math.pi
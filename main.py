tiles.set_current_tilemap(tilemap("""level1"""))
def on_a_pressed():
    mySprite.vy += -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    mySprite.set_image(assets.image("""
        myImage0
    """))
    pause(200)
    mySprite.set_image(assets.image("""
        myImage8
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    mySprite.set_image(assets.image("""
        myImage1
    """))
    pause(200)
    mySprite.set_image(assets.image("""
        myImage7
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    myImage4
"""), SpriteKind.player)
scene.set_background_color(9)
controller.move_sprite(mySprite, 100, 0)
mySprite.vy = 300

controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy += -150
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`myImage0`)
    pause(200)
    mySprite.setImage(assets.image`myImage8`)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`myImage1`)
    pause(200)
    mySprite.setImage(assets.image`myImage7`)
})
let mySprite: Sprite = null
tiles.setCurrentTilemap(tilemap`level1`)
mySprite = sprites.create(assets.image`myImage4`, SpriteKind.Player)
scene.setBackgroundColor(9)
controller.moveSprite(mySprite, 100, 0)
mySprite.vy = 300

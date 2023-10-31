# St. Plagueys Game

# Info
#game.splash("St. Plagueys")
#name = game.ask_for_string("Enter name:")
name = "Diya"


# Setup

# Create Tilemap
tiles.set_current_tilemap(tilemap("""test1"""))

# Create Sprites
player_character = sprites.create(img("""
    . . . . . f f 4 4 f f . . . . .
    . . . . f 5 4 5 5 4 5 f . . . .
    . . . f e 4 5 5 5 5 4 e f . . .
    . . f b 3 e 4 4 4 4 e 3 b f . .
    . . f 3 3 3 3 3 3 3 3 3 3 f . .
    . f 3 3 e b 3 e e 3 b e 3 3 f .
    . f 3 3 f f e e e e f f 3 3 f .
    . f b b f b f e e f b f b b f .
    . f b b e 1 f 4 4 f 1 e b b f .
    f f b b f 4 4 4 4 4 4 f b b f f
    f b b f f f e e e e f f f b b f
    . f e e f b d d d d b f e e f .
    . . e 4 c d d d d d d c 4 e . .
    . . e f b d b d b d b b f e . .
    . . . f f 1 d 1 d 1 d f f . . .
    . . . . . f f b b f f . . . . .
"""), SpriteKind.player)
player_character.say_text(name)
burger = sprites.create(img("""
    . . . . c c c b b b b b . . . .
    . . c c b 4 4 4 4 4 4 b b b . .
    . c c 4 4 4 4 4 5 4 4 4 4 b c .
    . e 4 4 4 4 4 4 4 4 4 5 4 4 e .
    e b 4 5 4 4 5 4 4 4 4 4 4 4 b c
    e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e
    e b b 4 4 4 4 4 4 4 4 4 4 4 b e
    . e b 4 4 4 4 4 5 4 4 4 4 b e .
    8 7 e e b 4 4 4 4 4 4 b e e 6 8
    8 7 2 e e e e e e e e e e 2 7 8
    e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e
    e c 6 7 6 6 7 7 7 6 6 7 6 c c e
    e b e 8 8 c c 8 8 c c c 8 e b e
    e e b e c c e e e e e c e b e e
    . e e b b 4 4 4 4 4 4 4 4 e e .
    . . . c c c c c e e e e e . . .
"""), SpriteKind.food)
duck = sprites.create(assets.image("""duck6"""), SpriteKind.enemy)
duck1 = sprites.create(assets.image("""duck6"""), SpriteKind.enemy)
duck2 = sprites.create(assets.image("""duck6"""), SpriteKind.enemy)
duck3 = sprites.create(assets.image("""duck6"""), SpriteKind.enemy)

# Place Sprites
tiles.place_on_tile(burger, tiles.get_tile_location(0, 10))
tiles.place_on_tile(duck, tiles.get_tile_location(0, 15))
tiles.place_on_tile(duck1, tiles.get_tile_location(0, 14))
tiles.place_on_tile(duck2, tiles.get_tile_location(0, 13))
tiles.place_on_tile(duck3, tiles.get_tile_location(0, 0))

# Set Camera
scene.camera_follow_sprite(player_character)


# Functions

# Player and Food Overlap
def on_overlap_player_food(sprite, otherSprite):
    sprite.start_effect(effects.spray)
    otherSprite.start_effect(effects.fire)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap_player_food)

# Player and Enemy Overlap
def on_overlap_player_enemy(sprite, otherSprite):
    load_level1(player_character)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap_player_enemy)
controller.move_sprite(player_character)

# Change Tilemap and Destroy Sprites
def load_level1(player):
    tiles.set_current_tilemap(tilemap("""level0"""))
    sprites.destroy(burger)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    tiles.place_on_tile(player, tiles.get_tile_location(0, 0))
    return


# Game Start

# Intro
game.set_dialog_cursor(img("""
    . . . . . . . 6 . . . . . . . .
    . . . . . . 8 6 6 . . . 6 8 . .
    . . . e e e 8 8 6 6 . 6 7 8 . .
    . . e 2 2 2 2 e 8 6 6 7 6 . . .
    . e 2 2 4 4 2 7 7 7 7 7 8 6 . .
    . e 2 4 4 2 6 7 7 7 6 7 6 8 8 .
    e 2 4 5 2 2 6 7 7 6 2 7 7 6 . .
    e 2 4 4 2 2 6 7 6 2 2 6 7 7 6 .
    e 2 4 2 2 2 6 6 2 2 2 e 7 7 6 .
    e 2 4 2 2 4 2 2 2 4 2 2 e 7 6 .
    e 2 4 2 2 2 2 2 2 2 2 2 e c 6 .
    e 2 2 2 2 2 2 2 4 e 2 e e c . .
    e e 2 e 2 2 4 2 2 e e e c . . .
    e e e e 2 e 2 2 e e e c . . . .
    e e e 2 e e c e c c c . . . . .
    . c c c c c c c . . . . . . . .
"""))
text = name + " is at school today and it is a normal day for " + name + "until a bad chemistry teacher did something silly..."
game.show_long_text(text, DialogLayout.BOTTOM)
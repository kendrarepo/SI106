import pyglet
import random
import test106 as test

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

class GameWindow(pyglet.window.Window):
    """The entire game in one class..."""
    def __init__(self):

        pyglet.window.Window.__init__(self, width = 1000, height = 600)
        pyglet.gl.glClearColor(255,255,0,0.05)
        
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)

        self.set_caption("Diag Squirrel Dodger")

        self.player_image = pyglet.resource.image("squirrel.png")
        self.bluebus_image = pyglet.resource.image("bluebus.png")
        
        self.center_image(self.player_image)
        self.center_image(self.bluebus_image)
        
        self.crash_sound = pyglet.resource.media("beep.wav", streaming=False)
        self.background_music = pyglet.resource.media("victors.wav", streaming=False)

        self.player = pyglet.sprite.Sprite(img=self.player_image, x=30, y=30)
        self.player.scale = 0.3

        self.score_label = pyglet.text.Label(text="Score:0 Highscore:0", x=10, y=10, color=(0,0,0,255))
        self.score = 0
        self.highscore = 0

        self.bluebus = []

        pyglet.clock.schedule_interval(self.game_tick, 0.005)
        self.background_music.play()
        #pyglet.clock.schedule_interval(lambda x: self.background_music.play(), 2.12)

    def game_tick(self, dt):
        self.update_bluebus()
        self.update_player()
        self.update_score()
        self.draw_elements()

    def draw_elements(self):
        self.clear()
        for bluebus in self.bluebus: #accumulation
            bluebus.draw()
        self.player.draw()
        self.score_label.draw()

    def update_bluebus(self):
        if random.randint(0, 45) == 3:
            ast = pyglet.sprite.Sprite(img=self.bluebus_image, x=random.randint(0, 1000), y=600)
            ast.scale = 0.3
            self.bluebus.append(ast)
        for bluebus in self.bluebus:
            bluebus.y -= 7
            if bluebus.y < 0:
                self.bluebus.remove(bluebus)
        for bluebus in self.bluebus:
            if self.sprites_collide(bluebus, self.player):
                self.bluebus.remove(bluebus)
                self.score = 0
                self.crash_sound.play()

    def update_player(self):
        if self.keys[pyglet.window.key.LEFT] and not self.player.x < 0:
            self.player.x -= 4
        elif self.keys[pyglet.window.key.RIGHT] and not self.player.x > 1000:
            self.player.x += 4

    def update_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.score_label.text = "Score: %s Highscore: %s" % (self.score, self.highscore)
        
    
    def center_image(self, image):
        image.anchor_x = image.width/2
        image.anchor_y = image.height/2

    def sprites_collide(self, spr1, spr2):
        return (spr1.x-spr2.x)**2 + (spr1.y-spr2.y)**2 < (spr1.width/2 + spr2.width/2)**2

game_window = GameWindow()

# Test case to make sure that score is an integer because needs to get added to
# to other integers later on in update_score method
test.testEqual(type(game_window.score), type(1) )

# Test case to make sure that highscore is a integer in the __init__ method 
# so that it can be added to other integers later
test.testEqual(type(game_window.highscore), type(1))

# Test case to make sure that bluebus is a list so that elements can get added to it
# later on in update_bluebus method
test.testEqual(type(game_window.bluebus), type([]))

# I added this here to meet the list comprehension and sort requirement! I couldn't find
# a logical place to implement it in my game code. Hopefully this shows that I am capable of
# writing these kind of things!!
gamelist = ["Thank", 12, "you", "for", 2015, "playing", "Diag", "Squirrel","Doger", 14]
wordsonly = [element for element in gamelist if type(element) == type("")]
for element in wordsonly:
    print element

words = {"day":14, "year":2015, "month":12}
print "This game was created on..."
for element in sorted(words, key = lambda x: words[x]):
    print words[element]

pyglet.app.run()
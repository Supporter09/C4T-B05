from pyglet.media import Source, Player, load

player = Player()
source = load('Centuries - Fall out boy.mp3')
player.queue(source)
player.play()
while True:
  input('Press any key to exit')
  break
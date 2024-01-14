import pygame

# Initialize pygame
pygame.init()

# Set up the mixer for playing sounds
pygame.mixer.init()

# Load sounds
b1 = pygame.mixer.Sound("Notes\B1.wav")

c2 = pygame.mixer.Sound("Notes\C2.wav")
cs2 = pygame.mixer.Sound("Notes\C#2.wav")
d2 = pygame.mixer.Sound("Notes\D2.wav")
ds2 = pygame.mixer.Sound("Notes\D#2.wav")
e2 = pygame.mixer.Sound("Notes\E2.wav")
f2 = pygame.mixer.Sound("Notes\F2.wav")
fs2 = pygame.mixer.Sound("Notes\F#2.wav")
g2 = pygame.mixer.Sound("Notes\G2.wav")
gs2 = pygame.mixer.Sound("Notes\G#2.wav")
a2 = pygame.mixer.Sound("Notes\A2.wav")
as2 = pygame.mixer.Sound("Notes\A#2.wav")
b2 = pygame.mixer.Sound("Notes\B2.wav")

c3 = pygame.mixer.Sound("Notes\C3.wav")
cs3 = pygame.mixer.Sound("Notes\C#3.wav")
d3 = pygame.mixer.Sound("Notes\D3.wav")
ds3 = pygame.mixer.Sound("Notes\D#3.wav")
e3 = pygame.mixer.Sound("Notes\E3.wav")
f3 = pygame.mixer.Sound("Notes\F3.wav")
fs3 = pygame.mixer.Sound("Notes\F#3.wav")
g3 = pygame.mixer.Sound("Notes\G3.wav")
gs3 = pygame.mixer.Sound("Notes\G#3.wav")
a3 = pygame.mixer.Sound("Notes\A3.wav")
as3 = pygame.mixer.Sound("Notes\A#3.wav")
b3 = pygame.mixer.Sound("Notes\B3.wav")

c4 = pygame.mixer.Sound("Notes\C4.wav")
cs4 = pygame.mixer.Sound("Notes\C#4.wav")
d4 = pygame.mixer.Sound("Notes\D4.wav")
ds4 = pygame.mixer.Sound("Notes\D#4.wav")
e4 = pygame.mixer.Sound("Notes\E4.wav")
f4 = pygame.mixer.Sound("Notes\F4.wav")
fs4 = pygame.mixer.Sound("Notes\F#4.wav")
g4 = pygame.mixer.Sound("Notes\G4.wav")
gs4 = pygame.mixer.Sound("Notes\G#4.wav")
a4 = pygame.mixer.Sound("Notes\A4.wav")
as4 = pygame.mixer.Sound("Notes\A#4.wav")
b4 = pygame.mixer.Sound("Notes\B4.wav")

c5 = pygame.mixer.Sound("Notes\C5.wav")
cs5 = pygame.mixer.Sound("Notes\C#5.wav")
d5 = pygame.mixer.Sound("Notes\D5.wav")
ds5 = pygame.mixer.Sound("Notes\D#5.wav")
e5 = pygame.mixer.Sound("Notes\E5.wav")
f5 = pygame.mixer.Sound("Notes\F5.wav")
fs5 = pygame.mixer.Sound("Notes\F#5.wav")
g5 = pygame.mixer.Sound("Notes\G5.wav")
gs5 = pygame.mixer.Sound("Notes\G#5.wav")
a5 = pygame.mixer.Sound("Notes\A5.wav")
as5 = pygame.mixer.Sound("Notes\A#5.wav")
b5 = pygame.mixer.Sound("Notes\B5.wav")

c6 = pygame.mixer.Sound("Notes\C6.wav")


# Set up mixer channels
channels = []  # Adjust based on your needs
for i in range(8):
	channels.append(pygame.mixer.Channel(i))

key_sound_mapping = {
	pygame.K_1: c2,
	pygame.K_2: cs2,
	pygame.K_3: d2,
	pygame.K_4: ds2,
	pygame.K_5: e2,
	pygame.K_6: f2,
	pygame.K_7: fs2,
	pygame.K_8: g2,
	pygame.K_9: gs2,
	pygame.K_0: a2,
	pygame.K_MINUS: as2,
	pygame.K_EQUALS: b2,

	pygame.K_TAB: c3,
	pygame.K_q: cs3,
	pygame.K_w: d3,
	pygame.K_e: ds3,
	pygame.K_r: e3,
	pygame.K_t: f3,
	pygame.K_y: fs3,
	pygame.K_u: g3,
	pygame.K_i: gs3,
	pygame.K_o: a3,
	pygame.K_p: as3,
	pygame.K_LEFTBRACKET: b3,

	pygame.K_CAPSLOCK: c4,
	pygame.K_a: cs4,
	pygame.K_s: d4,
	pygame.K_d: ds4,
	pygame.K_f: e4,
	pygame.K_g: f4,
	pygame.K_h: fs4,
	pygame.K_j: g4,
	pygame.K_k: gs4,
	pygame.K_l: a4,
	pygame.K_SEMICOLON: as4,
	pygame.K_QUOTE: b4,

	pygame.K_LSHIFT: c5,
	pygame.K_z: cs5,
	pygame.K_x: d5,
	pygame.K_c: ds5,
	pygame.K_v: e5,
	pygame.K_b: f5,
	pygame.K_n: fs5,
	pygame.K_m: g5,
	pygame.K_COMMA: gs5,
	pygame.K_PERIOD: a5,
	pygame.K_SLASH: as5,
	pygame.K_RSHIFT: b5
}

# Set up the display
pygame.display.set_caption("Raspiano Music")
display = pygame.display.set_mode((1300, 500))
display.fill((255,255,255))
key = pygame.image.load('Images\Key.png')
display.blit(key, (100, 0))
display.blit(key, (200, 0))
display.blit(key, (300, 0))
display.blit(key, (400, 0))
display.blit(key, (500, 0))
display.blit(key, (600, 0))
display.blit(key, (700, 0))
display.blit(key, (800, 0))
display.blit(key, (900, 0))
display.blit(key, (1000, 0))
display.blit(key, (1100, 0))
pygame.display.flip()

# Main loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN and event.key in key_sound_mapping:
			sound_to_play = key_sound_mapping[event.key]

			# Play the sound on all available channels with no delay
			for channel in channels:
				if not channel.get_busy():
					channel.play(sound_to_play)
					break

	pygame.time.delay(10)  # Add a small delay to ensure note is played for correct duration

# Clean up pygame
pygame.quit()
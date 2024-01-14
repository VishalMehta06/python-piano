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
		
# Define the key-to-sound mapping
key_sound_mapping = {
	pygame.K_5: 	[[b1, c2, cs2],		[b2, c3, cs3],		[b3, c4, cs4],		[b4, c5, cs5]	],
	pygame.K_6: 	[[cs2, d2, ds2],	[cs3, d3, ds3],		[cs4, d4, ds4],		[cs5, d5, ds5]	],
	pygame.K_7: 	[[ds2, e2, f2],		[ds3, e3, f3],		[ds4, e4, f4],		[ds5, e5, f5]	],
	pygame.K_8: 	[[e2, f2, fs2],		[e3, f3, fs3],		[e4, f4, fs4],		[e5, f5, fs5]	],
	pygame.K_9: 	[[fs2, g2, gs2],	[fs3, g3, gs3],		[fs4, g4, gs4],		[fs5, g5, gs5]	],
	pygame.K_0: 	[[gs2, a2, as2],	[gs3, a3, as3],		[gs4, a4, as4],		[gs5, a5, as5]	],
	pygame.K_MINUS: [[as2, b2, c3],		[as3, b3, c4],		[as4, b4, c5],		[as5, b5, c6]	]
}
key_octave_mapping = {
	pygame.K_1: 2,
	pygame.K_2: 3,
	pygame.K_3: 4,
	pygame.K_4: 5
}
half_step_mapping = {
	pygame.K_LCTRL: 0,
	pygame.K_LSHIFT: 2,
	pygame.K_CAPSLOCK: 1
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
octave = 0
half_step = 1
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			# Check if the pressed key has a sound mapping
			if event.key in key_octave_mapping:
				# Make the new octave the correct index
				octave = key_octave_mapping[event.key] - 2

			elif event.key in half_step_mapping:
				# Make the sharp/flat status correct
				half_step = half_step_mapping[event.key]

			elif event.key in key_sound_mapping:
				sound_to_play = key_sound_mapping[event.key][octave][half_step]
				# Adjust the sharp/flat status to default
				half_step = 1

				# Play the sound on all available channels with no delay
				for channel in channels:
					if not channel.get_busy():
						channel.play(sound_to_play)
						break  # Play on the first available channel

	pygame.time.delay(10)  # Add a small delay to ensure note is played for correct duration

# Clean up pygame
pygame.quit()
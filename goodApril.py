import sys
import random
import pygame
from pygame.locals import *

WIDTH, HEIGHT = 840, 840
BACKGROUND = (100, 191, 255)

def button(text, x, y, w, h, color, screen):
	pygame.draw.rect(screen, color, (x, y, w, h))
	font = pygame.font.Font('pack/simkai.ttf', 20)
	textRender = font.render(text, True, (0, 0, 0))
	textRect = textRender.get_rect()
	textRect.center = ((x+w/2), (y+h/2))	
	screen.blit(textRender, textRect)


def title(text, screen, scale, color=( 255,0,255)):
	font = pygame.font.Font('pack/simkai.ttf', WIDTH//(len(text)*2))
	textRender = font.render(text, True, color)
	textRect = textRender.get_rect()
	textRect.midtop = (WIDTH/scale[0], HEIGHT/scale[1])
	screen.blit(textRender, textRect)

def get_random_pos():
	x, y = random.randint(20, 620), random.randint(20, 460)
	return x, y

    
def show_like_interface(text, screen, color=( 	255,0,255)):
	screen.fill(BACKGROUND)
	font = pygame.font.Font('pack/simkai.ttf', WIDTH//(len(text)))
	textRender = font.render(text, True, color)
	textRect = textRender.get_rect()
	textRect.midtop = (WIDTH/2, HEIGHT/2)
	screen.blit(textRender, textRect)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()



def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
	pygame.display.set_caption('Be my lover!')
	clock = pygame.time.Clock()
	# pygame.mixer.music.load('D:/Backup/桌面/半阳.mp3')
	pygame.mixer.music.load('pack/Bruno Mars - Treasure.mp3')
	pygame.mixer.music.play(-1, 20.8)
	pygame.mixer.music.set_volume(0.40)
	unlike_pos_x = 420
	unlike_pos_y = 600
	unlike_pos_width = 100
	unlike_pos_height = 50
	like_pos_x = 320
	like_pos_y = 600
	like_pos_width = 100
	like_pos_height = 50
	running = True
	like_color = (255, 192, 203)

	while running:
		screen.fill(BACKGROUND)
		# img = pygame.image.load("D:/Backup/桌面/455.png")
		img = pygame.image.load("pack/nice.jpg")
		imgRect = img.get_rect()
		imgRect.midtop = WIDTH//2, HEIGHT//4
		screen.blit(img, imgRect)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if mouse_pos[0] < like_pos_x+like_pos_width+5 and mouse_pos[0] > like_pos_x-5 and\
					mouse_pos[1] < like_pos_y+like_pos_height+5 and mouse_pos[1] > like_pos_y-5:
					like_color = BACKGROUND
					running = False
		mouse_pos = pygame.mouse.get_pos()
		if mouse_pos[0] < unlike_pos_x+unlike_pos_width+5 and mouse_pos[0] > unlike_pos_x-5 and\
			mouse_pos[1] < unlike_pos_y+unlike_pos_height+5 and mouse_pos[1] > unlike_pos_y-5:
			while True:
				unlike_pos_x, unlike_pos_y = get_random_pos()
				if mouse_pos[0] < unlike_pos_x+unlike_pos_width+5 and mouse_pos[0] > unlike_pos_x-5 and\
					mouse_pos[1] < unlike_pos_y+unlike_pos_height+5 and mouse_pos[1] > unlike_pos_y-5:
					continue
				break
		title('琴琴，我喜欢你好久了~', screen, scale=[2, 10])
		title('做我女朋友好不好呀￣ω￣=', screen, scale=[2, 6])
		button('好呀', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen)
		button('滚蛋', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, (255,215,0), screen)
		pygame.display.flip()
		pygame.display.update()
		clock.tick(60)
	show_like_interface('^V^我就知道你也喜欢我^@^', screen, color=(255,0,255))

    
    
if __name__ == "__main__":
	main()
	input("good morning")





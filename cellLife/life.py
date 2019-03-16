import pygame
from random import randint

pygame.init()
win=pygame.display.set_mode((550,550))
pygame.display.set_caption('micro Life')
game=pygame.Surface((500,500))

clock=pygame.time.Clock()

win.fill((100,0,100))
pygame.draw.rect(win,(255,0,0),(5,5,530,530),5)
pygame.draw.rect(win,(255,0,0),(15,15,530,530),5)
pygame.display.update()

def restart():
	global stoper,painting,pole,copypole
	stoper=100
	painting=-1
	pole=[[0] * 25 for i in range(25)]
	copypole=pole

def draw():
	global pole
	game.fill((0,0,0))
	
	for yy in range(0,500,20):
		pygame.draw.line(game,(0,10,240),(0,yy),(500,yy),1)
	for xx in range(0,500,20):
		pygame.draw.line(game,(0,10,240),(xx,0),(xx,500),1)
	
	for xx in range(25): 
		for yy in range(25):
			if painting==1: smena(xx,yy)
			if pole[xx][yy]==2: pygame.draw.rect(game,(0,255,0),(xx*20+1,yy*20+1,20,20))
			elif pole[xx][yy]==10: pygame.draw.rect(game,(0,0,255),(xx*20+1,yy*20+1,20,20))
			elif pole[xx][yy]==1: pygame.draw.rect(game,(255,255,0),(xx*20+1,yy*20+1,20,20))
			elif pole[xx][yy]==5: pygame.draw.rect(game,(0,205,255),(xx*20+1,yy*20+1,20,20))
		
	pygame.time.delay(int(stoper)) 
	pole=copypole
	win.blit(game,(25,25))
	pygame.display.update()
	
def paint(x,y):
	if 25<x<525 and 25<y<525:
		if e.button==1:
			pole[(x-25)//20][(y-25)//20]=2
		elif e.button==3:
			pole[(x-25)//20][(y-25)//20]=10

def smena(xx,yy):
	k=pole[xx][yy]
	if xx>0: k+=pole[xx-1][yy]
	if yy>0: k+=pole[xx][yy-1]
	if yy<24: k+=pole[xx][yy+1]
	if xx<24: k+=pole[xx+1][yy]

	if 2*(k-1)//10>k%10-1 and 13<k<43 : copypole[xx][yy]=10
	elif 2*(k-1)//10<=k%10-1 and 3<k and k%10<9: copypole[xx][yy]=2
	else: copypole[xx][yy]=(randint(0,1001)//1000)*2*5**((randint(0,15)+4)//10)

	if (xx%24==0 or yy%24==0) and copypole[xx][yy]>0: copypole[xx][yy]=copypole[xx][yy]//2**(copypole[xx][yy]%2+1)


play=True
restart()

while play: 
	clock.tick(30)

	for e in pygame.event.get():
		if e.type==pygame.QUIT: #проверка выхода
				play=False
		if e.type==pygame.KEYDOWN:
			if e.key==pygame.K_ESCAPE: play=False
			if e.key==pygame.K_SPACE:
				painting*=-1
				stoper=100
			if e.key==pygame.K_r: restart()
		if painting==-1 and e.type==pygame.MOUSEBUTTONDOWN:
			xy=pygame.mouse.get_pos()
			paint(xy[0],xy[1])
	
	if stoper>1:stoper-=0.5

	draw()
	
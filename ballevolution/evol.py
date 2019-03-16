import pygame
from random import randint, randrange

pygame.init()
win=pygame.display.set_mode((550,550))
pygame.display.set_caption('micro Life2')
game=pygame.Surface((500,500))

win.fill((150,150,150))

clock=pygame.time.Clock()

class kletka():
	def __init__(self,x,y,type,r): # type 1=damage type 2= defens
		self.x=x
		self.y=y
		self.r=r
		self.type=type
		self.velx=randint(0,(3-type)*10)*randrange(-1,2,2)
		self.vely=((((3-type)*10)**2-self.velx**2)**0.5)*randrange(-1,2,2)
	
	def drawkletka(self):
		pygame.draw.circle(game,(255-(self.type-1)*255,0,(self.type-1)*255),(int(self.x),int(self.y)),int(abs(self.r)/10),0)
	
class eat():
	def __init__(self,x=0,y=0):
		if x==0 and y==0: x=randint(25,475); y=randint(25,475)
		self.x=x
		self.y=y
		self.r=randint(10,200)
		
	def draweat(self):
		pygame.draw.circle(game,(255,255,0),(int(self.x),int(self.y)),int(self.r/10),0)
	
		
def otskok():
		if telo.x>500-telo.r/10-telo.velx or telo.x<telo.r/10-telo.velx: telo.velx*=(-1)
		if telo.y>500-telo.r/10-telo.vely or telo.y<telo.r/10-telo.vely: telo.vely*=(-1)

def stolknovenie(index):
	for telo2 in kletki:
		if index<kletki.index(telo2) and ((telo.x-telo2.x)**2+(telo.y-telo2.y)**2<((telo.r+telo2.r)/10)**2) and telo.type!=telo2.type:
			if telo.r>telo2.r: telo.r+=telo.type*3+5; telo2.r-=telo.type*3+5
			if telo.r<telo2.r: telo.r-=telo2.type*3+5; telo2.r+=telo2.type*3+5

def paint(x,y):
	if 45<x<505 and 45<y<505:
		if e.button==1:
			kletki.append(kletka(x-25,y-25,1,200))
		elif e.button==3:
			kletki.append(kletka(x-25,y-25,2,300))

def draw():
	game.fill((0,0,0))
	for telo in kletki:
		telo.drawkletka()
	for eat in eda:
		eat.draweat()
	
	win.blit(game,(25,25))
	pygame.display.update()

def restart():
	global painting,kletki,eda
	painting=-1
	kletki=[]
	eda=[]
	
play=True
restart()
stoper=50
pygame.key.set_repeat(200,50)

while play:
	clock.tick(30)

	for e in pygame.event.get():
		if e.type==pygame.QUIT: play=False
		if e.type==pygame.KEYDOWN:
			if e.key==pygame.K_ESCAPE: play=False
			if e.key==pygame.K_SPACE:
				painting*=-1
			if e.key==pygame.K_r: restart()
			if e.key==pygame.K_UP and stoper<200: stoper-=2
			if e.key==pygame.K_DOWN and stoper>0: stoper+=2
		if painting==-1 and e.type==pygame.MOUSEBUTTONDOWN:
			xy=pygame.mouse.get_pos()
			paint(xy[0],xy[1])

	if painting==1:
		for telo in kletki: 
			for eatt in eda:
				if ((telo.x-eatt.x)**2+(telo.y-eatt.y)**2<((telo.r+eatt.r)/10)**2):
					telo.r+=eatt.r
					eda.pop(eda.index(eatt))
			otskok()
			stolknovenie(kletki.index(telo))
			telo.r-=(3-telo.type)*telo.r//100+(telo.r%100)//50+2     
			if telo.r<2: 
				eda.append(eat(telo.x,telo.y))
				kletki.pop(kletki.index(telo))
				continue
			elif telo.r>(telo.type+1)*500: 
				telo.r=int(telo.r/2)
				kletki.append(kletka(telo.x,telo.y,telo.type,telo.r))

			telo.x+=telo.velx
			telo.y+=telo.vely
	
		if randint(0,121)//100==1: eda.append(eat())
	
	
	draw()
	pygame.time.delay(int(stoper)) 
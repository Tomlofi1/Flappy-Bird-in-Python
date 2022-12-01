import pygame


class Obj(pygame.sprite.Sprite):

    def __init__(self, image, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y


class Coin(Obj):

    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

        self.ticks = 0

    def update(self, *args):
        self.anim()
        self.move()

    def anim(self):
        self.ticks = (self.ticks + 1) % 6
        self.image = pygame.image.load("assets/" + str(self.ticks) + ".png")

    def move(self):
        self.rect[0] -= 4

        if self.rect[0] <= -100:
            self.kill()


class Pipe(Obj):

    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

    def update(self, *args):
        self.rect[0] -= 4

        if self.rect[0] <= -100:
            self.kill()


class Bird(Obj):

    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

        self.grav = 1   #variavel de gravidade
        self.vel = 4    #variavel de velocidade

        self.ticks = 0  #variavel de ticks
        self.img = 1
        self.pts = 0
        
        self.play = True

        pygame.mixer.init()
        
        self.sound_pts = pygame.mixer.Sound("assets/sounds/point.wav")
        self.sound_wing = pygame.mixer.Sound("assets/sounds/wing.wav")
        self.sound_hit = pygame.mixer.Sound("assets/sounds/hit.wav")

    def update(self, *args):

        self.vel += self.grav      #apenas uma variavél para determinar que a velocidade seja constante, ou seja, ou ela aumenta, ou continua estavél.
        self.rect[1] += self.vel   #aqui é uma variavél para que, enquanto a velocidade não parar de aumentar, então a velocidade do passaró também não para de aumentar.

        if self.vel >= 10:  #essa condicao if é para dar um limite de velocidade
            self.vel = 10

        key = pygame.key.get_pressed()
        if self.play:
            if key[pygame.K_SPACE] and pygame.KEYDOWN:
                self.vel -= 5   #essa variavel é para adicionar uma gravidade quando o passaro cair(adicionar+ ele vai pra baixo, subtrair - ele vai pra cima)
                self.sound_wing.play()


        if self.rect[1] <= 0: #essa condição if é para o teto e o self.vel = 4 é quando ele entrar em colisão com o teto a variavél volta para onde ela estava
            self.rect[1] = 0
            self.vel = 4

        if self.rect[1] >= 420: #essa condiçãoo if é para o chão, assim entrando em colisão com o mesmo, aqui a velocidade não precisa ser resetada como no teto pois o personagem não estará em um movimento de queda constante como o teto.
            self.rect[1] = 420

        self.anim()

    def anim(self):
        self.img = (self.img + 1) % 4

        self.image = pygame.image.load("assets/bird" + str(self.img) + ".png")
       
    
    
    def colision_pipes(self, group):  #função de colisão com os canos(pipes)

        col = pygame.sprite.spritecollide(self, group, False)  #variavel de colisão, aqui se utiliza o pygame.spritecollide

        if col:
            self.play = False
            self.sound_hit.play()

    def colision_coin(self, group):

        col = pygame.sprite.spritecollide(self, group, True)  #aqui diferente dos pipes é True, pelo fato que os canos, a gente não destroem, já as moedas como vai existir um sistema de funcionamento elas são obrigatoriamente feitas para serem destruidas.

        if col:
            self.pts += 1
            self.sound_pts.play()


class Text:

    def __init__(self, size, text):

        self.font = pygame.font.Font("assets/font/font.ttf", size)
        self.render = self.font.render(text, True, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def text_update(self, text):
        self.render = self.font.render(text, True, (255, 255, 255))
    
    
    
    
    
    
    
    pygame.font.init()
    pygame.mixer.init()
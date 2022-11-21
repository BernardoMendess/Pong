from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.collision import *


largura = 800
altura = 600
teclado = keyboard.Keyboard()

janela = Window(largura, altura)
janela.set_title("Pong")

bola = Sprite("bola.png")
bola.set_position(janela.width/2 - bola.width/2, janela.height/2 - bola.height/2)

pad1 = Sprite("pad.png")
pad1.set_position(40, janela.height/2 - pad1.height/2)

pad2 = Sprite("pad.png")
pad2.set_position(janela.width - pad2.width - 40, janela.height/2 - pad1.height/2)

fundo = GameImage("fundo.png")
velx = 600
vely = 600
velpad = 500
placar1 = 0
placar2 = 0
centro = True
tempo = 0


while True:
    janela.set_background_color((0, 0, 0))
    if(teclado.key_pressed("ESC")):
        break

    #Movimentação da bola
    bola.x += velx*janela.delta_time()
    bola.y += vely*janela.delta_time()

    #Checando se a bola bateu no teto ou no chão
    if bola.y <= 0:
        bola.y += 1
        vely = vely * -1

    if bola.y >= altura - bola.height:
        bola.y -= 1
        vely = vely * -1

    #Colisão da bola com a raquete
    if (bola.collided(pad1) and velx < 0):
        velx *= -1

    if (bola.collided(pad2) and velx > 0):
        velx *= -1

    #Testando se a bola saiu do mapa e qual jogador pontuou
    if bola.x < 0:
        placar2 += 1
        centro = True

    if bola.x > janela.width:
        placar1 += 1
        centro = True

    #Colocando a bola no centro depois de algum jogador pontuar
    if centro == True:
        bola.set_position(janela.width / 2 - bola.width / 2, janela.height / 2 - bola.height / 2)
        pad1.set_position(40, janela.height / 2 - pad1.height / 2)
        pad2.set_position(janela.width - pad2.width - 40, janela.height / 2 - pad1.height / 2)
        velx = 0
        vely = 0
        velpad = 0
        tempo += 1
        if tempo == 300:
            velx = 600
            vely = 600
            velpad = 500
            centro = False
            tempo = 0

    #Movimentação do jogador
    if pad1.y >= 0:
        if (teclado.key_pressed("W")):
            pad1.y -= velpad*janela.delta_time()

    if pad1.y <= janela.height - pad1.height:
        if (teclado.key_pressed("S")):
            pad1.y += velpad*janela.delta_time()

    #Movimentação da IA
    if velx > 0 and bola.x > janela.width/2 and bola.x < janela.width:
        if pad2.y >= 0:
            if bola.y < pad2.y + pad2.height/2:
                pad2.y -= velpad*janela.delta_time()
        if pad2.y <= janela.height - pad2.height:
            if bola.y > pad2.y + pad2.height/2:
                pad2.y += velpad*janela.delta_time()


    fundo.draw()
    janela.draw_text(str(placar2), x=janela.width / 1.5, y=10, size=50, color=(211, 211, 211), font_name="arial", bold=True, italic=False)
    janela.draw_text(str(placar1), x=(janela.width / 3.3), y=10, size=50, color=(211, 211, 211), font_name="arial", bold=True, italic=False)
    pad1.draw()
    pad2.draw()
    bola.draw()
    janela.update()

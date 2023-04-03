import pygame
from pygame.locals import *
from random import *

def affich() :
    if ecran == 1 :
        pygame.draw.rect(fenetre,(125,125,125),(0,0,600,650))
        myfont = pygame.font.SysFont("Fixedsys",40)
        texte = myfont.render("Choisissez un mode de jeu :",False,(0,0,0))
        fenetre.blit(texte,(100,80))
        pygame.draw.rect(fenetre,(0,0,0),(95,195,410,90))
        pygame.draw.rect(fenetre,(255,255,255),(100,200,400,80))
        texte = myfont.render("Joueur contre joueur",False,(0,0,0))
        fenetre.blit(texte,(150,225))
        pygame.draw.rect(fenetre,(0,0,0),(95,395,410,90))
        pygame.draw.rect(fenetre,(255,255,255),(100,400,400,80))
        texte = myfont.render("Joueur contre IA",False,(0,0,0))
        fenetre.blit(texte,(175,425))
    elif ecran == 2 :
        pygame.draw.rect(fenetre,(255,255,255),(0,0,600,650))
        pygame.draw.rect(fenetre,(125,125,125),(0,0,600,50))
        myfont = pygame.font.SysFont("Fixedsys",40)
        if mode == 1 :
            texte = myfont.render("Joueur 1 :",False,(0,0,0))
            fenetre.blit(texte,(10,10))
            pygame.draw.polygon(fenetre,(237,28,36),((162,10),(190,38),(188,40),(160,12)))
            pygame.draw.polygon(fenetre,(237,28,36),((162,40),(190,12),(188,10),(160,38)))
            texte = myfont.render("Joueur 2 :",False,(0,0,0))
            fenetre.blit(texte,(410,10))
        elif mode == 21 :
            texte = myfont.render("Joueur :",False,(0,0,0))
            fenetre.blit(texte,(10,10))
            pygame.draw.polygon(fenetre,(237,28,36),((142,10),(170,38),(168,40),(140,12)))
            pygame.draw.polygon(fenetre,(237,28,36),((142,40),(170,12),(168,10),(140,38)))
            texte = myfont.render("IA :",False,(0,0,0))
            fenetre.blit(texte,(500,10))
        elif mode == 22 :
            texte = myfont.render("IA :",False,(0,0,0))
            fenetre.blit(texte,(10,10))
            pygame.draw.polygon(fenetre,(237,28,36),((72,10),(100,38),(98,40),(70,12)))
            pygame.draw.polygon(fenetre,(237,28,36),((72,40),(100,12),(98,10),(70,38)))
            texte = myfont.render("Joueur :",False,(0,0,0))
            fenetre.blit(texte,(430,10))
        pygame.draw.circle(fenetre,(0,162,232),(575,25),15)
        pygame.draw.line(fenetre,(0,0,0),(200,50),(200,650),10)
        pygame.draw.line(fenetre,(0,0,0),(400,50),(400,650),10)
        pygame.draw.line(fenetre,(0,0,0),(0,250),(600,250),10)
        pygame.draw.line(fenetre,(0,0,0),(0,450),(600,450),10)
        for i in range (3) :
            for j in range (3) :
                if plat[i*3+j] == "x" :
                    pygame.draw.polygon(fenetre,(237,28,36),((j*200+25,i*200+70),(j*200+180,i*200+225),(j*200+175,i*200+230),(j*200+20,i*200+75)))
                    pygame.draw.polygon(fenetre,(237,28,36),((j*200+25,i*200+230),(j*200+180,i*200+75),(j*200+175,i*200+70),(j*200+20,i*200+225)))
                elif plat[i*3+j] == "o" :
                    pygame.draw.circle(fenetre,(0,162,232),(j*200+100,i*200+150),80)

    elif ecran == 3 :
        pygame.draw.rect(fenetre,(125,125,125),(0,0,600,650))
        myfont = pygame.font.SysFont("Fixedsys",40)
        texte = myfont.render(gagne,False,(0,0,0))
        fenetre.blit(texte,(300-(len(gagne)//2)*15,310))

    pygame.display.flip()

def tour_ia() :
    global plat
    global plat2
    global j
    non = 0
    if j == 1 :
        a = "x"
    else :
        a = "o"
    for i in range (9) :
        if plat[i] == "-" :
            plat2 = list(plat)
            plat2[i] = a
            if test(a) == True :
                non = 1
                plat[i] = a
                break
    if non == 0 :
        if j == 1 :
            b = "o"
        else :
            b = "x"
        for i in range (9) :
            if plat[i] == "-" :
                plat2 = list(plat)
                plat2[i] = b
                if test(b) == True :
                    non = 1
                    plat[i] = a
                    break
    if non == 0 :
        for i in range (9) :
            total = 0
            if plat[i] == "-" :
                plat3 = list(plat)
                plat3[i] = a
                for k in range (9) :
                    if not i == k and plat[k] == "-" :
                        plat2[k] = a
                        if test(a) == True :
                            total += 1
            if total == 2 :
                non = 1
                plat[i] = a
                break
    if non == 0 :
        for i in range (9) :
            total = 0
            if plat[i] == "-" :
                plat3 = list(plat)
                plat3[i] = b
                for k in range (9) :
                    if not i == k and plat[k] == "-" :
                        plat2[k] = b
                        if test(b) == True :
                            total += 1
            if total == 2 :
                non = 1
                plat[i] = a
                break
    if non == 0 :
        i = randint(0,8)
        while not plat[i] == "-" :
            i = randint(0,8)
        plat[i] = a
    if j == 1 :
        j = 2
    else :
        j = 1

    affich()

def test(a) :
    if plat2[0] == plat2[1] == plat2[2] == a or plat2[3] == plat2[4] == plat2[5] == a or plat2[6] == plat2[7] == plat2[8] == a or plat2[0] == plat2[3] == plat2[6] == a or plat2[1] == plat2[4] == plat2[7] == a or plat2[2] == plat2[5] == plat2[8] == a or plat2[0] == plat2[4] == plat2[8] == a or plat2[2] == plat2[4] == plat2[6] == a :
        return(True)
    else :
        return(False)

def fin_partie() :
    global ecran
    global plat2
    global gagne
    plat2 = list(plat)
    if test("x") == True :
        ecran = 3
        if mode == 1 :
            gagne = "Le joueur 1 a gagné !"
        elif mode == 21 :
            gagne = "Vous avez gagné !"
        elif mode == 22 :
            gagne = "L'IA a gagné !"
    elif test("o") == True :
        ecran = 3
        if mode == 1 :
            gagne = "Le joueur 2 a gagné !"
        elif mode == 21 :
            gagne = "L'IA a gagné !"
        elif mode == 22 :
            gagne = "Vous avez gagné !"
    else :
        non = 0
        for i in range (9) :
            if plat2[i] == "-" :
                non = 1
        if non == 0 :
            ecran = 3
            gagne = "Egalité."

    affich()

pygame.init()

fenetre = pygame.display.set_mode((600,650))
pygame.display.set_caption("Morpions")

raccourci = __file__
raccourci = raccourci[0:-8]

icone = pygame.image.load(raccourci+"icone.png")
pygame.display.set_icon(icone)

plat = []
for i in range (9) :
    plat += ["-"]
ecran = 1
mode = 1

affich()

b = 1
while b == 1 :
    for event in pygame.event.get() :
        if event.type == QUIT :
            b = 0
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN :
            if ecran == 1 :
                if event.pos[0] > 100 and event.pos[0] < 500 and event.pos[1] > 200 and event.pos[1] < 280 :
                    mode = 1
                    ecran = 2
                    j = 1
                elif event.pos[0] > 100 and event.pos[0] < 500 and event.pos[1] > 400 and event.pos[1] < 480 :
                    j = 1
                    mode = 20+randint(1,2)
                    ecran = 2
            elif ecran == 2 and (mode == 1 or mode == 21 and j == 1 or mode == 22 and j == 2) and event.pos[1] > 50 and plat[event.pos[0]//200+((event.pos[1]-50)//200)*3] == "-" :
                if j == 1 :
                    plat[event.pos[0]//200+((event.pos[1]-50)//200)*3] = "x"
                    j = 2
                else :
                    plat[event.pos[0]//200+((event.pos[1]-50)//200)*3] = "o"
                    j = 1
                fin_partie()

            affich()
            if ecran == 2 and (mode == 21 and j == 2 or mode == 22 and j == 1) :
                tour_ia()
                fin_partie()
        elif event.type == KEYDOWN :
            if ecran == 3 :
                if event.key == K_RETURN :
                    ecran = 1
                    plat = []
                    for i in range (9) :
                        plat += ["-"]

            affich()
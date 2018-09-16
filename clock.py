import pygame
import math
import sys
import datetime
import textwrap

#Init Pygame
pygame.init()

#Define Constants
logo = pygame.image.load('images/shell_Logo.png')
bluish_key = pygame.image.load('images/bluish_key.png')
nudeish_key = pygame.image.load('images/nudeish_key.png')
orangeish_key = pygame.image.load('images/orangeish_key.png')
pinkish_key = pygame.image.load('images/pinkish_key.png')


pi = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282"
pi = list(pi)
displayWidth = 1080
displayHeight = 720

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('PiClock')

largeText = pygame.font.Font('freesansbold.ttf', 48)
mediumText = pygame.font.Font('freesansbold.ttf', 36)
smallText = pygame.font.Font('freesansbold.ttf', 22)

intro_back = (22, 51, 62)
intro_text = (255, 255, 255)
black = (255,255,255)
bluish = (53,255,186)
pinkish = (255, 149, 112)
orangeish = (220, 110, 30)
nudeish = (255, 198, 154)



#Define Methods
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def pi_text_objects(text, font, color):
    rect = pygame.Rect((250,150),(500,300))
    rect.y = displayHeight - 600
    rect.x = displayWidth - 400
    textSurface = font.render(text, True, color)
    return textSurface, rect

def button(msg, x,y, w, h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def getTime():
    currentTime = str(datetime.datetime.now())
    currentTime = currentTime.split()
    currentTime = currentTime[1].split(':')
    return currentTime

def getHour():
    return getTime()[0]

def getMinutes():
    return getTime()[1]

def getSeconds():
    return getTime()[2].split('.')[0]

def getMicroSeconds():
    return getTime()[2].split('.')[1]

def getHourMinSec():
    hourmin = []
    hourmin.append(getHour()[0])
    hourmin.append(getHour()[1])
    hourmin.append(getMinutes()[0])
    hourmin.append(getMinutes()[1])
    hourmin.append(getSeconds()[0])
    hourmin.append(getSeconds()[1])
    hourmin.append(getMicroSeconds()[0])


    return hourmin

#VERY IMPORTANT METHOD
#
# def printPi(hour, minute):
#     timePos = 0
#     piPos = 0
#     while timePos < len(getHourMin()):



#Init run time clock
clock = pygame.time.Clock()

def clockScreen():
    #While 'running' value
    running = True
    while running:
        for event in pygame.event.get():
            #if quit then quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(intro_back)

        textSurf, textRect = text_objects("PiClock", largeText, intro_text)
        textRect.center = ((displayWidth/2) , (displayHeight/8.5))
        gameDisplay.blit(textSurf,textRect)

        textSurf2, textRect2 = text_objects("Current time: " + getHour() + ":" + getMinutes() + ":" + getSeconds(), mediumText, intro_text)
        textRect2.center = ((displayWidth / 2), (displayHeight/5))
        gameDisplay.blit(textSurf2,textRect2)

        gameDisplay.blit(logo, ((displayWidth - displayWidth/8),(displayHeight - displayHeight/5)))

        gameDisplay.blit(bluish_key, ((displayWidth/9),(displayHeight - displayHeight/6)) )

        textSurf4, textRect4 = text_objects(" = Hours", smallText, intro_text)
        textRect4.center = ((displayWidth / 5.5), (displayHeight - displayHeight/7))
        gameDisplay.blit(textSurf4, textRect4)

        gameDisplay.blit(pinkish_key, ((displayWidth / 4), (displayHeight - displayHeight / 6)))

        textSurf4, textRect4 = text_objects("= Minutes", smallText, intro_text)
        textRect4.center = ((displayWidth / 3.01), (displayHeight - displayHeight / 7))
        gameDisplay.blit(textSurf4, textRect4)
        gameDisplay.blit(bluish_key, ((displayWidth / 9), (displayHeight - displayHeight / 6)))

        gameDisplay.blit(orangeish_key, ((displayWidth / 2.5), (displayHeight - displayHeight / 6)))


        textSurf4, textRect4 = text_objects("= Seconds", smallText, intro_text)
        textRect4.center = ((displayWidth / 2.05), (displayHeight - displayHeight / 7))
        gameDisplay.blit(textSurf4, textRect4)
        gameDisplay.blit(bluish_key, ((displayWidth / 9), (displayHeight - displayHeight / 6)))

        gameDisplay.blit(nudeish_key, ((displayWidth/1.8), (displayHeight - displayHeight / 6)))

        textSurf4, textRect4 = text_objects("= Microseconds", smallText, intro_text)
        textRect4.center = ((displayWidth - displayWidth/3.02), (displayHeight - displayHeight / 7))
        gameDisplay.blit(textSurf4, textRect4)

        piPos=0
        timePos= 0
        timeArr = getHourMinSec()
        x = 150
        y = 200
        while piPos < len(pi) - 62:

            if timePos < len(timeArr):
                if pi[piPos] == timeArr[timePos]:
                    if timePos == 0 or timePos == 1:
                        textSurf3, textRect3 = text_objects(pi[piPos], largeText, bluish)
                        textRect3.center = (x, y)
                        gameDisplay.blit(textSurf3, textRect3)
                    elif timePos == 2 or timePos == 3:
                        textSurf3, textRect3 = text_objects(pi[piPos], largeText, pinkish)
                        textRect3.center = (x, y)
                        gameDisplay.blit(textSurf3, textRect3)
                    elif timePos == 4 or timePos == 5:
                        textSurf3, textRect3 = text_objects(pi[piPos], largeText, orangeish)
                        textRect3.center = (x, y)
                        gameDisplay.blit(textSurf3, textRect3)
                    else:
                        textSurf3, textRect3 = text_objects(pi[piPos], largeText, nudeish)
                        textRect3.center = (x, y)
                        gameDisplay.blit(textSurf3, textRect3)
                    timePos += 1
                else:
                    textSurf3, textRect3 = text_objects(pi[piPos], smallText, intro_text)
                    textRect3.center = (x, y)
                    gameDisplay.blit(textSurf3, textRect3)
            else:
                textSurf3, textRect3 = text_objects(pi[piPos], smallText, intro_text)
                textRect3.center = (x, y)
                gameDisplay.blit(textSurf3, textRect3)
            x += 32
            if x > (displayWidth - (displayWidth / 8)):
                x = 150
                y += 37
            # print(piPos)
            piPos += 1


        clock.tick()
        pygame.display.update()

clockScreen()
quit()
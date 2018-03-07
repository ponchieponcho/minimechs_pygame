import pygame, time, os

def main():
    width = 800
    height = 600
    black_color = (0, 0, 0)
    grey_color = (100, 100, 100)
    red_color = (255,0,0)
    FPS = 8
    pos = 0 
    i = 0

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('MiniMechs v2')
    clock = pygame.time.Clock()

    mech1_idle1 = pygame.image.load('images/mech1/sdgundam_idle1.png')
    mech1_idle2 = pygame.image.load('images/mech1/sdgundam_idle2.png')
    mech1_idle3 = pygame.image.load('images/mech1/sdgundam_idle3.png')
    mech1_idle4 = pygame.image.load('images/mech1/sdgundam_idle4.png')
    mech2 = pygame.image.load('images/mech2/char_idle1.png')
    space_bkg = pygame.image.load('images/backgrounds/space_bkg.png')
    console_bkg = pygame.image.load('images/backgrounds/console_bkg.png')
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (255, 0, 0))

    # while i < FPS:
    #     position = 0
    #     if position < 4:
    #         print('images/mech1/sdgundam_idle%d.png' % position)
    #         position += 1
    #     # mechAnimation.append('images/mech1/sdgundam_idle%s.png' % pos)
    #     i += 1

    mechAnimation = [
    mech1_idle1,
    mech1_idle2,
    mech1_idle3,
    mech1_idle4
]      

    stop_game = False

    while not stop_game:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

        screen.fill(black_color)
        screen.blit(space_bkg,(0,0))
        screen.blit(console_bkg,(0,0))
        pygame.draw.line(screen, grey_color, (0,400), (800,400+0), 6)
        screen.blit(mech2, (600, 230))
        #screen.blit(textsurface, (0,0)) #displays test text        
        screen.blit(mechAnimation[pos], (0, 0))  

        pos += 1
        if pos > 3:
            pos = 0
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    os.system('clear')

main()

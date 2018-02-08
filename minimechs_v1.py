import pygame
import time
import os

def main():
    # declare the size of the canvas
    width = 800
    height = 600
    black_color = (0, 0, 0)
    grey_color = (100, 100, 100)
    red_color = (255,0,0)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('MiniMechs v1')
    clock = pygame.time.Clock()

    # Game initialization
    mech1 = pygame.image.load('images/mech1/sdgundam_idle1.png')
    mech2 = pygame.image.load('images/mech2/char_idle1.png')
    space_bkg = pygame.image.load('images/backgrounds/space_bkg.png')
    console_bkg = pygame.image.load('images/backgrounds/console_bkg.png')
    myfont = pygame.font.SysFont('Futura', 30)
    buttonMelee = myfont.render('Melee', False, red_color)
    buttonRanged = myfont.render('Ranged', False, red_color)
    buttonDefend = myfont.render('Defend', False, red_color)
    buttonFlee = myfont.render('Flee', False, red_color)

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        screen.fill(black_color)
        screen.blit(space_bkg,(0,0))
        screen.blit(console_bkg,(0,0))
        pygame.draw.line(screen, grey_color, (0,400), (800,400+0), 6)
        pygame.draw.rect(screen, grey_color, (50, 420, 200, 60)) 
        pygame.draw.rect(screen, grey_color, (50, 500, 200, 60)) 
        pygame.draw.rect(screen, grey_color, (550, 420, 200, 60)) 
        pygame.draw.rect(screen, grey_color, (550, 500, 200, 60))
        screen.blit(buttonMelee,(115,440))
        screen.blit(buttonRanged,(110,520))
        screen.blit(buttonDefend,(620,440))
        screen.blit(buttonFlee,(630,520))


        # Game display
        screen.blit(mech1, (150, 240)) # x  higher=right , y - higher=down
        screen.blit(mech2, (600, 230))


        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    os.system('clear')

if __name__ == '__main__':
    main()

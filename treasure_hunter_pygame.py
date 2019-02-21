import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('hunter.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = pos

class Hunter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('hunter.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.speed_x = 50
        self.speed_y = 50

def main():
    pygame.init()
    size =[800, 800]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 50
    bg = pygame.image.load('map.jpg')


    

    player = Hunter(100, 100) # determines player start location
    

    player_group = pygame.sprite.Group()
    player_group.add(player)

    
    while True:
        
        for event in pygame.event.get():
            # Event handling
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    player.rect.y += 50
                elif event.key == KEY_UP:
                    player.rect.y -= 50
                elif event.key == KEY_LEFT:
                    player.rect.x -= 50
                elif event.key == KEY_RIGHT:
                    player.rect.x += 50
            
            if event.type == pygame.QUIT:
                return False


        screen.blit(bg, (0,0)) #pygame.image.load('../images/background.png').convert_alpha()

        # first parameter takes a single sprite
        # second parameter takes sprite groups
        # third parameter is a do kill commad if true
        # all group objects colliding with the first parameter object will be
        # destroyed. The first parameter could be bullets and the second one
        # targets although the bullet is not destroyed but can be done with
        # simple trick bellow
        # hit = pygame.sprite.spritecollide(player, wall_group, True)


        player_group.draw(screen)
        # wall_group.draw(screen)

        pygame.display.update()
        clock.tick(fps)
        
        font = pygame.font.Font(None, 25)
        text = font.render('Use arrow keys to move the Hunter', True, (0, 0, 0))
        screen.blit(text, (80, 750))

    pygame.quit()


if __name__ == '__main__':
    main()
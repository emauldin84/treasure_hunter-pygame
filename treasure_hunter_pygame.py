import pygame
import sys
import random

pygame.font.init()

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

class Treasure(pygame.sprite.Sprite):
    def __init__(self, x_treasure, y_treasure):
        pygame.sprite.Sprite.__init__(self)
        self.x_treasure = x_treasure # generate random x coordinate
        self.y_treasure = y_treasure # generate random y coordinate

treasure_coordinates = [-25, 125, 275, 425, 575]
y_treasure = random.choice(treasure_coordinates)
x_treasure = random.choice(treasure_coordinates)
treasure = Treasure(x_treasure, y_treasure)



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
    treasure_group = pygame.sprite.Group()
    treasure_group.add(treasure)
    print(x_treasure, y_treasure)
    while True:
        
        for event in pygame.event.get():
            # Event handling
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN and player.rect.y < 574:
                    player.rect.y += 150
                if event.key == KEY_UP and player.rect.y > -24:
                    player.rect.y -= 150
                if event.key == KEY_LEFT and player.rect.x > -24:
                    player.rect.x -= 150
                if event.key == KEY_RIGHT and player.rect.x < 574:
                    player.rect.x += 150
                print(player.rect.x, player.rect.y)

            if event.type == pygame.KEYDOWN:
                if event.key == KEY_D:
                
            
            if event.type == pygame.QUIT:
                return False

        


        screen.blit(bg, (-50,-50)) #pygame.image.load('../images/background.png').convert_alpha()

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
        
        font = pygame.font.SysFont(None, 25)
        text = font.render("Use arrow keys to move the Hunter & 'D' to dig for treasure.", False, (0, 0, 0))
        screen.blit(text, (80, 400))

    pygame.quit()


if __name__ == '__main__':
    main()
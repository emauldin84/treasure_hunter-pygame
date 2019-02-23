import pygame
import sys
import random
import time
from pygame.locals import *

pygame.font.init()
pygame.font.get_fonts()

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
D_Key = pygame.K_d
Y_Key = pygame.K_y
N_Key = pygame.K_n
dig_length = 30



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

def main():
    
    pygame.init()
    size =[800, 800]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 50
    bg = pygame.image.load('map.jpg')
    
    font_background = pygame.Surface((800, 46), pygame.SRCALPHA)
    font_background.fill((0, 0, 0, 128))

    end_game_background = pygame.Surface((535, 50), pygame.SRCALPHA)
    end_game_background.fill((0, 0, 0, 128))
    
    pygame.mixer.init()
    sound = pygame.mixer.Sound('Shovel.wav')
    shovel_breaks = pygame.mixer.Sound('LTTP_Shatter.wav')
    victory_sound = pygame.mixer.Sound('WW_Fanfare_Pearl.wav')
    victory_sound.set_volume(.5)
    music = pygame.mixer.music.load("Hollow Knight OST - Dung Defender.mp3")
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play()
    hole = pygame.image.load('hole.png').convert_alpha()
    treasure_coordinates = [-25, 125, 275, 425, 575]
    y_treasure = random.choice(treasure_coordinates)
    x_treasure = random.choice(treasure_coordinates)
    treasure = Treasure(x_treasure, y_treasure)

    player = Hunter(100, 100) # determines player start location

    player_group = pygame.sprite.Group()
    player_group.add(player)
    treasure_group = pygame.sprite.Group()
    treasure_group.add(treasure)
    print(x_treasure, y_treasure)

    
    font = pygame.font.Font(None, 32)
    title_font = pygame.font.Font("Open_Sans/OpenSans-Bold.ttf", 30)
    instructions_font = pygame.font.Font(None, 24)
    nothing_there_font = pygame.font.Font(None, 32)
    title = title_font.render("Treasure Hunter", True, (255, 255, 255))
    instructions = instructions_font.render("Use arrow keys to move the Hunter & 'D' to dig for treasure.", True, (255, 255, 255))
    
    shovel_vitals = 12
    current_status = ()
    game_play_message = font.render("%s" % (current_status,), True, (255, 255, 255))
    found_treasure_message = font.render("Treasure Hunter has found the Treasure! You win!", True, (255, 255, 255))
    you_lose_message_1 = font.render("Your shovel has broken. You lose!", True, (255, 255, 255))
    play_again_message = font.render("Press 'Y' to start try again. Press 'N' to quit.", True, (255, 255, 255))
    nothing_there_message = nothing_there_font.render("Nothing there!", True, (255, 255, 255))
    dig_counter = dig_length
    hole_list = []
    dig_result = ()
    
    
    while True:
        screen.blit(bg, (-50,-50))
        screen.blit(font_background, (0,0))
        screen.blit(font_background, (0,775))
        shovel_health_display = font.render("Shovel Health: %d" % (shovel_vitals), True, (255, 255, 255))

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

                if event.key == D_Key:
                    sound.play()
                    dig_counter = 0
                    player.image = pygame.image.load('hunter-dig.png').convert_alpha()
                    # append hole coordinates to hole list
                    hole_list.append([player.rect.x, player.rect.y])
                    
                    if (player.rect.x, player.rect.y) == (x_treasure, y_treasure):
                        dig_result = True
                        pygame.mixer.music.set_volume(.2)
                        victory_sound.play()
                    else:
                        shovel_vitals -= 2
                        print(shovel_vitals)
                        dig_result = False
                    if shovel_vitals == 0:
                        sound.set_volume(.0)
                        shovel_breaks.play()   
            
        if event.type == pygame.QUIT:
            return False

        
        # draw everything in hole list
        # print(hole_list)    
        for i in hole_list:
            screen.blit(hole, (i[0], i[1]))

        # increment dig_counter by 1
        dig_counter += 1
        if dig_counter > dig_length:
            player.image = pygame.image.load('hunter.png').convert_alpha()
        else:
            player.image = pygame.image.load('hunter-dig.png').convert_alpha()
            if dig_result == False:
                current_status = screen.blit(nothing_there_message, (12, 12))
        
        player_group.draw(screen)

        # draw dig result to screen
        if dig_result == True:
            screen.blit(end_game_background, (150,345))
            current_status = screen.blit(found_treasure_message, (160, 350))
            screen.blit(play_again_message, (190, 370))
            pygame.event.clear()
            event = pygame.event.wait()
            if hasattr(event, 'key') and event.key == Y_Key:
                main()
            elif hasattr(event, 'key') and event.key == N_Key:
                pygame.quit()
            
            

        # decrement shovel_vitals by 2 on each False dig result
        
        # print you_lose_message to screen when shovel_vitals == 0
        if shovel_vitals == 0:
            pygame.mixer.music.set_volume(.2)
            key = pygame.key.get_pressed()
            screen.blit(end_game_background, (150,345))
            screen.blit(you_lose_message_1, (250, 350))
            screen.blit(play_again_message, (190, 370))
            pygame.event.clear()
            event = pygame.event.wait()
            if hasattr(event, 'key') and event.key == Y_Key:
                main()
            elif hasattr(event, 'key') and event.key == N_Key:
                pygame.quit()
            
            
        # player_group.draw(screen)
        screen.blit(title, (280, 0))
        screen.blit(instructions, (175, 780))
        screen.blit(shovel_health_display, (600, 12))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
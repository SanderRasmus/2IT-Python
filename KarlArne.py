''' IMPORTERER PYGAME-BIBLIOTEKET OG NØDVENDIGE KONSTANTER '''
import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import random
import time

''' STARTER OPP PYGAME '''
pygame.init()

''' LAGER KONSTANTER SOM BRUKES I PROGRAMMET '''
# Høyde og bredde på spillvinduet
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 850
# Definerer noen farger som kan brukes i spillet (fargepalett)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)

''' OPPRETTER SPILLVINDUET '''
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

''' OPPRETTER EN KLASSE FOR SPILLEREN '''
class Player(pygame.sprite.Sprite):
    # Konstruktør for å opprette et Player-objekt
    def __init__(self):
        # Definerer klassen vår som en subklasse av Sprite-klassen (som er innebygd i Pygame)
        super(Player, self).__init__()
        # Definerer overflaten til Player-objektet
        self.surf = pygame.image.load("jet.png").convert()
        # Setter fargen til Player-objektet
        self.surf.set_colorkey((COLOR_WHITE), RLEACCEL)
        # Setter Player-objektet til å være et rektangel
        self.rect = self.surf.get_rect()

    # Lager en metode for å flytte Player-objektet ut fra knappene som er trykket inn
    # move_ip (move in place) flytter objektet relativt til dets nåværende posisjon
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT


''' OPPRETTER EN KLASSE FOR FIENDER '''
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # Definerer klassen vår som en subklasse av Sprite-klassen (som er innebygd i Pygame)
        super(Enemy, self).__init__()
        # Definerer overflaten til Enemy-objektet 
        self.surf = pygame.image.load("missile.png").convert()
        # Definerer fargen til Enemy-objektet
        self.surf.set_colorkey((COLOR_WHITE), RLEACCEL)
        #Plasserer fienden på et tilfeldig sted utenfor skjermen (til høyre for skjermen)
        self.rect = self.surf.get_rect(
            center=(
                # random.randint(a, b) -> genererer et tilfeldig heltall mellom a og b
                random.randint(WINDOW_WIDTH + 20, WINDOW_WIDTH + 100),
                random.randint(0, WINDOW_HEIGHT)
            )
        )
        # Gir fienden en hastighet (tilfeldig mellom 1 og 3)
        self.speed = random.randint(5, 20)


    # Lager en metode for å flytte en fiende
    def update(self):
        # Fiender flytter seg fra høyre mot venstre
        self.rect.move_ip(-self.speed*0.10, 0)
        #Hvis fienden går utenfor skjermen på venstre side, fjernes fienden fra spillet
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("Cloud.png").convert()
        self.surf.set_colorkey((COLOR_BLACK), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(WINDOW_WIDTH + 20, WINDOW_WIDTH + 100),
                random.randint(0, WINDOW_HEIGHT),
            )
        )
        self.speed = random.randint(5, 10)
    
    def update(self):
        self.rect.move_ip(-self.speed*0.20, 0)
        if self.rect.right < 0:
            self.kill

''' LAGER EN NY EVENT I SPILLET '''    
ADDENEMY = pygame.USEREVENT + 1
# Setter eventen til å kjøre med 250 millisekunders mellomrom
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 700)

''' OPPRETTER ET OBJEKT AV KLASSEN PLAYER (spillerobjektet) '''
player = Player()

''' OPPRETTER GRUPPER FOR SPRITENE I SPILLET '''
# En gruppe for alle fiender
enemies = pygame.sprite.Group()

clouds = pygame.sprite.Group()
# En gruppe for alle sprites (alle fiender pluss spilleren)
all_sprites = pygame.sprite.Group()
# Legger til spilleren i gruppen all_sprites
all_sprites.add(player)

# Boolean-variabelen running angir om spillet kjører eller ikke
running = True

liv = 5
liv_tapt = 0

''' SPILL-LØKKA SOM REPETERER SÅ LENGE running ER LIK true '''
while running:

    ''' LØKKE SOM SJEKKER EVENTS SOM SKJER I SPILLET '''
    for event in pygame.event.get():
        # Hvis vinduet lukkes skal spilles avsluttes
        if event.type == QUIT:
            running = False
        # Hvis ESC-knappen trykkes skal spillet avsluttes
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        # Hvis eventen ADDENEMY kjøres skal det opprettes en ny fiende
        # Vi husker at vi oprettet eventen ADDENEMY og fikk denn til å kjøre hvert 250. millisekund
        elif event.type == ADDENEMY:
            # Oppretter et nytt objekt av klassen Enemy
            new_enemy = Enemy()
            # Legger fiendeobjektet i Sprite-gruppen enemies
            enemies.add(new_enemy)
            # Legger fiendeobjektet i Sprite-gruppen all_sprites
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    ''' HENTER INN ALLE KNAPPER SOM ER TRYKKET INN SOM EN DICTIONARY '''
    pressed_keys = pygame.key.get_pressed()

    # Kjører metoden update fra Player-klassen, med knappene som er trykket inn
    # Dette gjør at spilleren beveger seg når vi trykker på piltastene
    player.update(pressed_keys)
    # Kjører metoden update fra Enemy-klassen
    # Dette gjør at fiendene flyr over skjermen fra høyre side
    enemies.update()
    clouds.update()
    
    ''' TEGNER OPP BAKGRUNNSFARGEN TIL SKJERMEN '''
    # Bakgrunnen tegnes opp på nytt hver gang noe flytter på seg, slik at objekter ikke sitter igjen påo skjermen
    screen.fill((135, 206, 250))

    ''' TEGNER OPP ALLE SPILOBJEKTER (SPRITES) '''
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    ''' SJEKKER OM SPILLEREN KOLLIDERER MED EN FIENDE '''
    if pygame.sprite.spritecollideany(player, enemies):
        enemy = pygame.sprite.spritecollideany(player, enemies)
        enemy.kill()
        liv -= 1
        print(f"Du har nå {liv} igjen!")
        # Spilleren fjerns
        ##player.kill()
        # Spillet avsluttes
        ##running = False

    if liv == 0:
        print("Du har nå då!")
        player.kill
        running = False

    ''' TEGNER OPP ALLE ELEMENTER PÅ SKJERMEN '''
    pygame.display.flip()

''' NÅR VI FORLATER SPILL-LØKKA AVSLUTTES PYGAME '''
pygame.quit()
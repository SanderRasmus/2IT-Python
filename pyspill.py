import pygame as pg

#Initialiserer PyGame ved start
pg.init()

#Setter vindu bredde og høyde som en "kostant". Med andre ord en verdi som ikke skal endres
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
# Pg.display.set_mode forteller pygame hva bredden og høyden på vinduet er ved bruk av konstantene våre. Vi lagrer dette i variablen vindu.
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Klassen / Oppskriften til Ballen og funksjonene tegn og flytt
class Ball:
  # Initialiserer verdiene i ballen. X & Y Kordinater, Farten til ballen, Radiusen og vinduet den skal tegnes i.
  def __init__(self, x, y, fart, radius, vindusobjekt):
    self.x = x
    self.y = y
    self.fart = fart
    self.radius = radius
    self.vindusobjekt = vindusobjekt
  
  # Metode for å tegne sirkelen. Første blokk sier at den skal tegnes i vinduet, Andre blokk forteller noe om fargen, Tredje om X og Y
  # Og den siste betyr størrelsen/radiusen til sirkelen.
  def tegn(self):
    pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 

  # Metode for å flytte ballen. Her sier den at om x - radius er mindre eller det samme som 0
  # Eller x + radius er større eller det samme som bredden på vinduet vil farten bli reversert å sende kulen bakover.
  def flytt(self):
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.fart = -self.fart
    
    self.x += self.fart

# Lager ballen ved bruk av klasse/oppskriften. Her sier vi at x skal være 250, y 250, fart 0.3, radius 30 og at den skal bli tegnet i vindu.
# Siden vi følger oppskriften til ballen blir også variabelen "vindusobjekt" gjort om til "vindu" variabelen.
ball = Ball(250, 250, 0.3, 30, vindu)

# Uendelig løkke som avslutter spillet da det avsluttes, eller fortsetter å tegne samt flytte ballen på skjermen. Vi bruker også
# vindu.fill siden at bakgrunnen også må bli malt/tegnet på nytt, hvis ikke hadded et bare vært en lang oransj strek på skjermen etter sirkelen.
fortsett = True
while fortsett:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((135, 206, 235))

    ball.tegn()
    ball.flytt()

    pg.display.flip()

pg.quit()
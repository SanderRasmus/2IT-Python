import pygame as pg
import math as m
import time as t
import random as rd

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
  def __init__(self, x, y, fartx, farty, radius, vindusobjekt):
    self.x = x
    self.y = y
    self.fartx = fartx
    self.farty = farty
    self.radius = radius
    self.vindusobjekt = vindusobjekt
  
  # Metode for å tegne sirkelen. Første blokk sier at den skal tegnes i vinduet, Andre blokk forteller noe om fargen, Tredje om X og Y
  # Og den siste betyr størrelsen/radiusen til sirkelen.
  def tegn(self):
    pg.draw.circle(self.vindusobjekt, (0, 100, 255), (self.x, self.y), self.radius) 

  # Metode for å flytte ballen. Her sier den at om x - radius er mindre eller det samme som 0
  # Eller x + radius er større eller det samme som bredden på vinduet vil farten bli reversert å sende kulen bakover.

  # Den andre if-statementen sjekker om at y - radius er mindre eller det samme som 0, samt
  # om y er det samme som eller større en høyden på vinduet. Om dette blir TRUE, blir farten reversert og man snur da ballen rundt.
  def flytt(self):
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.fartx = -self.fartx

    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.farty = -self.farty

    #Self.x += self.fartx gjør slik at den flytter seg i samråd med fart. Samme går for self.y += self.farty
    self.x += self.fartx
    self.y += self.farty
  
  def finnAvstand(self, obj2):
     xAvstand2 = (self.x - obj2.x)**2 # x avstand i andre
     yAvstand2 = (self.y - obj2.y)**2 # y avstand i andre
     avstand = m.sqrt(xAvstand2 + yAvstand2)
     return avstand

# Tom Liste
kuler = []

# Loop som lager 4 baller med random posisjon, samt fart og radius. RD.Uniform henter et random tall fra a til b.
for i in range(5):
   x = rd.randint(0, VINDU_BREDDE)
   y = rd.randint(0, VINDU_HOYDE)
   fartx = rd.uniform(-0.2, 0.2)
   farty = rd.uniform(-0.5, 0.2)
   radius = rd.randint(10, 30)
   kuler.append(Ball(x, y, fartx, farty, radius, vindu))

# Lager ballen ved bruk av klasse/oppskriften. Her sier vi at x skal være 250, y 250, fart 0.3, radius 30 og at den skal bli tegnet i vindu.
# Siden vi følger oppskriften til ballen blir også variabelen "vindusobjekt" gjort om til "vindu" variabelen.
#obj1 = Ball(250, 250, 0.3, 0.1, 30, vindu)
#obj2 = Ball(50, 400, 0.2, 0.4, 25, vindu)

# Uendelig løkke som avslutter spillet da det avsluttes, eller fortsetter å tegne samt flytte ballen på skjermen. Vi bruker også
# vindu.fill siden at bakgrunnen også må bli malt/tegnet på nytt, hvis ikke hadded et bare vært en lang oransj strek på skjermen etter sirkelen.
fortsett = True

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((231, 206, 100))

    # Loop for hvel kule i listen
    for kule in kuler:
       kule.tegn()
       kule.flytt()

    # For loop som repeteres for hver kule i listen "kuler".
    # Så sjekker den videre angående avstanden mellom kulene og sier om de traff hverandre.
    
    for i in range(len(kuler)):
        for j in range(i + 1, len(kuler)):
            avstand = kuler[i].finnAvstand(kuler[j])
            if avstand <= kuler[i].radius + kuler[j].radius:
                print("Kulene traff hverandre!")


    #if avstand <= obj1.radius + obj2.radius and not kollisjon_skjedd:
    #   print("Kulene traff hverandre!")
    #   kollisjon_skjedd = True
    #elif avstand > obj1.radius + obj2.radius:
    #   kollisjon_skjedd = False # Resetter kollisjons variabelen etter de har truffet hverandre.
  
    pg.display.flip()

pg.quit()
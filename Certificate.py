import pygame
import csv
import pandas as pd

# Read the XLSX file
xlsx_file = 'Ai for biomedical _ registration data.xlsx'
df = pd.read_excel(xlsx_file)

# Save the DataFrame as a CSV file
csv_file = 'AIBiomedical2.csv'
df.to_csv(csv_file, index=False)

def ren(name):
    if len(name) >= 20:
        font = pygame.font.Font('Darleston.otf',80)
    else:
        font = pygame.font.Font('Darleston.otf',80)
    return font.render(name,True,(0,0,0))

pygame.init()

win = pygame.display.set_mode((1600,1131))

with open('AIBiomedical2.csv', newline='\n') as f:
    reader = csv.reader(f)
    data = list(reader)

topic = "hehe"
for person in data[1:]:
    if topic != person[4]:
        bg = pygame.image.load("C:/Users/Sagnik Barman/Desktop/RhapsodyCert/"+person[4]+".png")
        topic = person[4]
    
    text = ren(person[1].title())
    textrect = text.get_rect()
    textrect.center = (800,520)
    
    win.blit(bg,(-2,-4))
    win.blit(text,textrect)
    
    pygame.display.update()
    pygame.image.save(win, ".\\certs\\"+person[4].title()+"_"+person[1]+".png")

pygame.quit()

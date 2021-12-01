import pygame

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))


face=pygame.Rect(100,200,200,200)
mouth=pygame.Rect(160,320,70,30)
eye1=pygame.Rect(120,240,60,30)
eye2=pygame.Rect(210,240,60,30)



while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
         
    pygame.draw.rect(screen,(120,120,120),face)  
    pygame.draw.rect(screen,(255,255,0),eye1)
    pygame.draw.rect(screen,(255,255,0),eye2)
    pygame.draw.rect(screen,(255,0,255),mouth)
    
    pygame.display.update()
    clock.tick(30)





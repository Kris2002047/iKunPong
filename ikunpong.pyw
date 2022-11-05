import pygame

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("iKunPong")
pygame.display.set_icon(pygame.image.load("./img/ball.png"))

background_color = (0, 0, 0)

pd = {
    "pic" : pygame.image.load("./img/paddle.png"),
    "width" : 100,
    "height" : 15,
    "x" : 0,
    "y" : height - 50,
    "speed" : 0.5
}

bl = {
    "pic" : pygame.image.load("./img/ball.png"),
    "width" : 30,
    "height" : 30,
    "x" : 10,
    "y" : 50,
    "speedx" : 0.1,
    "speedy" : 0.1
}

loop_expr = True
key_down = 1
score = 0
font = pygame.font.SysFont(['Courier New', "Consolas"], 24, bold=True)
n_speed = 0.01

while loop_expr:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_expr = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # if(pd["x"]>0):
                #     pd["x"] -= pd["speed"]
                key_down = 0
            if event.key == pygame.K_RIGHT:
                # if(pd["x"]<width-pd["width"]):
                #     pd["x"] += pd["speed"]
                key_down = 2
        if event.type == pygame.KEYUP:
            key_down = 1
    if key_down == 0:
        if pd["x"] >= 1:
            pd["x"] -= pd["speed"]
    if key_down == 2:
        if pd["x"] <= width-pd["width"]-1:
            pd["x"] += pd["speed"]
    if(bl["x"]<=0 and bl["y"]<=0):
        bl["speedx"] = -bl["speedx"]
        bl["speedy"] = -bl["speedy"]
    elif(bl["x"]>=width-bl["width"] and bl["y"]<=0):
        bl["speedx"] = -bl["speedx"]
        bl["speedy"] = -bl["speedy"]
    elif(bl["x"]>=width-bl["width"]):
        bl["speedx"] = -bl["speedx"]
    elif(bl["x"]<=0):
        bl["speedx"] = -bl["speedx"]
    elif(bl["y"]<=0):
        bl["speedy"] = -bl["speedy"]
    elif(bl["y"]>=height-50-pd["height"]):
        if(pd["x"]-bl["width"]<=bl["x"]<=pd["x"]+pd["width"]):
            score += 1
            bl["speedy"] = -bl["speedy"]
            if bl["speedx"]<0:
                bl["speedx"] -= n_speed
            else:
                bl["speedx"] += n_speed
            bl["speedy"] -= n_speed
        else:
            score -= 1
            bl["speedy"] = -bl["speedy"]
    bl["x"] += bl["speedx"]
    bl["y"] += bl["speedy"]
    text = font.render(f"Score: {score}", True, (255, 255, 255), (0, 0, 0))
    screen.blit(bl["pic"], (bl["x"], bl["y"]))
    screen.blit(pd["pic"], (pd["x"], pd["y"]))
    screen.blit(text, (0, 0))
    pygame.display.update()

pygame.quit()
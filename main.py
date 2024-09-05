import pygame as py

winH, winD = 1000, 800
win = py.display.set_mode(winH, winD)
py.display.set_caption("Cubical Survival")

bg = py.image.load("/Assets/Background_Template.jpg")

def draw():
    win.blit(bg, (0, 0))
    py.display.update()

def main():
    val = True

    while val:
        for ev in py.event.get():
            if ev.type == py.QUIT()
                val = False
                break
            draw()

if __name__ == "__name__":
    main()

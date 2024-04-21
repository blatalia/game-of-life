import matplotlib.pyplot as plt
import matplotlib.animation as animation
import logic

option = input("Welcome to Game of Life!\nChoose which option you want to display.\nFor a random display enter 1\nFor glider enter 2\nFor pulsar enter 3\nFor gosper glider gun enter 4\n")

if option == "1":

    fig, ax = plt.subplots(figsize=(7, 7))
    im = ax.imshow(logic.random_drawing, cmap = 'magma')
    im.set_clim(vmin = 0, vmax = 1)


    def update(i):
        im.set_data(logic.gameoflife(logic.random_drawing, logic.height_random, logic.width_random))
        return im,

    ani = animation.FuncAnimation(fig, update, interval = 200, blit = True)

    plt.axis('off')
    plt.draw()
    plt.show()

elif option == "2":

    fig, ax = plt.subplots(figsize=(7, 7))
    im = ax.imshow(logic.glider_matrix, cmap = 'magma')
    im.set_clim(vmin = 0, vmax = 1)


    def update(i):
        im.set_data(logic.gameoflife(logic.glider_matrix, logic.height_glider, logic.width_glider))
        return im,

    ani = animation.FuncAnimation(fig, update, interval = 200, blit = True)

    plt.axis('off')
    plt.draw()
    plt.show()

elif option == "3":

    fig, ax = plt.subplots(figsize=(7, 7))
    im = ax.imshow(logic.pulsar_matrix, cmap = 'magma')
    im.set_clim(vmin = 0, vmax = 1)


    def update(i):
        im.set_data(logic.gameoflife(logic.pulsar_matrix, logic.height_pulsar, logic.width_pulsar))
        return im,

    ani = animation.FuncAnimation(fig, update, interval = 200, blit = True)

    plt.axis('off')
    plt.draw()
    plt.show()

elif option == "4":

    fig, ax = plt.subplots(figsize=(7, 7))
    im = ax.imshow(logic.gosper_matrix, cmap = 'magma')
    im.set_clim(vmin = 0, vmax = 1)


    def update(i):
        im.set_data(logic.gameoflife(logic.gosper_matrix, logic.height_gosper, logic.width_gosper))
        return im,

    ani = animation.FuncAnimation(fig, update, interval = 100, blit = True)

    plt.axis('off')
    plt.draw()
    plt.show()
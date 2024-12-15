import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around
            total = int(
                (
                    grid[i, (j - 1) % N]
                    + grid[i, (j + 1) % N]
                    + grid[(i - 1) % N, j]
                    + grid[(i + 1) % N, j]
                    + grid[(i - 1) % N, (j - 1) % N]
                    + grid[(i - 1) % N, (j + 1) % N]
                    + grid[(i + 1) % N, (j - 1) % N]
                    + grid[(i + 1) % N, (j + 1) % N]
                )
                / 255
            )

            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img


# set grid size
N = 100
# set animation update interval
updateInterval = 50
# set grid values: ON=255, OFF=0
ON = 255
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation="nearest")
ani = animation.FuncAnimation(
    fig,
    update,
    fargs=(
        img,
        grid,
        N,
    ),
    frames=10,
    interval=updateInterval,
    save_count=50,
)

# set output file
ani.save("conway_game_of_life.mp4", fps=30, extra_args=["-vcodec", "libx264"])

plt.show()

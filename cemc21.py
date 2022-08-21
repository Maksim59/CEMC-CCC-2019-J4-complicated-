listh = []
listv = []
grid1 = []
grid2 = []
grid1_12 = []
grid2_1 = []


a = input("")
grid = input()

grid = grid.split(',')

for j in grid:
    j = int(j)
    grid2.append(j)


for i in a:
    if i == 'v':
        listv.append(i)
    elif i == 'h':
        listh.append(i)

gridl = len(grid2)
lengthh = len(listh)
lengthv = len(listv)
moduloh = lengthh % 2
modulov = lengthv % 2
half = gridl / 2
half = int(half)

def equal():
    print(grid2)
    return

def notequal():
    new_grid = grid2[::-1]
    print(new_grid)
    return


def v_win(grid2_1, grid1_12):
    for k in range(half):
        grid1_12.append(grid2[k])
    grid2_1.append(grid2[half:half*2])
    grid2_1 = grid2_1[0]
    for m in range(len(grid2_1)-1):
        grid2_1 = grid2_1[::-1]
        grid1_12 = grid1_12[::-1]
    print(grid2_1)
    print(grid1_12)

    return
def h_win(grid2_1, grid1_12):
    grid2_1.append(grid2[::2])
    grid2_1 = grid2_1[0]
    grid1_12.append(grid2[1::2])
    grid1_12 = grid1_12[0]
    print(grid1_12)
    print(grid2_1)

    return




if lengthv % 2 == 0 and lengthh % 2 == 0:
    equal()
elif modulov != 0 and moduloh != 0:
    notequal()
elif modulov != 0 and moduloh == 0:
    v_win(grid2_1, grid1_12)
elif moduloh != 0 and modulov == 0:
    h_win(grid2_1, grid1_12)




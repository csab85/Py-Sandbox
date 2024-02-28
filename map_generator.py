#VARIABLES
#region

mapX : int
mapY : int

#endregion

#GENERATION RULES
#region

mapX = int(input('Map X')) 
mapY = int(input('Map Y'))

#endregion

#MAP PRINTING
for y in range(mapY):
    for x in range(mapX):
        if x < mapX - 1:
            print('A', end = '')
        else:
            print('A')
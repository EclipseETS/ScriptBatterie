import random

class Cells(object):
    
    def __init__(self, box, number, capacity, intRes):
        """Constructeur de notre classe"""
        self.box = box
        self.number = number
        self.capacity = capacity
        self.intRes = intRes

moduleQty = int(input("Nombre de module?"))
cellQty = int(input("Nombre de Cellules par module?"))
packCellQty = moduleQty*cellQty
        
#generate random value
# need to be replaced by file parsing
cells_list = []
boxQty = 20
boxCellQty = 30
totCellQty = boxQty*boxCellQty
for boxIndex in range (1,boxQty+1):
    for numberIndex in range (1,boxCellQty+1):
        rCap=random.randint(3200,3350)
        rIntRes=random.randint(20,80)
        cells_list.append(Cells(boxIndex,numberIndex,rCap,rIntRes))
        
#class cells capacity by ascending order
ascended_cells_list = sorted(cells_list, key=lambda c: c.capacity)

#remove cells with the worst capacity
best_cells = []
for i in range (0,packCellQty):
    best_cells.append(ascended_cells_list[i+(totCellQty-packCellQty)])

#split the list in 11 list of moduleQty
capacity_group = []
for i in range(0, len(best_cells), moduleQty):
        capacity_group.append(best_cells[i:i+moduleQty])

#class internal resistance by ascending order for each group  
for i in range (0,len(capacity_group)):
    capacity_group[i] = sorted(capacity_group[i], key=lambda c: c.intRes)


#Make module by matching the internal resistance of each capacity group
Module_list = []
module = []
for i in range (0,moduleQty):
    for j in range (0,cellQty):
        module.append(capacity_group[j][i])
    Module_list.append(module)
    module = [] #clear module

# print the result
summ = 0
print("Cell#--capacity--internal resistence")
for i in range (0,len(Module_list)):
    print("---------------------Module #",i," :")  
    for cells in Module_list[i]:
        summ = summ+cells.capacity
        print ("#",cells.box,"-",cells.number," ",cells.capacity," ",cells.intRes)
    print("capacité total:",summ)
    summ = 0 
      




                          

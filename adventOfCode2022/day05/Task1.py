import re

initialStack1 = ["F", "H", "M", "T", "V", "L", "D"]
initialStack2 = ["P", "N", "T", "C", "J", "G", "Q", "H"]
initialStack3 = ["H", "P", "M", "D", "S", "R"]
initialStack4 = ["F", "V", "B", "L"]
initialStack5 = ["Q", "L", "G", "H", "N"]
initialStack6 = ["P", "M", "R", "G", "D", "B", "W"]
initialStack7 = ["Q", "L", "H", "C", "R", "N", "M", "G"]
initialStack8 = ["W", "L", "c"]
initialStack9 = ["T", "M", "Z", "J", "Q", "L", "D", "R"]

data = [x.strip() for x in open('Dataset.txt', 'r')]
for index, line in enumerate(data):
    if index > 9:
        print(index)
        rearrangementProcedure = re.sub('\D', ' ', line).split()
        numberOfMoves = 0
        while int(rearrangementProcedure[0]) > numberOfMoves:
            numberOfMoves += 1
            if int(rearrangementProcedure[1]) == 1:
                if int(rearrangementProcedure[2]) == 2:
                    initialStack2.insert(0, initialStack1[0])
                elif int(rearrangementProcedure[2]) == 3:
                    initialStack3.insert(0, initialStack1[0])
                elif int(rearrangementProcedure[2]) == 4:
                    initialStack4.insert(0, initialStack1[0])
                elif int(rearrangementProcedure[2]) == 5:
                    initialStack5.insert(0, initialStack1[0])
                elif int(rearrangementProcedure[2]) == 6:
                    initialStack6.insert(0, initialStack1[0])
                elif int(rearrangementProcedure[2]) == 7:
                    initialStack7.insert(0, initialStack1[0])
                elif int(rearrangementProcedure[2]) == 8:
                    initialStack8.insert(0, initialStack1[0])
                elif int(rearrangementProcedure[2]) == 9:
                    initialStack9.insert(0, initialStack1[0])
                initialStack1.pop(0)
            elif int(rearrangementProcedure[1]) == 2:
                if int(rearrangementProcedure[2]) == 1:
                    initialStack1.insert(0, initialStack2[0])
                elif int(rearrangementProcedure[2]) == 3:
                    initialStack3.insert(0, initialStack2[0])
                elif int(rearrangementProcedure[2]) == 4:
                    initialStack4.insert(0, initialStack2[0])
                elif int(rearrangementProcedure[2]) == 5:
                    initialStack5.insert(0, initialStack2[0])
                elif int(rearrangementProcedure[2]) == 6:
                    initialStack6.insert(0, initialStack2[0])
                elif int(rearrangementProcedure[2]) == 7:
                    initialStack7.insert(0, initialStack2[0])
                elif int(rearrangementProcedure[2]) == 8:
                    initialStack8.insert(0, initialStack2[0])
                elif int(rearrangementProcedure[2]) == 9:
                    initialStack9.insert(0, initialStack2[0])
                initialStack2.pop(0)
            elif int(rearrangementProcedure[1]) == 3:
                if int(rearrangementProcedure[2]) == 2:
                    initialStack2.insert(0, initialStack3[0])
                elif int(rearrangementProcedure[2]) == 1:
                    initialStack1.insert(0, initialStack3[0])
                elif int(rearrangementProcedure[2]) == 4:
                    initialStack4.insert(0, initialStack3[0])
                elif int(rearrangementProcedure[2]) == 5:
                    initialStack5.insert(0, initialStack3[0])
                elif int(rearrangementProcedure[2]) == 6:
                    initialStack6.insert(0, initialStack3[0])
                elif int(rearrangementProcedure[2]) == 7:
                    initialStack7.insert(0, initialStack3[0])
                elif int(rearrangementProcedure[2]) == 8:
                    initialStack8.insert(0, initialStack3[0])
                elif int(rearrangementProcedure[2]) == 9:
                    initialStack9.insert(0, initialStack3[0])
                initialStack3.pop(0)
            elif int(rearrangementProcedure[1]) == 4:
                if int(rearrangementProcedure[2]) == 2:
                    initialStack2.insert(0, initialStack4[0])
                elif int(rearrangementProcedure[2]) == 1:
                    initialStack1.insert(0, initialStack4[0])
                elif int(rearrangementProcedure[2]) == 3:
                    initialStack3.insert(0, initialStack4[0])
                elif int(rearrangementProcedure[2]) == 5:
                    initialStack5.insert(0, initialStack4[0])
                elif int(rearrangementProcedure[2]) == 6:
                    initialStack6.insert(0, initialStack4[0])
                elif int(rearrangementProcedure[2]) == 7:
                    initialStack7.insert(0, initialStack4[0])
                elif int(rearrangementProcedure[2]) == 8:
                    initialStack8.insert(0, initialStack4[0])
                elif int(rearrangementProcedure[2]) == 9:
                    initialStack9.insert(0, initialStack4[0])
                initialStack4.pop(0)
            elif int(rearrangementProcedure[1]) == 5:
                if int(rearrangementProcedure[2]) == 2:
                    initialStack2.insert(0, initialStack5[0])
                elif int(rearrangementProcedure[2]) == 1:
                    initialStack1.insert(0, initialStack5[0])
                elif int(rearrangementProcedure[2]) == 4:
                    initialStack4.insert(0, initialStack5[0])
                elif int(rearrangementProcedure[2]) == 3:
                    initialStack3.insert(0, initialStack5[0])
                elif int(rearrangementProcedure[2]) == 6:
                    initialStack6.insert(0, initialStack5[0])
                elif int(rearrangementProcedure[2]) == 7:
                    initialStack7.insert(0, initialStack5[0])
                elif int(rearrangementProcedure[2]) == 8:
                    initialStack8.insert(0, initialStack5[0])
                elif int(rearrangementProcedure[2]) == 9:
                    initialStack9.insert(0, initialStack5[0])
                initialStack5.pop(0)
            elif int(rearrangementProcedure[1]) == 6:
                if int(rearrangementProcedure[2]) == 2:
                    initialStack2.insert(0, initialStack6[0])
                elif int(rearrangementProcedure[2]) == 1:
                    initialStack1.insert(0, initialStack6[0])
                elif int(rearrangementProcedure[2]) == 4:
                    initialStack4.insert(0, initialStack6[0])
                elif int(rearrangementProcedure[2]) == 5:
                    print(initialStack6)
                    initialStack5.insert(0, initialStack6[0])
                elif int(rearrangementProcedure[2]) == 3:
                    initialStack3.insert(0, initialStack6[0])
                elif int(rearrangementProcedure[2]) == 7:
                    initialStack7.insert(0, initialStack6[0])
                elif int(rearrangementProcedure[2]) == 8:
                    initialStack8.insert(0, initialStack6[0])
                elif int(rearrangementProcedure[2]) == 9:
                    initialStack9.insert(0, initialStack6[0])
                initialStack6.pop(0)
            elif int(rearrangementProcedure[1]) == 7:
                if int(rearrangementProcedure[2]) == 2:
                    initialStack2.insert(0, initialStack7[0])
                elif int(rearrangementProcedure[2]) == 1:
                    initialStack1.insert(0, initialStack7[0])
                elif int(rearrangementProcedure[2]) == 4:
                    initialStack4.insert(0, initialStack7[0])
                elif int(rearrangementProcedure[2]) == 5:
                    initialStack5.insert(0, initialStack7[0])
                elif int(rearrangementProcedure[2]) == 6:
                    initialStack6.insert(0, initialStack7[0])
                elif int(rearrangementProcedure[2]) == 3:
                    initialStack3.insert(0, initialStack7[0])
                elif int(rearrangementProcedure[2]) == 8:
                    initialStack8.insert(0, initialStack7[0])
                elif int(rearrangementProcedure[2]) == 9:
                    initialStack9.insert(0, initialStack7[0])
                initialStack7.pop(0)
            elif int(rearrangementProcedure[1]) == 8:
                if int(rearrangementProcedure[2]) == 2:
                    initialStack2.insert(0, initialStack8[0])
                elif int(rearrangementProcedure[2]) == 1:
                    initialStack1.insert(0, initialStack8[0])
                elif int(rearrangementProcedure[2]) == 4:
                    initialStack4.insert(0, initialStack8[0])
                elif int(rearrangementProcedure[2]) == 5:
                    initialStack5.insert(0, initialStack8[0])
                elif int(rearrangementProcedure[2]) == 6:
                    initialStack6.insert(0, initialStack8[0])
                elif int(rearrangementProcedure[2]) == 7:
                    initialStack7.insert(0, initialStack8[0])
                elif int(rearrangementProcedure[2]) == 3:
                    initialStack3.insert(0, initialStack8[0])
                elif int(rearrangementProcedure[2]) == 9:
                    initialStack9.insert(0, initialStack8[0])
                initialStack8.pop(0)
            elif int(rearrangementProcedure[1]) == 9:
                if int(rearrangementProcedure[2]) == 2:
                    initialStack2.insert(0, initialStack9[0])
                elif int(rearrangementProcedure[2]) == 1:
                    initialStack1.insert(0, initialStack9[0])
                elif int(rearrangementProcedure[2]) == 4:
                    initialStack4.insert(0, initialStack9[0])
                elif int(rearrangementProcedure[2]) == 5:
                    initialStack5.insert(0, initialStack9[0])
                elif int(rearrangementProcedure[2]) == 6:
                    initialStack6.insert(0, initialStack9[0])
                elif int(rearrangementProcedure[2]) == 7:
                    initialStack7.insert(0, initialStack9[0])
                elif int(rearrangementProcedure[2]) == 8:
                    initialStack8.insert(0, initialStack9[0])
                elif int(rearrangementProcedure[2]) == 3:
                    initialStack3.insert(0, initialStack9[0])
                initialStack9.pop(0)
print(initialStack1)
print(initialStack2)
print(initialStack3)
print(initialStack4)
print(initialStack5)
print(initialStack6)
print(initialStack7)
print(initialStack8)
print(initialStack9)



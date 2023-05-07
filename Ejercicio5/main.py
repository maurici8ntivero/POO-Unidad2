from clasePlanAhorro import PlanAhorro
from claseMenu import Menu
import csv



if __name__=="__main__":
    lista=[]
    with open("planes.csv","r") as planes:
        reader=csv.reader(planes, delimiter=";")
        for plan in reader:
            lista.append(PlanAhorro(
                int(plan[0]),plan[1],plan[2],int(plan[3])
            ))
    Menu(lista)
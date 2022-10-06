
import math
import sys
import pandas as pan


print(pan.__version__ +" pandas")


db = pan.read_csv("./inf.csv")
p1 = db['fernan']
p2 = db['bloku']
p3 = db['plokun']
p4 = db['ayleen']

print(db)

    



z=input("ingresa las personas a comparar con formato (px) persona 1:")
y=input("ingresa las personas a comparar con formato (px) persona 2:")

def caos (r0,r9): 

    if(r0=="p1")and(r9=="p2"):
    
        ab = int((p1[0]*p2[0])+(p1[1]*p2[1])+(p1[2]*p2[2])+(p1[3]*p2[3]))
        af = int(math.sqrt((p1[0]**2)+(p1[1]**2)+(p1[2]**2)+(p1[3]**2)))
        bf = int(math.sqrt((p2[0]**2)+(p2[1]**2)+(p2[2]**2)+(p2[3]**2)))
    
    elif(r0=="p2")and(r9=="p1"):
        
        ab = int((p1[0]*p2[0])+(p1[1]*p2[1])+(p1[2]*p2[2])+(p1[3]*p2[3]))
        af = int(math.sqrt((p1[0]**2)+(p1[1]**2)+(p1[2]**2)+(p1[3]**2)))
        bf = int(math.sqrt((p2[0]**2)+(p2[1]**2)+(p2[2]**2)+(p2[3]**2)))
        
    elif(r0=="p2")and(r9=="p3"):
        
        ab = int((p2[0]*p3[0])+(p2[1]*p3[1])+(p2[2]*p3[2])+(p2[3]*p3[3]))
        af = int(math.sqrt((p2[0]**2)+(p2[1]**2)+(p2[2]**2)+(p2[3]**2)))
        bf = int(math.sqrt((p3[0]**2)+(p3[1]**2)+(p3[2]**2)+(p3[3]**2)))
        
    elif(r0=="p3")and(r9=="p2"):
        
        ab = int((p2[0]*p3[0])+(p2[1]*p3[1])+(p2[2]*p3[2])+(p2[3]*p3[3]))
        af = int(math.sqrt((p2[0]**2)+(p2[1]**2)+(p2[2]**2)+(p2[3]**2)))
        bf = int(math.sqrt((p3[0]**2)+(p3[1]**2)+(p3[2]**2)+(p3[3]**2)))
    
    elif(r0=="p3")and(r9=="p4"):
        
        ab = int((p3[0]*p4[0])+(p3[1]*p4[1])+(p3[2]*p4[2])+(p3[3]*p4[3]))
        af = int(math.sqrt((p3[0]**2)+(p3[1]**2)+(p3[2]**2)+(p3[3]**2)))
        bf = int(math.sqrt((p4[0]**2)+(p4[1]**2)+(p4[2]**2)+(p4[3]**2)))
        
    elif(r0=="p4")and(r9=="p3"):
        
        ab = int((p3[0]*p4[0])+(p3[1]*p4[1])+(p3[2]*p4[2])+(p3[3]*p4[3]))
        af = int(math.sqrt((p3[0]**2)+(p3[1]**2)+(p3[2]**2)+(p3[3]**2)))
        bf = int(math.sqrt((p4[0]**2)+(p4[1]**2)+(p4[2]**2)+(p4[3]**2)))
    
    elif(r0=="p4")and(r9=="p1"):
        
        ab = int((p4[0]*p1[0])+(p4[1]*p1[1])+(p4[2]*p1[2])+(p4[3]*p1[3]))
        af = int(math.sqrt((p4[0]**2)+(p4[1]**2)+(p4[2]**2)+(p4[3]**2)))
        bf = int(math.sqrt((p1[0]**2)+(p1[1]**2)+(p1[2]**2)+(p1[3]**2)))
        
    elif(r0=="p1")and(r9=="p4"):
        
        ab = int((p4[0]*p1[0])+(p4[1]*p1[1])+(p4[2]*p1[2])+(p4[3]*p1[3]))
        af = int(math.sqrt((p4[0]**2)+(p4[1]**2)+(p4[2]**2)+(p4[3]**2)))
        bf = int(math.sqrt((p1[0]**2)+(p1[1]**2)+(p1[2]**2)+(p1[3]**2)))
        
    elif(r0=="p1")and(r9=="p3"):
        
        ab = int((p1[0]*p3[0])+(p1[1]*p3[1])+(p1[2]*p3[2])+(p1[3]*p3[3]))
        af = int(math.sqrt((p1[0]**2)+(p1[1]**2)+(p1[2]**2)+(p1[3]**2)))
        bf = int(math.sqrt((p3[0]**2)+(p3[1]**2)+(p3[2]**2)+(p3[3]**2)))
        
    elif(r0=="p3")and(r9=="p1"):
        
        ab = int((p1[0]*p3[0])+(p1[1]*p3[1])+(p1[2]*p3[2])+(p1[3]*p3[3]))
        af = int(math.sqrt((p1[0]**2)+(p1[1]**2)+(p1[2]**2)+(p1[3]**2)))
        bf = int(math.sqrt((p3[0]**2)+(p3[1]**2)+(p3[2]**2)+(p3[3]**2)))
    
    elif(r0=="p2")and(r9=="p4"):
        
        ab = int((p2[0]*p4[0])+(p2[1]*p4[1])+(p2[2]*p4[2])+(p2[3]*p4[3]))
        af = int(math.sqrt((p2[0]**2)+(p2[1]**2)+(p2[2]**2)+(p2[3]**2)))
        bf = int(math.sqrt((p4[0]**2)+(p4[1]**2)+(p4[2]**2)+(p4[3]**2)))
        
    elif(r0=="p4")and(r9=="p2"):
        
        ab = int((p2[0]*p4[0])+(p2[1]*p4[1])+(p2[2]*p4[2])+(p2[3]*p4[3]))
        af = int(math.sqrt((p2[0]**2)+(p2[1]**2)+(p2[2]**2)+(p2[3]**2)))
        bf = int(math.sqrt((p4[0]**2)+(p4[1]**2)+(p4[2]**2)+(p4[3]**2)))
        
    else:
        print("no")
    
    zi = ab/(af*bf)
    return(zi)

sys.modules[__name__] = caos()

print("--------------------------------------------")
print("la comparacion aritmetosa es")
print(caos(z,y))

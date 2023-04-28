import math
import random
#co0rd: lista suntetagmenon
#param: parametroi metasximatismou 

#metathesi
def translation(coord ,cor):
    coord_t=[[0,0]]*(len(coord)+1)#voithitikos pinakas coord'
    for i in range(len(coord)):
        coord_t[i]=[coord[i][0]+cor[0],coord[i][1]+cor[1]]
    return coord_t
#strofi
def rotation(coord,angle):
    coord_t=[[0,0]]*(len(coord)+1)#voithitikos pinakas coord'
    pi=3.141592653589
    for i in range(len(coord)):
            coord_t[i]=[(round(coord[i][0]*math.cos(angle*pi/180)-coord[i][1]*math.sin(angle*pi/180),3)),round(coord[i][0]*math.sin(angle*pi/180)+coord[i][1]*math.cos(angle*pi/180),3)]#perasma apotelesmatos kathe zevgariou ston coord' me orio 3 dekadika 
    return coord_t
'''  
We know that, 
x = rcosB, y = rsinB
x’ = rcos(A+B) = r(cosAcosB – sinAsinB) = rcosBcosA – rsinBsinA = xcosA – ysinA 
y’ = rsin(A+B) = r(sinAcosB + cosAsinB) = rcosBsinA + rsinBcosA = xsinA + ycosA
Rotational Matrix Equation:- 
def rotate(a, n, x_pivot, y_pivot, angle):
    i = 0
    while (i < n) :
        # Shifting the pivot point to the origin
        # and the given points accordingly
        x_shifted = a[i][0] - x_pivot
        y_shifted = a[i][1] - y_pivot
 
        # Calculating the rotated point co-ordinates
        # and shifting it back
        a[i][0] = x_pivot + (x_shifted * COS(angle) - y_shifted * SIN(angle))
        a[i][1] = y_pivot + (x_shifted * SIN(angle) + y_shifted * COS(angle))
        print("({}, {}) ".format(a[i][0], a[i][1]),end=" ")
        i+=1
'''
#allagi klimakas
def scale(coord,sc):
    coord_t=[[0,0]]*(len(coord)+1) #voithitikos pinakas coord'
    for i in range(len(coord)):
        coord_t[i]=[round(coord[i][0]*sc,3),round(coord[i][1]*sc,3)]#perasma apotelesmatos kathe zevgariou ston coord' me orio 3 dekadika 
    return coord_t

''' affine transformation can be decomposed
into a rotation, followed by a scaling, followed by a
shearing, and followed by a translation'''
#affinikos
def affine(coord,params):
    x=rotation(coord,params[0]) 
    y=scale(x,params[1])  
    z=translation(y,params[2])
    return z
#omoiotitas
def similarity(coord,params):
    return coord
#provolikos
def projective(coord,params):
    return coord
#voithitiki gia na kanei ola ta print
def printa(coord,params,trans,coord_t):
    print("After %s transformation the results are: "% trans)
    for i in range(len(coord)):
        print("from "+"("+str(coord[i][0])+","+str(coord[i][1])+")"+" to "+"("+str(coord_t[i][0])+","+str(coord_t[i][1])+")")     
    if(trans == "Translation"):
        print("Using for parameters xt: %d , yt: %d"% (params[0],params[1]))
    elif(trans == "Scale"):
        print("Using for parameters scale: %d"% params)
    elif(trans == "Rotation"):
        print("Using for parameters Rotation: %d"% params)
    elif(trans == "Affine"):
        print()
    elif(trans == "Projective"):
        print()
    elif(trans == "Similarity"):
        print()
    else:    
        print("Using for parameters")
#ergaleiothiki
def toolbox(coord,params):
    
    angle = params[0]
    sc = params[1]
    cor = params[2]
    printa(coord,cor,"Translation",translation(coord,cor))
    printa(coord,angle,"Rotation",rotation(coord,angle))
    printa(coord,sc,"Scale",scale(coord,sc))
    printa(coord,[angle,sc,cor],"Affine",affine(coord,[angle,sc,cor]))
    scale(coord,sc)
    rotation(coord,angle)
    
    
#params = [angle,scale,coord_t] etsi kratao tous parametrous gia na tous metafero metaksi methods
def main():
    point_data=[]
    coord=[]
    #anoigo arxeio gia na diavaso
    with open("point_data.txt") as f:
        lines = f.readlines()
    for line in lines:
        point_data.append(line.split())
    point_data.pop(0) #"travao" ta dedomena afaironta tin proti grami (id,xcoord, ycoord) gia na min enoxlei 
    for data in point_data:
        id=data[0]
        coord.append([float(data[1]),float(data[2])])#perno auta pou me endiaferoun (xcoord,ycoord) se enan pinaka coord
        rangle=random.randrange(-360,360)#tuxaia gonia gia rotation
        rscale=random.randrange(1,150)#tuxaio scale gia allagi megethous
        rcord_t=[random.randrange(0,150),random.randrange(0,150)]#tuxaia x,y gia translation
        params=[rangle,rscale,rcord_t]#tuxaioi parametroi gia to affine 
    toolbox(coord,params)
main()
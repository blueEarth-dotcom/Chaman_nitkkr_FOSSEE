#print('hello chaman ') FOSSEE 2025 @NIT_kurukshetra


class bm_Data:
    def __init__(self): 
        self.L=float(input("Enter length of the beam in metre: "))
        self.w1=float(input("Enter load w1 in KN: "))
        self.w2=float(input("Enter load w2 in KN: "))
        self.x=float(input("Enter distance between w1 and w2: "))


beamdata=bm_Data()

def Reacn(beamdata,a=0):
    ord_1=(beamdata.L-a)/beamdata.L
    ord_2=(beamdata.L-(a+beamdata.x))/beamdata.L
    Rx_A = beamdata.w1*ord_1+beamdata.w2*ord_2
    Rx_B = beamdata.w1+ beamdata.w2-Rx_A #1 more way
    return Rx_A,Rx_B


def max_Rxn(beamdata):
    max_rxa=0.0
    max_rxb=0.0
   
    for a in range (0,int(beamdata.L+1)):
       
        Rx_A,Rx_B=Reacn(beamdata,a)
        if Rx_A>max_rxa and Rx_A<=(beamdata.w1+beamdata.w2):
            max_rxa=Rx_A
            pos_a=a
        
        if Rx_B>max_rxb and Rx_B<=(beamdata.w1+beamdata.w2): 
            max_rxb=Rx_B
            pos_b=a
                
    print(f"\nMaximum Rx_A: {max_rxa:.2f} KN @ w1 at {pos_a} m ")
    print(f"Maximum Rx_B: {max_rxb:.2f} KN @ w1 at {pos_b} m ")

max_Rxn(beamdata)


def BM_01(beamdata,s):
    if s<beamdata.x:
        bm_ord2=(beamdata.L-beamdata.x)*(s*(beamdata.L-s))/(beamdata.L*beamdata.L)
    else:   
     bm_ord2=(beamdata.L-s)*beamdata.x/beamdata.L
    bm = beamdata.w1*0+beamdata.w2*bm_ord2
    return round(bm,2)

lis_BM_01=[]
for  s in range(0,int(beamdata.L+1)):
    lis_BM_01.append(BM_01(beamdata,s))
    
print(f"BM_01 at w1=0 m is: {lis_BM_01}")


def SF_01(beamdata,t):  

    ord_1= t/beamdata.L
    ord_2= (t+beamdata.x)/beamdata.L

    if (t)<0.5*beamdata.L:
         Sf=  -(beamdata.w1*ord_1 + beamdata.w2*ord_2)
    elif (t>0.5*beamdata.L and t+beamdata.x<=beamdata.L): 
         Sf= (beamdata.w2*(1-ord_1) + beamdata.w1*(1-ord_2))
    else:
        Sf=((-beamdata.w1*(ord_2) + beamdata.w2*(1-ord_1)))

    return round(Sf,2)


lis_SF_01=[]
for t in range(0,int(beamdata.L+1-beamdata.x)):
    lis_SF_01.append((SF_01(beamdata,t)))

print("SF_01 at mid-span is:",lis_SF_01)   



def max_BM(beamdata):
    max_val=0.00
    for y in range(0,int(beamdata.L+1)): 
        ord_1= y*(beamdata.L-y)/beamdata.L
        ord_2= (y+beamdata.x)*(beamdata.L-(y+beamdata.x))/beamdata.L
        Bm_y= (beamdata.w1*ord_1 + beamdata.w2*ord_2)
        

        if Bm_y>max_val:
            max_val=round(Bm_y,2)
            pos_y=y
        
            
    print(f"max BM is {max_val:.2f}  kN-m and position y from left support is {pos_y} m\n")


 

def max_SF(beamdata):
    max_val=0.00
    for z in range(0,int(beamdata.L+1)): 
        ord_1= z/beamdata.L
        ord_2= (z+beamdata.x)/beamdata.L
        if z>0.5*beamdata.L:
         Sf_z= (beamdata.w1*ord_1 + beamdata.w2*ord_2)
        else:
         Sf_z= (beamdata.w2*ord_1 + beamdata.w1*ord_2)
       

        if Sf_z>max_val:
            max_val=Sf_z
            pos_z=z
    print(f"\nmax SF is {max_val:.2f} kN and position z from left support is {pos_z:} m")

max_SF(beamdata)
max_BM(beamdata)
    
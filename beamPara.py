#print('hello chaman ')

class bm_Data:
    def __init__(self): 
        self.L=float(input("Enter length of the beam in metre: "))
        self.w1=float(input("Enter load w1 in KN: "))
        self.w2=float(input("Enter load w2 in KN: "))
        self.x=float(input("Enter distance between w1 and w2: "))
        self.a=0.00


beamdata=bm_Data()


def Reacn(beamdata):
    ord_1=(beamdata.L-beamdata.a)/beamdata.L
    ord_2=(beamdata.a)/beamdata.L
    Rx_A = beamdata.w1*ord_1+beamdata.w2*ord_2
    Rx_B = beamdata.w1+ beamdata.w2-Rx_A #1 more way
    return Rx_A,Rx_B
 
ab=Reacn(beamdata) #(17.4, 12.6) <class 'tuple'>
# print(ab,type(ab)) #type of two output by a function is class 'tuple'


def max_Rxn(beamdata):
    max_rxa=0.0
    max_rxb=0.0
   
    for a in range (0,int(beamdata.L+1)):
        # beamdata.a=a
        Rx_A,Rx_B=Reacn(beamdata)
        if Rx_A>max_rxa:
            max_rxa=Rx_A
        
        if Rx_B>max_rxb: 
            max_rxb=Rx_B
                
    print(f"\nMaximum Rx_A: {max_rxa} KN ")
    print(f"Maximum Rx_B: {max_rxb} KN")

max_Rxn(beamdata)


def BM_01(beamdata):
    cs_01=beamdata.x #BM is maximum under the Point Load ; cs_01 is distance of critical section from support A
    bm_ord2=(beamdata.L-cs_01)*beamdata.x/beamdata.L
    bm = beamdata.w1*0+beamdata.w2*bm_ord2
    return bm

def SF_01(beamdata):
    mid_span=0.5*beamdata.L
    ord_1= mid_span/beamdata.L
    ord_2= (mid_span-beamdata.x)/beamdata.L

    if beamdata.w1>=beamdata.w2:
         Sf= (beamdata.w1*ord_1 + beamdata.w2*ord_2)
    else:
         Sf= -(beamdata.w2*ord_1 + beamdata.w1*ord_2)
    return Sf  


 

bms=BM_01(beamdata)
sfs= SF_01(beamdata)
print(f"\nBM_01 is {bms:.2f} kN-m\nSF_01 is {sfs:.2f} kN-m")


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
    
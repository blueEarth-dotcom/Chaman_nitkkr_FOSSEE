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
    Rx_A = beamdata.w1*(beamdata.L-beamdata.a)/beamdata.L +beamdata.w2*(beamdata.L-beamdata.a-beamdata.x)/beamdata.L
    Rx_B = beamdata.w1+ beamdata.w2-Rx_A #1 more way
    return Rx_A,Rx_B
 
ab=Reacn(beamdata) #(17.4, 12.6) <class 'tuple'>
# print(ab,type(ab)) #type of two output by a function is class 'tuple'

# .............................................................................

def max_Rxn(beamdata):
    max_rxa=0.0
    max_rxb=0.0
    max_posA=0.0
    max_posB=0.0
   
    for a in range (0,int(beamdata.L+1)):
        beamdata.a=a
        Rx_A,Rx_B=Reacn(beamdata)
        if Rx_A>max_rxa:
            max_rxa=Rx_A
            max_posA=a
        
        if Rx_B>max_rxb: 
            max_rxb=Rx_B
            max_posB=a
        
    print(f"\n\nMaximum Rx_A: {max_rxa} ")
    print(f"Maximum Rx_B: {max_rxb} ")

max_Rxn(beamdata)
   
def max_RxB():
    pass
#...................................................................................

def BM_01(beamdata,ab):
    bm = -beamdata.w2*beamdata.x + ab[1]
    return bm

def SF_01(beamdata,ab):
    sf = ab[0]-beamdata.w2
    return sf

bms=BM_01(beamdata,ab)
sfs= SF_01(beamdata,ab)
print(f"BM_01 is {bms}\nSF_01 is {sfs}")


def max_BM(beamdata):
    max_val=0
    for y in range(0,int(beamdata.L+1)): 
        ord_1= y*(beamdata.L-y)/beamdata.L
        ord_2= (y+beamdata.x)*(beamdata.L-(y+beamdata.x))/beamdata.L
        Bm_y= (beamdata.w1*ord_1 + beamdata.w2*ord_2)
        

        if Bm_y>max_val:
            max_val=round(Bm_y,2)
            pos_y=y
        
            
    print(f"max BM is {max_val} and position y from left support is {pos_y}")


 

def max_SF(beamdata):
    max_val=0
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
        
            
    print(f"max SF is {max_val} and position y from left support is {pos_z}")

max_SF(beamdata)
max_BM(beamdata)
    
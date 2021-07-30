#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Manasvi Goyal 2K19/PE/034
# Machine Design Project
# Python Program For Longitudinal Butt Joint and Circumferential Lap Joint

import math
Di=float(input("\nEnter internal diameter Di (in metre) : "))
Pi=float(input("\nEnter Steam Pressure Pi (in N/m^2 or MPa): "))
Sut_shell=float(input("\nEnter Ultimate tensile strength Sut for Boiler shell material (in N/m^2 or MPa): "))
Sut_rivet=float(input("\nEnter Ultimate tensile strength Sut for rivet material (in N/m^2 or MPa): "))
Effi = float(input("\nEnter efficiency of longitudinal joint (%): "))
Eff=Effi/100 
# for boilers factor of safety is considered as 5
fos=5 

while True:
    try:
        strap=input("\nAre straps equal or unequal? = ")
        if strap in ['equal', 'Equal', 'EQUAL', 'unequal', 'Unequal', 'UNEQUAL']:
            break
        else:
            print("\nEnter 'equal' or 'unequal'.")
    except:
        continue
        
Sigmat_shell=Sut_shell/fos
SigmaC_shell=1.5*Sigmat_shell
Tau_shell=0.5*Sigmat_shell
Sigmat_rivet=Sut_rivet/fos
SigmaC_rivet=1.5*Sigmat_rivet
Tau_rivet=0.5*Sigmat_rivet

#--------------------------------------------------------------------------------------------------------------------------

# Longitudinal Butt Joint
print('\033[1m' + '\033[4m' + '\033[95m'+ '\n\nLongitudinal Butt Joint')
print('\033[0m')
# assumming triple riveted double strap butt joint
# Thickness of Boiler Shell(t)

# Efficiency of Longitudinal Butt Joint for triple riveted double strap butt joint = 85%

#Corrosion Allowance
CA = 2 
t=(Pi*Di*1000)/(2*Sigmat_shell*Eff) + CA
t=math.ceil(t) 
print('\nThickness of Boiler Shell (t) = ',t,'mm')

# Diameter of Rivet (d)
#Using Unwins's Formula, as t>8mm
d=6*math.sqrt(t)
d=math.ceil(d) 
print('\nDiameter of Rivet (d) = ',d,'mm')

# Pitch of Rivet (p)

print('\nSince, strap = ',strap)

# n1 = number of rivets subjected to single shear per pitch length
# n2 = number of rivets subjected to double shear per pitch length

if strap in ['equal', 'Equal', 'EQUAL'] :
    n1=0
    n2=5
elif strap in ['unequal', 'Unqual', 'UNEQUAL'] :
    n1=1
    n2=4
print('\nnumber of rivets subjected to single shear per pitch length (n1) = ',n1)
print('\nnumber of rivets subjected to double shear per pitch length (n2) = ',n2)

p=(((n1+1.875*n2)*math.pi*pow(d, 2)*Tau_rivet)/(4*t*Sigmat_shell))+d

pmin=2*d
# for double strap butt joint where number of rivets per pitch length is 5
C=6
pmax=C*t+41.28

if p<pmax and p>pmin :
    p=p
elif p<=pmin :
     p=pmin
elif p>=pmax :
     p=pmax
        
p=math.ceil(p) 
print('\nPitch of Rivet in Outer Rows = ',p,'mm')
p_im=p/2
print('\nPitch of Rivet in Inner and Middle Rows = ',p_im,'mm')

# Transverse Pitch (pt)

# The number of rivets in outer row is one half of the number of rivet in middle and inner rows

#distance between outer and middle rows
pt1=0.2*p+1.15*d
pt1=math.ceil(pt1) 
#distance between middle and inner rows
pt2=0.165*p+0.67*d
pt2=math.ceil(pt2) 
print('\ndistance between outer and middle rows = ',pt1,'mm')
print('\ndistance between middle and inner rows = ',pt2,'mm')

# Margin (m)

m=1.5*d
m=math.ceil(m) 
print('\nMargin (m) = ',m,'mm')

# Thickness of straps

if strap == "unequal" :
    t1_inner=0.75*t
    t1_outer=0.625*t
elif strap == "equal" :
    t1_inner=0.625*t*((p-d)/(p-2*d))
    t1_outer = t1_inner

if t1_inner<10 :
    t1_inner=10
if t1_outer<10 :
    t1_outer=10
t1_inner=math.ceil(t1_inner) 
t1_outer=math.ceil(t1_outer)  

print('\nThickness of inner strap = ',t1_inner,'mm')
print('\nThickness of outer strap = ',t1_outer,'mm')

# Efficiency of Longitudinal Butt Joint

# Tensile Strength of shell per pitch length in outer row
Pt=(p-d)*t*Sigmat_shell
print('\nTensile Strength of shell per pitch length in outer row (Pt) = %.2f' %Pt,'N')

# Shear Strength of rivets per pitch length
Ps=(n1+1.875*n2)*(math.pi*pow(d, 2)*Tau_rivet/4)
print('\nShear Strength of rivets per pitch length (Ps) = %.2f' %Ps,'N')

# Crushing Strength of shell
Pc=(n1+n2)*d*t*SigmaC_shell
print('\nCrushing Strength of shell (Pc) = %.2f' %Pc,'N')

# Tensile Strength of shell per pitch length
P_t=p*t*Sigmat_shell
print('\nTensile Strength of shell per pitch length (P) = %.2f' %P_t,'N')
lowest=min(Pt,Ps,Pc)
print('\nThe lowest strength out of Pt, Ps and Pc = %.2f' %lowest,'N')
efficiency_butt=lowest*100/P_t
print('\nEfficiency of Longitudinal Butt Joint = %.2f' %efficiency_butt,'%')

#--------------------------------------------------------------------------------------------------------------------------

# Circumferential Lap Joint
print('\033[1m' + '\033[4m' + '\033[95m'+ '\n\nCircumferential Lap Joint')
print('\033[0m')

# Thickness of Cylindrical Shell and Diameter of Rivet is same as Longitudinal Butt Joint

print('\nThickness of Boiler Shell (t) = ',t,'mm')
print('\nDiameter of Rivet (d) = ',d,'mm')

# Number of Rivets

n=pow(Di*1000/d,2)*Pi/Tau_rivet
n=math.ceil(n) 
print('\nNumber of Rivets (n) = ',n)

# Pitch of Rivets (p1)

Eff1=0.5*Eff
if Eff1<0.42 :
    Eff1=0.42
print('\nEfficiency of Circumferential Joint (n) = ',Eff1,'mm')

p1=d/(1-Eff1)

pmin1=2*d
# for lap joint where number of rivets per pitch length is 1
C=1.31
pmax1=C*t+41.28

if p1<pmax1 and p1>pmin1 :
    p1=p1
elif p1<=pmin1 :
     p1=pmin1
elif p1>=pmax1 :
     p1=pmax1

p1=math.ceil(p1) 
print('\nPitch of Rivets (p1) = ',p1,'mm')

# Number of Rivets in One Row (n1)

n_1 = math.pi*(Di*1000+t)/p1
n_1=math.ceil(n_1) 
print('\nNumber of Rivets in One Row (n1) = ',n_1)

# Number of Rows of Rivets 

nrow=n/n_1
nrow=round(nrow)
print('\nNumber of Rows of Rivets = ',nrow)

if nrow==1:
    print('(This joint is single-riveted lap joint)')
if nrow==2:
    print('(This joint is double-riveted lap joint)')
if nrow==3:
    print('(This joint is triple-riveted lap joint)')
    
# Revised Value of Diameter of Rivet

d=math.sqrt(pow(Di*1000,2)*Pi/(Tau_rivet*n_1*nrow))
d=math.ceil(d) 
print('\nRevised Value of Diameter of Rivet (d) = ',d,'mm')

# Transverse Pitch (pt)

# assuming number of rivets in each row is equal 

if nrow>1 :
    while True:
        try:
            riveting_type=input("\nzig-zag or chain rivetting? = ")
            if riveting_type in ['zig-zag', 'Zig-Zag', 'Zig-zag', 'ZIG-ZAG', 'chain', 'Chain', 'CHAIN']:
                break
            else:
                print("\nEnter 'zig-zag' or 'chain'.")
        except:
            continue

    if riveting_type in ['zig-zag', 'Zig-Zag', 'Zig-zag', 'ZIG-ZAG'] :
        ptrans=0.33*p1+0.67*d
    elif riveting_type in ['chain', 'Chain', 'CHAIN'] :
        ptrans=2*d    
    ptrans=math.ceil(ptrans) 
    print('\nTransverse Pitch (pt) = ',ptrans,'mm')
elif nrow==1 :
    ptrans=0   
print('\nTransverse Pitch (pt) = ',ptrans,'mm')

# Margin (m)

m1=1.5*d
m1=math.ceil(m1) 
print('\nMargin (m) = ',m1,'mm')

# Overlap of Plates (a)

a=ptrans+2*m1
a=math.ceil(a) 
print('\nOverlap of Plates (a) = ',a,'mm')

# Efficiency Check for Design

efficiency_lap=(p1-d)*100/p1
print('\nEfficiency of Circumferential Lap Joint = %.2f' %efficiency_lap,'%\n')

#--------------------------------------------------------------------------------------------------------------------------


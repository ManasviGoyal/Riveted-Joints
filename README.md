<h1 "id="top" align ="center"> Design of Riveted-Joints</h1>

A program to design a longitudinal butt joint and a circumferential lap joint for a boiler shell of any given internal diameter and steam pressure, with the help of Python programming language in Jupyter Notebook. By inputting different values of internal diameter, steam pressure and stresses, this program can be used to design any londitudinal butt joint and circumferential lap joint

## :page_with_curl: Table of Contents
- Riveted Joints
- Riveted Joints in Boiler Shell
- Problem Statement
- Selection of Materials
- Assumptions

## 🔗 Riveted Joints

A rivet is a short cylindrical bar with a head integral to it. The cylindrical
portion of the rivet is called shank or body and lower portion of shank is
known as tail. The rivets are used to make permanent fastening between the
plates such as in structural work, ship building, bridges, tanks and boiler
shells. The riveted joints are widely used for joining light metals. The
function of rivets in a joint is to make a connection that has strength and
tightness.

<h2 id="top" align="center"> <img src="https://user-images.githubusercontent.com/55101825/127709839-628aec47-52d1-4331-be14-7c2341055b50.png"> </h2>

There are two types of riveted joints :- <br><br>
a) **Lap Joint** - A lap joint is that in which one plate overlaps the other and the two plates are then riveted together.<br><br>
b) **Butt Joint** - A butt joint is that in which the main plates are kept in alignment butting each other and a cover plate (i.e. strap) is placed either on one side or on both sides of the main plates. The cover plate is then riveted together with the main plates.<br>

## :chains: Riveted Joints in Boiler Shell

Boilers are cylindrical vessels which are subjected to circumferential and longitudinal tensile stresses Boiler joints are subjected to steam pressure. They should withstand the steam pressure and also prevent leakage. Hence, great care must be exercised in their design and a high standard of workmanship should be provided in their manufacture. Further, the boiler shells are subjected to close inspection, which must conform to the Indian Boiler Regulation Act. <br>

There are two types of riveted joints in a cylindrical boiler shell<br>
a) **Longitudinal Butt Joint** - The plate of the boiler shell is bent to form the ring and the two edges of the plate are joined by a longitudinal butt joint. This longitudinal joint is usually a double-strap triple riveted butt joint. The longitudinal joint makes a ring from the steel plate. The longitudinal joint is stronger than circumferential joint. <br><br>

<h3 id="top" align="center"> <img src="https://user-images.githubusercontent.com/55101825/127710554-b6307a7d-e440-48d8-bcc5-5ec9ba7ef1e8.png"> </h3>
<h3 id="top" align="center"> Triple-Riveted Double-strap Longitudinal Butt Joint with Unequal straps </h3><br>


b) **Circumferential Lap Joint** - The circumferential joint is used to get the required length of the boiler shell by connecting one ring to another. For this purpose, one ring is kept overlapping over the adjacent ring and the two rings are joined by a circumferential. This type of joint is also used to connect the end cover to the cylindrical shell.<br><br>

<h3 id="top" align="center"> <img src="https://user-images.githubusercontent.com/55101825/127710819-c04cb60a-1e9f-4888-955f-87cd2975e155.png"> </h3>
<h3 id="top" align="center"> Double-Riveted Circumferential Lap Joint </h3><br>

## :bulb: Problem Statement

Design a triple riveted zig-zag longitudinal butt joint with double straps of 
unequal width and circumferentional lap joint for steam boiler drum of 
internal diameter 1.8 m to withstand steam pressure 1.5 Mpa, so that 
efficiency does not fall below 75%.

## :nut_and_bolt: Selection of Materials

From data book, 
Material used for boiler shell = Grade 20 Alloy steel (Sut = 480 N/mm2)<br>
Material used for rivets = C15 (medium carbon steel (Sut = 400 N/mm2)<br>
According to Indian Boiler Regulations,<br>
Factor of safety for both boiler shell and rivets = 5<br>

## :shield: Assumptions 

1. The load on the joint is equally shared by all the rivets. The 
assumption implies that the shell and plate are rigid and that all the 
deformation of the joint takes place in the rivets themselves. 
2. The tensile stress is equally distributed over the section of metal 
between the rivets. 
3. The shearing stress in all the rivets is uniform. 
4. The crushing stress is uniform. 
5. There is no bending stress in the rivets. 
6. The holes into which the rivets are driven do not weaken the member. 
7. The rivet fills the hole after it is driven. 
8. The friction between the surfaces of the plate is neglected.


# Particle Based 2D fluid Simulation

This script was developed as a final project after completing the Python Crash Course by Eric Matthes.

Fluid Simulation For Computer Graphics: A Tutorial in Grid Based and Particle Based Methods by Colin Braley et al. 2005. 
https://www.ljll.fr/~frey/papers/levelsets/Clavet%20S.,%20Particle-based%20viscoelastic%20fluid%20simulation.pdf

As an initial draft implementation, a rudimentary formula was used calculate particle interactions, 
force = sum ((1- (rij)/h) **2 )
Essentially a particle will move in the direction with a vector being the sum of its 
distance from each neighbouring particle

The fundamentals of simulating a fluid is that particles are required to maintain constant pressure 
since fluids are incompressible. A good approach to simulating this is forcing the particles to always
move to locations of low pressure. While this approach is more effective for gases,


---
title: "Projects"
permalink: /projects/
classes: wide
font-size: "18px"
---

In my career, I have done various projects and here lists some of them. They range from theoretical physics project to statistical projects. 

### Lepton Isolation Problem with Neural Networks 
<p><img src="{{ site.url }}/assets/images/projects_images/BubbleTracks480.jpeg" alt="image" class="align-left" style="max-width: 330px; margin-top:1em"></p>

In the search for Supersymmetry physics from LHC data, it is important to find the $W$ bosons from gluino pair production. A good indication
is the lepton isolation. Leptons from decay of $W$ bosons are expected to be isolated from other activities while other sources of leptons will give
rise of other accompanying particles. In principle, isolated leptons will leave a track without neighboring tracks in the detector. 
However, this can be contaminated by other particles from other processes in the hadron collision event. Therefore, a good method of subtracting 
contaminated tracks from the isolated electrons will be essential. An important information is the neighboring tracks of lepton track. In this project, 
we utilized this information efficiently by passing them into a deep neural network, which is good at extracting complicated dependencies of the target
on the inputs. 
{: .text-justify}


### Incorporating Effective Potential into FermiNet

<p><img src="{{ site.url }}/assets/images/projects_images/QuantumChemistry.jpeg" alt="image" class="align-left" style="max-width: 330px; margin-top:1em"></p>

Calculation of energy for a given molecule configuration has always been a challenge to scientists. In order to find the energy, people has to
solve the Schr&oumlndinger equation, which becomes quite hard when there are multiple electrons. A variational method has been proposed and behaves
well for simple, uncorrelated molecules. However, when electrons begin to correlate with each other, the Hartree-Fork method breaks down. This is because
the ansatz in the variational process is quite limited. 
[Deepmind proposed an antisymmetric neural network structure (FermiNet)](https://deepmind.com/blog/article/FermiNet) to have more general wave function form
to do the variation. However, due to the large prefactor in its $O(N^4)$ time scaling, the network takes enormous resources to train. In our project, we 
incorporate effective potential that can reduce the number of electrons into the network and by paying some price for the integration time, our method
speeds up FermiNet effectively and especially in transition metals. 
{: .text-justify}


### Lovelock Gravity from Entanglement Entropy

<p><img src="{{ site.url }}/assets/images/projects_images/Entanglement_surface.png" alt="image" class="align-left" style="max-width: 330px; margin-top:1em"></p>

It is widely believed that the quantum gravity theory in a D dimensional spacetime which is asymptotically Anti de Sitter (AdS) is dual to a conformal 
quantum field theory (CFT)  on a D-1 dimensional spacetime. This is called AdS-CFT correspondence. It is often pitured as the quantum field theory lives 
on the bounday of which the dual gravity lives. This is also referred to as holography principle. However, the correspondence is not fully understood and 
people are still trying to find the detailed correspondence or dictionary between the two theories. One is the entanglement entropy between an enclosed region
with the outside is described by the minimal surface area in the bulk by [Ryu-Takayanagi](https://en.wikipedia.org/wiki/Ryu%E2%80%93Takayanagi_conjecture). 
[People have shown that if Ryu-Takayanagi formula holds for small perturbations of the CFT, then the small perturbations mapped to the bulk must obey first order
Einstein gravity](https://link.springer.com/article/10.1007%2FJHEP03%282014%29051). In this project, we improved the order of perturbation. We showed, 
Ryu-Takayanagi formula can give a second order gravity, the Lovelock gravity which becomes Einstein gravity theory in first order perturbation. 
{: .text-justify}


### GRMHD for Neutron Stars and Black Holes


<p><img src="{{ site.url }}/assets/images/projects_images/bhGravityWaves.png" alt="image" class="align-left" style="max-width: 330px; margin-top:1em"></p>

Einstein gravity theory has gained confirmation by the [LIGO detection of gravitational waves](https://www.ligo.org/detections/GW190521.php) from binary 
black holes. However, this not only depends on the infrastructure of the gravitational wave detector but also the numerouse simulation of compact celestial
objects. This includes binary black hole systems, neutron star systems and etc. In the simulation of these compact objects, general relativity has to be
considered and Einstein gravity equation coupled with matter has to be solved. In the Universe, it is common for the matter to be magnetically charged. Thus,
in this project, we used the magnetically charged hydrodynamics coupled to curved spacetime to simulate binary neutron stars and black holes. We analyze the 
behaviour of merger, emission of EM signals and gravitational waves from them. 
{: .text-justify}


### Stability of  Lagrangian Point under Gravitational Radiation  

<p><img src="{{ site.url }}/assets/images/projects_images/Trojandiagram.jpeg" alt="image" class="align-left" style="max-width: 330px; margin-top:1em"></p>

In a binary system consists of a massive center body  and a light satellite, there exist two points on which test particles will corotate with the system, 
i.e., it is stationary in the corotating frame. However, when general relativity effects is considered, the rotation of the binary system will emit gravitional 
waves which  will carry out angular momentum. The decrease of angular momentum will decrease the distance between the satellite and the central body. If the
test particle is also considered as a satellite of the central massive object, the radius of the orbit will also decrease. However, this decrease rate will 
depend on the mass of the satellite. The massive satellite will have larger rate of approaching the center. Thus, it is natrual to ask whether the Trojan
point which results from Newtonian gravity, will continue to exist after a long time of gravitational wave emission. In this project, we did post Newtonian 
simulation for the system and showed the Trojan point is stable until the satellite orbit radius shrinks to around $18M$. 
{: .text-justify}

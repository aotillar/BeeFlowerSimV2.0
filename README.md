**Project Description**
This is a Bee and Flower Simulator made in Python. The goal of this project is
to model ecological behavior of bees and of flowers in a virtual environment.

Any ecological model will have to make choices about the goals, systems it wishes
to model and abstractions made within the model. This model will be a stochastic 
model, with abstractions made in both behavior, and environment. This will not 
be a mathmatical model, instead a programatic model. 

**Goals**
A 2d world that simulates Bee and Flower interactions. 

* Flowers will:
  * Grow, reproduce, change state, evolve,gather resources, absorb sunlight
  transport water, produce pollen and eggs, and die
  
* Bees will:
  * Have full bee hive simulations(Queen, Drone, Pupae States etc), grow old
  and die, forage for food, find flowers and communicate their location to 
  other bees, find flowers that are attractive to them, produce honey, 
  explore their world and more
  
 * The Environment will:
  * Simulate time, temperature, radiation(sunlight), nutrient cycles, 
  spatial heterogeneity of objects, nutrients availability.
  
* This simulation will present all of this information in a GUI developed with the 
QT framework in Pyside2 so that it can be freely distributed under the LGPL license.
The GUI will allow greater interaction with all of the model parameters, as well as
display of important model information. 
  * Various inputs and controlls for all major model parameters
  * SQL Databse + MVC for model entities
  * Biome Selection
  * Export to common file formats
  * Graphical representation of the model objects in a 2d Space
    Plenty of interaction with the Graphics Objects of the model
   
This project Primarily serves as a means to practive python programming, and to 
incorporate some higher level statistics, chemistry, earth science, adn biology
knownledge into a model. My personal goal is to get a masters degree in 
Environmental Science, which many programs use high level sophisticated models
to aid their research. If I can get a head star tnow developing both code and GUI
models, I believe I will go a long way towards achieving my goals.
  

# building class
import math

import pygame

directions ={
"up":{
    "up" : 0,
    "down" : 180,
    "left" : 90,
    "right" : -90
},"down":{
    "up" : 180,
    "down" : 0,
    "left" : -90,
    "right" : 90
},"left":{
    "up" : 270,
    "down" : 90,
    "left" : 0,
    "right" : 180},
"right" :{
    "up" : 90,
    "down" : 270,
    "left" : 180,
    "right" : 0
}}


class Building:
    def __init__(self, name, description,localisation):
        self.name = name
        self.description = description
        self.localisation = localisation
        self.x = localisation[0]
        self.y = localisation[1]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# mission class
class Mission:
    def __init__(self, name, description, localisation, reward):
        self.name = name
        self.description = description
        self.localisation = localisation
        self.reward = reward
        self.x = localisation[0]
        self.y = localisation[1]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

#car class

class Car:
    def __init__(self, name, description,image, localisation):
        self.name = name
        self.description = description
        self.image = image
        self.localisation = localisation
        self.x = localisation[0]
        self.y = localisation[1]
        self.direction = 'up'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def move(self, direction):
        if direction != self.direction:
           angle = directions[self.direction][direction]
           self.image = pygame.transform.rotate(self.image,angle)
           self.direction = direction



#player class
class Player:
    def __init__(self, name, description, localisation):
        self.name = name
        self.description = description
        self.localisation = localisation
        self.x = localisation[0]
        self.y = localisation[1]
        self.car = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def setcar(self,car):
        self.car = car

    def move(self, direction):
        if direction == 'up' or direction == pygame.K_UP:
            direction = 'up'
            self.y -= 1
        elif direction == 'down' or direction == pygame.K_DOWN:
            direction = 'down'
            self.y += 1
        elif direction == 'left' or direction == pygame.K_LEFT:
            direction = 'left'
            self.x -= 1
        elif direction == 'right' or direction == pygame.K_RIGHT:
            direction = 'right'
            self.x += 1
        self.car.move(direction)

#floor surface class
class Surface:
    def __init__(self, name,canWalk,canDrive,carSpeed):
        self.name = name
        self.canWalk = canWalk
        self.canDrive = canDrive
        self.carSpeed = carSpeed


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

#weapon class
class Weapon:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



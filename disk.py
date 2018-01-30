# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:30:03 2018

@author: JKPark
"""

import pygame

class disk:
    def __init__(self, disk_ind, color, disp, disk_d, disk_b):
        self.disk_ind = disk_ind
        self.color = color
        
        self.disk_w = 20 + 25 * (disk_ind)
        self.disk_d = disk_d
        self.disk_b = disk_b
        
        self.disp = disp
        
        
    def draw(self, x, y):
        pygame.draw.rect(self.disp, self.color, (x - self.disk_w / 2, y, self.disk_w, self.disk_d))
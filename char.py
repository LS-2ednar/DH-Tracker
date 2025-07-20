import numpy as np

class Character:
    def __init__(self):
        self.Name = None
        self.Class = None
        self.Heritage = None
        self.Evasion = None
        self.Armor = None
        self.HP = None
        self.Stress = None
        self.Hope = None
        self.Expertise = None
        self.Stats = None
        self.Proficency = None
        self.Weapons = None
        self.Armor = None
        self.Level = None
        self.Domains = None
        self.Background_Questions = None
        self.Connections = None
        self.Gold = None

class Character_Class:
    def __init__(self): 
        self.Class = None
        self.Subclass = None
        self.Features = None

class Heritage:
    def __init__(self):
        self.Race = None
        self.Community = None

class Race:
    def __init__(self):
        self.Multirace = None
        self.Race = None


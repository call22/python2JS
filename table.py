#!/usr/bin/env python3

__author__ = 'longyufeng'

class FuncTable:
    def __init__(self):
        self.functree = {}

    def initTree(self):
        self.functree["print"] = {"type": "console.log", "param": (1, 1)}
        self.functree["input"] = {"type": "prompt", "param": (0, 0)}
        self.functree["int"] = {"type": "parseInt", "param": (1, 1)}
        self.functree["len"] = {"type": "alien", "param": (1, 1)}
        self.functree["append"] = {"type": "push", "param": (1, 1)}
        self.functree["pop"] = {"type": "default", "param": (0, 0)}
        self.functree["range"] = {"type": "default", "param": (2,2)}

    def add(self, name, type, param):
        self.functree[name] = {"type": type, "param": param}

    def find(self, name):
        if self.functree.get(name):
            return self.functree.get(name)
        else:
            return False

class VarTable:
    def __init__(self):
        self.varlist = {}

    def add(self, name, type):
        pass

    def find(self, name):
        pass

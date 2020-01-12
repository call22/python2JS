#!/usr/bin/env python3

__author__ = 'longyufeng'


class funcNode:
    def __init__(self, name, type, param):
        self.name = name
        self.type = type
        self.param = param
        self.subFuncDict = None

# |func| type| param| subfunction[]
#
class FuncTable:

    def __init__(self):
        self.functree = funcNode("all","","")
        self.functree.subFuncDict = {}

    def initTree(self):
        self.functree.subFuncDict["print"] = funcNode("print", "console.log", (1,1))
        self.functree.subFuncDict["input"] = funcNode("input", "prompt", (0,0))
        self.functree.subFuncDict["int"] = funcNode("int", "parseInt", (1,1))
        self.functree.subFuncDict["len"] = funcNode("len", "alien", (1,1))
        self.functree.subFuncDict["append"] = funcNode("append", "push", (1,1))
        self.functree.subFuncDict["pop"] = funcNode("pop", "default", (0,0))
        self.functree.subFuncDict["range"] = funcNode("range", "default", (2,2))

    def add(self, name, type, param, proc: list):
        pre = self.functree
        func = pre.subFuncDict
        for i in proc:
            pre = func[i]
            func = pre.subFuncDict
        ## 不考虑同一作用域下, 两个函数定义同名情况.
        pre.subFuncDict[name] = funcNode(name, type, param)

    def find(self, name, proc: list):
        func = self.functree.subFuncDict
        for i in proc:
            if func.get(name) is not None:
                return True
            func = func[i].subFuncDict
        return False


class VarTable:

    def __init__(self):
        self.varlist = {}

    def add(self, name:str, type, funcRange):
        if self.varlist.get(name) is None:
            self.varlist[name] = [(type, funcRange)]
        else:
            self.varlist.get(name).append((type, funcRange))

    def find(self, name, type, funcRange):
        if self.varlist.get(name) is not None:
            pass


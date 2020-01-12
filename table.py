#!/usr/bin/env python3

__author__ = 'longyufeng'


class funcNode:
    def __init__(self, name, type, param):
        self.name = name
        self.type = type
        self.param = param
        self.subFuncDict = {}
        self.localVar = {}


class localvarNode:
    def __init__(self, name, type):
        self.var_name = name
        self.var_type = type


# |name | type| param| subfunction[]
#--------------------------------------------
# for function, we judge them with limits:
#   1.function name     2. param number     3. scope
#----------------------------------------------
# for variable, we judge them with limits:
#   1. variable name    2. scope
#   judge variable's type is also essential,
#   but now I can't find appropriate method to get it's type.

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
        if func.get(name) is not None:
            return func.get(name)

        for i in proc:
            func = func[i].subFuncDict
            if func.get(name) is not None:
                return func.get(name)
        return False

    def add_var(self, var_name: str, var_type: str, proc: list):
        pre = self.functree
        func = pre.subFuncDict
        for i in proc:
            pre = func[i]
            func = pre.subFuncDict
        pre.localVar[var_name] = localvarNode(var_name, var_type)

    def find_var(self, var_name: str, var_type: str, proc: list):
        func = self.functree
        if func.localVar.get(var_name) is not None:
            return True

        for i in proc:
            func = func.subFuncDict[i]
            if func.localVar.get(var_name) is not None:
                return True
        return False

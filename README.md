### 一、文件结构:

```
filter: 对生成的目标js文件换行符进行处理.(因为python解析时会自动增加换行符).
JSEmitter: 语法解析, 基本错误处理
python2js.py: 主函数
Python3.g4: antlr4语法, 包含词法和语法匹配规则, 参考官方Python3.g4的java版本代码, 实现实验要求的词法和语法分析.
table: 函数和变量符号表.
```

### 二、主要流程:

1. 参考官方Python3.g4的java版本代码, 实现实验要求的词法和语法分析.

2. 使用antlr4工具和Python3.g4文件自动生成基本lexer和parser文件.

3. 继承自动生成的listener文件, 对生成的语法树进行遍历。

   维护一个list列表, 将当前节点对应的代码替换片段存入list列表，类似压栈的形式，遍历完成后最末尾即为转换后的代码。

4. 建立Table类，建立用户自定义函数和语言内置函数的符号表。在语法树遍历时添加维护函数和变量表, 用于检查函数和变量的合法性.

### 三、符号表结构说明:

```python
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

class FuncTable:

    def __init__(self):
        self.functree = funcNode("all","","")
        self.functree.subFuncDict = {}
```

FuncTable以funcNode为结点的树状结构.

subFuncDict为该函数作用域内定义的函数信息, 用字典存储方便查找, dict对应的value仍然为funcNode.

localVar为该函数作用域内定义的全部变量信息, 同样用字典存储, dict对应的value为localvarNode.

符号表中有4个method,用于:**添加新函数, 查找函数, 添加新变量, 查找变量**.

### 四、重点:

1. 了解.g4文件的书写规则和python的语法构成。

2. 了解antlr4语法树的相关方法

3. 构建符号表的数据结构。

4. 在语法树中找到修改符号表的对应位置。

   

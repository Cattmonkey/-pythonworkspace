# -*- coding: utf-8 -*-


#制作解释器 将配置文件 解释成python

#解释器的核心是「中间表示」（Intermediate representation，IR）
    #将源码中的字符分割成标记符（token）
    #将标记符组织成一棵抽象语法树（AST）。抽象语法树就是中间表示。
    #评估这棵抽象语法树，并在最后打印这棵树的状态
    
import ast
#from model.phMode1 import main1


#Module(body=[FunctionDef(name='hello', args=arguments(args=[arg(arg='name', annotation=None)], 
#vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[Str(s='world')]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Str(s='hello '), op=Add(), right=Name(id='name', ctx=Load()))], keywords=[]))], decorator_list=[], returns=None), 
#Expr(value=Call(func=Name(id='hello', ctx=Load()), args=[], keywords=[]))])
expr = """
from model.phMode import main_
def hello(args):
    return main(args)   
"""
class PmlTransformer(ast.NodeTransformer):

    def __init__(self, funName = 'func', callmain = "main", import_module = "model.test"):
        
        self.funName = funName
        self.callmain = callmain
        self.import_module = import_module
        
#        self.args = ''
    
    def visit_BinOp(self, node):
#        print(node.__dict__)
#        node.op = ast.Mult()
#        node.id = "main1"
#        print(node.__dict__)
        return node
    
    def visit_Num(self, node):  
#        if node.n == 10:  
#            node.n = 100  
        return node
    
    def visit_FunctionDef(self, node):
#        print("----------visit_FunctionDef------------")
        node.name = self.funName
        node.args.id = node.args.args[0].arg
#        node.args.args.arg = self.args
        node.body[0].value.func.id = self.callmain
        
#        print('Found function ', node._fields)
#        print("---------------------------------------")
        return node
    def visit_ImportFrom(self, node):
#        print("----------------ImportFrom-------------")
#        print('visit_ImportFrom ', node._fields)
#        print(node.Expr)
        node.module = self.import_module
        node.names[0].name = self.callmain
#        print("---------------------------------------")
        return node
    def generic_visit(self, node):  
#        print("------------generic_visit--------------")
#        getattr(node, "body", "None")
#        has_lineno = getattr(node, "lineno", "None")  
#        col_offset = getattr(node, "id", "None")  
#        print(type(node).__name__, has_lineno, col_offset)
        ast.NodeTransformer.generic_visit(self, node)  
#        print("---------------------------------------")
        return node
    
    def __readPml(self, path):
        #读取pml文件进行语法
        with open(path) as f:
            for i in f.read().strip().replace("\n", "").split(","):
                yield dict([j.split(":") for j in i.split(";") if j != ""])
        pass
    def getpml(self, path):
        temp = []
        for i in self.__readPml(path):
            temp.append(i)
        return temp
    def runPmlTransformer(self, path = "./preRead.pml"):
        pmls = self.getpml(path)
#        print(pmls)
#        print("--------------------------")
#        self.visit(self.expr_ast)
        expr_ast = ast.parse(expr)
#        print(ast.dump(expr_ast))
        for pml in pmls:
            for k, v in pml.items():
#                print(k, v)
                execstr = "self." + k + "=" + "'" + v + "'"
#                print("execstr", execstr)
                exec(execstr)
#            print(self.callmain)
#            print(self.funName)
#            print(self.import_module)
            expr_ast = self.visit(expr_ast)
#            print(ast.dump(expr_ast))
#            exec(compile(expr_ast, '<test' + str(i) + '>' , 'exec'))
            
            yield {self.funName:expr_ast}
#            print("--------------------------")
#        print("--------------------------")
        

if __name__ == "__main__":
    transformer = PmlTransformer()
    #expr_asts, funName = transformer.runPmlTransformer()

    for funName_expr_ast in transformer.runPmlTransformer():
        #    print(iexpr_ast
        for funName, expr_ast in funName_expr_ast.items():
            eval(compile(expr_ast, '<test' + funName + '>' , 'exec'))
            print("def", funName)
            print(eval(funName + "('yyx')"))






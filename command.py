import os
from pi import *
from data import *
def var(name,value):
    global var_name,var_value
    var_name.append(name)
    var_value.append(value)

def out(name):
    global var_name,var_value
    for i in range(len(var_name)):
        if var_name[i] == name:
            print(var_value[i])
            break
def cput(prompt):
    return input(prompt)

def include(lib_name):
    try:
        lib=open(f'{lib_name}.fc',encoding='utf-8').read()
        lib.split('\n')
        for i in range(len(lib)):
            fc_exec(lib[i])
    except FileNotFoundError:
        print(f'foxc:not import {lib_name}')
        return None

def fc_exec(code):
    try:

                c=code.split(" ")
                if c[0] == 'var':
                    var(c[1],c[2])
                elif c[0] == 'cint':
                    out(c[1])
                elif c[0] == 'cput':
                    cc=cput(c[1])
                    var(c[2],cc)
                elif c[0] == 'cmd':
                    os.system(c[1])
                elif c[0]=='ln':
                    global ln
                    ln=c[1]
                elif c[0] == 'fun':
                    global function_name
                    global function_value
                    function_name.append(c[1])
                    while True:
                            code = input('. . .')
                            global fun_list
                            if code == 'funend' or code == '':
                                function_value.append(fun_list)
                                break
                            fun_list.append(code)
                elif c[0] == 'pi':
                    print(PI(c[1]))
                elif c[0] == 'include':
                    print(include(c[1]))
                else:
                    print(f'Not command "{code}"')
    except IndexError:
            print('Error in code')

def fun(fun_name):
     for i in range(len(function_name)):
          if function_name[i] == fun_name:
               code=function_value[i]
               for j in code:
                    fc_exec(j)
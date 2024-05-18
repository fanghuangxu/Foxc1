from include import *

def main():
    while True:
        code = input('>')
        try:
            if code == 'exit':
                break
            else:
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
                elif c[0] == 'exec':
                    list_len=len(c)
                    codee=''
                    for i in range(1,list_len):
                        codee+=c[i]
                        codee+=' '
                    print(codee)
                    fc_exec(codee)
                elif c[0] == 'rf':
                    fun(c[1])
                elif c[0] == 'for':
                    for x in range(int(c[1])):
                        fun(c[2])
                else:
                    print(f'Not command "{code}"')
        except IndexError:
            print('Error in code')
if __name__ == '__main__':
    main()
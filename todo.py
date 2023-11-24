def Speak(txt):
    return

def openlist():
    f=open('tododata.txt','r')
    td=f.read()
    td=td.split('\n')
    f.close()
    res = [i for n, i in enumerate(td) if i not in td[:n]]
    return res
def closelist(lst):
    res = [i for n, i in enumerate(lst) if i not in lst[:n]]
    f=open('tododata.txt','w')
    for i in res:
        f.write(i+'\n')
    f.close()
    return
def addtodo(task):
    try:
        td=openlist()
        td.insert(0,task)
        closelist(td)
        return f'{task} added to todo list'
    except Exception as e:
        return f'Error code {e}'
def viewtodo():
    try:
        td=openlist()
        for i in td:
            Speak(i)
        closelist(td)
        return 'End of todo list'
    except Exception as e:
        return f'Error code {e}'
def deletetodo(task):
    try:
        td=openlist()
        if task in td:
            td.remove(task)
        closelist(td)
        return f'{task} removed from todo list'
    except Exception as e:
        return f'Error code {e}'
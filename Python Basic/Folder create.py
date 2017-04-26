import os
path = r'D:\Google\Python my code\Python Basic\top_projects'
projectname = 'project1'
folders = \
[    ['input',[
        ['src', []],
        ['doc', []],
        ]],
     ['output',[]],
     ['scene',[]],
     ['assets',[
         ['charactes',[]],
         ['models',[]]
     ]]
]

def createFolder(path):
    if not os.path.exists(fullPath): # провіршка чи існує шлях
        os.mkdir(fullPath)

def build(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root,name)
            createFolder(path)
            build(path, d[1])

projectname = raw_input('enter project name : ')
if projectname:

    fullPath = os.path.join(path, projectname)
    createFolder(fullPath)
    build(fullPath, folders)
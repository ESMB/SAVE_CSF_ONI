# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import os

def init():
    fp = (r"D:/20221202_Exenatide_samples_SAVE_round4")
    print_dirs(fp)

def print_dirs(fp):
    
    for root,dirs,files in os.walk(fp):
        if 'pos_0' in root:
            name=root[:-6]
    
            for_py = 'pathList.append(r"{0}")'.format(name)
            
            print(for_py)
    
    
    
    
    
    
    
    #print('\n\n')

    #for root, dirs, files in os.walk(fp):
        #for name in files:
          
               # if 'pos_0' in dirs:
        
                    #    for_py = 'pathList.append(r"{0}")'.format(root)
                    #    print(for_py)
                        

        
init()
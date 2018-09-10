# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:16:58 2018

@author: Gerson
"""

import pandas as pd
#pd.set_option('max_rows',100,'max_columns',100)

u_info = pd.read_csv('u.info', index_col=None, encoding='utf-8',error_bad_lines=False)
#u_item = pd.read_csv('u.item', index_col=None, encoding='utf-8',error_bad_lines=False)
u_genre = pd.read_csv('u.genre', index_col=None, encoding='utf-8',error_bad_lines=False)
u_user = pd.read_csv('u.user', index_col=None, encoding='utf-8',error_bad_lines=False)
u1_base = pd.read_csv('u1.base', index_col=None, encoding='utf-8',error_bad_lines=False)
#c.head()
d=[]
for i in range(100):
    d.append({'tipo_um':pd.Series(u_user['id'][1].split('|'),index=['id','ano','sexo','op','data'])})
    
df = pd.DataFrame(d)

for i in range(u_user):
    print (i)

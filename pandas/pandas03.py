# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:35:20 2018

@author: Gerson
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:59:25 2018

@author: Gerson
"""

import pandas as pd
#date = pd.read_table('http://bit.ly/chiporders')
colunas = ['user_id','item_id','rating','timestamp']
u_data = pd.read_table('../u.data', sep='\t', header=None, names=colunas)

colunas = ['movie_id',
           'movie_title',
           'release_date',
           'video_release_date',
           'IMDb_URL',
           'unknown',
           'Action',
           'Adventure',
           'Animation',
           'Childrens',
           'Comedy',
           'Crime',
           'Documentary',
           'Drama',
           'Fantasy',
           'Film-Noir',
           'Horror',
           'Musical',
           'Mystery',
           'Romance',
           'Sci-Fi',
           'Thriller',
           'War',
           'Western']

u_item = pd.read_table('../u_u.item', sep='|', header=None , names=colunas)

colunas = ['user_id','age','gender','occupation','zip_code']
u_user = pd.read_table('../u.user',sep='|',header=None, names=colunas)

print(u_data.item_id.sort_values())
print(u_data.sort_values('item_id',ascending=False))
print(u_data.sort_values(['item_id','rating']))
print(u_data.rating.mean())
print(u_data.groupby('item_id').rating.mean())
print(u_data.sort_values('item_id'))

print(u_data)
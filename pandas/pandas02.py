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

#u_data[u_data.item_id == 1664]
d = u_data
#d_join = d.join(u_item)
d_set_index = u_item.set_index('movie_id').join(d.set_index('item_id'))

d_set_index_groupby = d_set_index.groupby(['movie_title',
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
           'Western']).rating.mean()

d_set_index_groupby2 = d_set_index.groupby(['movie_title','Animation']).agg('War').mean()


d_set_index_groupby_rating = d_set_index.groupby(['movie_title']).rating.mean()

d_set_index_groupby_Action = d_set_index.groupby(['movie_title']).Action.mean()

d_set_index_groupby_Adventure = d_set_index.groupby(['movie_title']).Adventure.mean()

d_set_index_groupby_Childrens = d_set_index.groupby(['movie_title']).Childrens.mean()

d_set_index_groupby_Horror = d_set_index.groupby(['movie_title']).Horror.mean()

d_set_index_groupby_Romance = d_set_index.groupby(['movie_title']).Romance.mean()



print(u_data.item_id.sort_values())
#print(u_data.sort_values('item_id',ascending=False))
#print(u_data.sort_values(['item_id','rating']))
#print(u_data.rating.mean())
print(u_data.groupby('item_id').rating.mean())

u = u_data.groupby('item_id').rating.mean()
#print(u_data.sort_values('item_id'))

#print(u_data)
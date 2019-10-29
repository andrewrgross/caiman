# -*- coding: utf-8 -*-
"""
CaImAn Tutorials 1 - Andrew R Gross - 2019/10/29

An initial attempt to follow tutorials outlined here:
https://caiman.readthedocs.io/en/master/Getting_Started.html
"""

import caiman as cm
import os
import numpy as np

os.chdir('C:\\Users\\grossar\\Data\\Caiman\\CaImAn\\')

#source activate CaImAn

### Loading movies

single_movie = cm.load('example_movie\\demoMovie.tif')
print(single_movie.shape)

file_names = ['example_movies/demoMovie.tif', 'example_movies/demoMovie.tif'] # for the sake of the example we repeat the same movie
movies_chained = cm.load_movie_chain(file_names)
print(movies_chained.shape)

### Generating a random movie
movie_random = cm.movie(np.random.random([1000,100,100]))

### Saving Movies

movie_random.save('movie_random-10-29.tif')

np.random.random([2,3,3])

### Visualizing Movies

movies_chained.play(magnification = 2, fr=30, q_min=0.1, q_max=99.75)

movie_random.play(magnification = 2, fr=30, q_min=0.1, q_max=99.75)

### Loading E230

E230_172_1001_stim = cm.load('C:\\Users\\grossar\\Data\\Caiman\\Input_Data\\E230\\172_1001_stim.avi')

E230_172_1001_stim.play(magnification = 2, fr=30, q_min=0.1, q_max=99.75)


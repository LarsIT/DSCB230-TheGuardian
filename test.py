from plotapi import Chord
import chord_matrix
import json

matrix = [
    [0, 5, 6, 4, 7, 4],
    [5, 0, 5, 4, 6, 5],
    [6, 5, 0, 4, 5, 5],
    [4, 4, 4, 0, 5, 5],
    [7, 6, 5, 5, 0, 4],
    [4, 5, 5, 5, 4, 0],
]

m1 = chord_matrix.matrix

names = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Thriller"]

with open('kw_count.json','r') as infile:
    threshhold = json.load(infile)

keywords = sorted(list(set(keyword for keyword in threshhold)))


Chord(m1, keywords, arc_numbers= True, colored_diagonals= False, padding= 0.05).to_html(filename= 'test_page1Chord_wTHRESHHOLD.html')


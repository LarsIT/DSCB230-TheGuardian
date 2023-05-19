# Import the library
from plotapi import Chord


# Basic cord diagram
# TODO THIS WON'T WORK BECAUSE INPUT TYPE ISNT RECOGNIZE
# Chord(data, names).to_html("../../static/interactiveCharts/chord-diagram-chord-library.html")

# TO UNDERSTAND THE MATRIX
# each list is correspondent to one of the names
# each element of each list is a counter of the frequency those 2 names (name of list and name of item, being correspondent to same index of names list)
# thats why on the diagonal it is always a zero, since an article cant have the same keyword twice
matrix = [
    [0, 20, 6, 4, 7, 4], #ACTION
    [5, 0, 5, 4, 6, 5], #ADVENTURE
    [6, 5, 0, 4, 5, 5], #COMEDY
    [4, 4, 60, 0, 5, 5], #DRAMA
    [7, 6, 5, 5, 0, 4], #FANTASY
    [4, 5, 5, 5, 4, 0], #THRILLER
]


names = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Thriller"]

Chord(matrix, names).to_html()


import string
import random

from utilities import fetchilarity_score

path1 = input('Full or relative filepath for first text file: ')
path2 = input('Full or relative filepath for second text file: ')

try:
    print(fetchilarity_score(path1,path2))
except:
    raise BaseException('Something about those pathnames failed. Please try again.')



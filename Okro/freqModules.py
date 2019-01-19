############################################################################
#"""
#    Authors: Ismail Dawud Ibrahim
#             Prince Alfred Gyan
#             Francis Billa
#             Franklin Wae Luther
#    Date Created:16th Jul,2018
#     Date Modified: 17th Jul,2018
#     
#     project: Okro -> This python project allows us to check whether a
#             given set of numerical data obeys the "Benford Law" or not
#             and also generate data based on the "Benford Law".
#
#             ReadMore: https://en.wikipedia.org/wiki/Benford%27s_law
#     
#     Deccription: This module makes up for the implementation of the benford's law 
#                 algorithm,thus fuctions for the leading values , lead frequency counts
#                 and ther corresponding percentages, to check for benford compliance.
# """
###########################################################################

import os
# get the upload folder in the current working directory/server
UPLOAD_FOLDER = os.getcwd()+'/upload'
#upload extension supported
ALLOWED_EXTENSIONS = set(['csv']) 



def allowed_file(filename):
    """ Returns 'True' if a file is part of the supported extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def file_to_list(file):
    """ It takes a .csv file as a parameter and returns a list """
    temp = open('upload/'+file, 'r+')
    data = temp.read()
    values = data.split(',')
    temp.close()
    for v in range(len(values)):
        values[v] = int(values[v])
    return values

    
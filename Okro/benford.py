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

import math

def lead_digit_conter(x,leadData):
    ''' increase the count of leadind digit '''
    if x != None:
        leadData[x-1] += 1

def leading_digit(x,dig=1):
    """ returns the leading_digit of a number """
    x = str(x)
    try:
        out = int(x[dig-1])
        return out
    except:
        return None

def benford_frequency(listValues):
    """ Returns the total frequency counts of all the leads"""
    leadData = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
    for lv in listValues:
        lead = leading_digit(lv)
        lead_digit_conter(lead, leadData)
    return leadData


def benford_percentages(leadData):
    """ Returns the percentages of frequency counts of all the leads"""
    percentages = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
    sum = 0
    for val in leadData:
        sum +=val
    for x in range(len(percentages)):
        percentages[x] =round(( leadData[x]/sum ) * 100 , 2) 
        
    return percentages

def benford_check(percentages):
    """ Returns true or false according to the percentages check with the
        expected Benford percentages 
    """ 
    percentages =  percentages
    expectation = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    check = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(9):
        check[x] = round(expectation[x] - percentages[x], 2)
    for i in range(9):
        if not((expectation[i]-2) <= percentages[i] <= (expectation[i]+2) ):
            return False
    return True

def benford_data(percentages, leadData):
    """ This function return all the necessary data after computing in python list format """
    expectation = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    data = [ [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0] ]
    for k in range(len(percentages)):
        data[k][0] = leadData[k]
        data[k][1] = percentages[k]
        data[k][2] = expectation[k]
        data[k][3] = round(expectation[k] - percentages[k], 2)
        data[k][4] = k+1
   
    return data

def benford_data_json(percentages, leadData):
    """ This function return all the necessary data after computing in json format """
    expectation = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    data = {
        'one':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        },
        'two':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        },
        'three':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        },
        'four':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        },
        'five':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        },
        'six':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        },
        'seven':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        },
        'eight':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        },
        'nine':{
            'count': 0,
            'expectation': 0,
            'percentage': 0,
            'deviation': 0,
        }
    }
    xCount = 0
    for k in data:
        data[k]['count'] = leadData[xCount]
        data[k]['percentage'] = percentages[xCount]
        data[k]['expectation'] = expectation[xCount]
        data[k]['deviation'] = round(expectation[xCount] - percentages[xCount], 2)
        xCount += 1
    
    return data


def benford_data_csv(percentages, leadData):
    """ This function return all the necessary data after computing in csv format """
    data = ''
    expectation = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    for k in range(len(percentages)):
         if data != '':
             data += ","
         data += str(leadData[k])+","
         data += str(percentages[k])+","
         data += str(expectation[k]) +","
         data += str(round((expectation[k] - percentages[k]),2))
    return data

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
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug import secure_filename
import freqModules as fq
import generator as gen
import benford as bf


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = fq.UPLOAD_FOLDER

@app.route('/index')
@app.route('/')
def index():
    """ This function renders the index.html page,
        if it's a GET request a normal page 
        .csv"""
    return render_template('index.html')

@app.route('/gene')
def gene():
    """ This function renders the index.html page,
        if it's a GET request a normal page 
        .csv"""
    return render_template('generate.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    """ This method is rendered when a user submits a file,
        it validates the file extension or if file submit is empty 
    """
    bigDataRead = []
    check= ""
    if request.method == 'POST':
        try:
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return render_template('index.html')
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                return render_template('index.html')
            if file and fq.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                bigDataRead = fq.file_to_list(filename)
                #return str(bigDataRead)
                main_list = bf.benford_frequency(bigDataRead)
                per_list = bf.benford_percentages(main_list)
                data = bf.benford_data(per_list, main_list)
                check = bf.benford_check(per_list)
                return render_template('index.html', data = data,jsData = per_list , check = check)
            else:
                flash('FILE NOT SUPPORTED!')
                return render_template('index.html',check = check)
        except:
            return render_template('index.html',check = check)
    elif request.method == 'GET':
        return render_template('index.html',check = check)

@app.route('/generator', methods = ['GET', 'POST'])
def generator():
    """ This method generates a set of random number that obeys the benford law
        according to the description provided.
    """
    data = ''
    if request.method == 'POST':
        min = request.form['dataMin']
        max = request.form['dataMax']
        dataSize = request.form['dataSize']

        if min == "" or max == "" or dataSize== "":
            #flash('Please fill the data description !')
            return render_template('generate.html')
        else:
            min = int(min)
            max = int(max)
            dataSize = int(dataSize)
            result = gen.generate(max, min, dataSize)
            for k in range(len(result)):
                if data != '':
                    data += ","
                data += str(result[k])

            with open('upload/dataGenerate.csv', 'w') as f:
                f.write(data)
                f.close()
            return render_template('generate.html', result = result)


@app.route('/data_generate.csv', methods = ['GET', 'POST'])
def download_csv_generate():
    """ This function allow user to download the results of the dataset
        in .csv format 
    """
    #uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename='dataGenerate.csv')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host= '0.0.0.0', port= port, debug =True)
    
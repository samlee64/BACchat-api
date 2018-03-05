from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import ml

cFile = open("confidence.json", "w")
cFile.write('0')
cFile.close()

app = Flask(__name__)
CORS(app)
@app.route('/api/v1/drunk', methods=['POST'])
def give_data():
    file = open("data.json", "a")
    data = request.form
    dataDict = data.to_dict(flat=False)
    dataList = dataDict["mlData[]"]

    file.write('[')
    for index, element in enumerate(dataList):
        if (len(dataList)  - 1) == index:
            file.write(element)
        else:
            file.write(element+', ')
    file.write(']' + '\n')

    file.close()
    return jsonify({'status': "ok"})

CORS(app)
@app.route('/api/v1/confidence', methods=['POST'])
def give_confidence():
    cFile = open("confidence.json", "r")
    for line in cFile:
        pass
    lastLine = line
    cFile.close()

    data = request.form
    dataDict = data.to_dict(flat=False)
    dataList = dataDict['confidenceArray[]']

    totalSum = 0
    for element in dataList:
        totalSum += float(element)


    totalAvg= (((totalSum)/(len(dataList))) + float(lastLine))/2

    nFile = open("confidence.json", "w")
    nFile.write(str(totalAvg))
    nFile.close()
    return  jsonify({'status': 'ok'})



@app.route('/api/v1/drunk', methods=['GET'])
def get_ml():
    file = open("data.json", "r")
    for line in file:
        pass
    data = line
    file.close()

    file = open("confidence.json", "r")
    for line in file:
        pass
    confidence = line
    file.close()

    cFile = open("confidence.json", "w")
    cFile.write('0')
    cFile.close()

    jsonData = json.loads(data)
    jsonData.append(float(confidence))
    result = ml.isDrunk(jsonData)

    head, *tail = result

    if head == 1:
        return jsonify({'isDrunk': True})
    else:
        return jsonify({'isDrunk': False})

if __name__ == '__main__':
    app.run(debug=True)



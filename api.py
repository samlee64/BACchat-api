from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
            },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
            }
        ]

CORS(app)
@app.route('/api/v1/drunk', methods=['GET', 'POST'])
def get_tasks():
    file = open("data.json", "a")
    print("foobar")
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
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)



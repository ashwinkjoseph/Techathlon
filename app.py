from flask import Flask, render_template, request, jsonify
import pickle
from pathlib import Path
import requests

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/del', methods=['POST'])
def dele():
    file = Path("file")
    if file.is_file():
        f = open("file", "rb")
        rules = pickle.load(f)
        f.close()
    else:
        rules = []
    i = int(request.json['id'])
    i = i-1
    if len(rules)>i:
        del rules[i]
    f = open("file", "wb")
    pickle.dump(rules, f)
    f.close()

    return jsonify({'status':'success'}), 200
    

@app.route('/')
def index():
    file = Path("file")
    if file.is_file():
        f = open("file", "rb")
        rules = pickle.load(f)
        f.close()
    else:
        rules = []
    ru = []
    id = []
    for rule in rules:
        condition = rule['condition'].split("!")
        condition.pop()
        # print(condition)
        # res.append(condition)
        conditionS = ' '.join(condition[1:])
        ru.append({'c':conditionS, 'i':rule['id']})
        # id.append(rule['id'])
    # return jsonify({'c':ru}), 200
    return render_template('index.html', conditions=ru)

@app.route('/view', methods=['GET'])
def view():
    f = open("file", "rb")
    tempRules = pickle.load(f)
    f.close()
    return jsonify({'tempRules':tempRules}), 200

@app.route('/node1', methods=['GET'])
def node1():
    file = Path("values")
    if file.is_file():
        f = open("values", "rb")
        values = pickle.load(f)
        f.close()
    else:
        values = {
            'Hum':0,
            'Temp':0,
            'Mois':0
        }
    Hum = request.args.get('Hum')
    values['Hum'] = Hum
    Hum = values['Hum']
    Temp = values['Temp']
    Mois = values['Mois']
    f = open("values", "wb")
    pickle.dump(values, f)
    f.close()
    f = open("file", "rb")
    rules = pickle.load(f)
    f.close()
    res = []
    # return jsonify({'rules':rules}), 200
    for rule in rules:
        condition = rule['condition'].split("!")
        condition.pop()
        # print(condition)
        # res.append(condition)
        conditionS = ' '.join(condition[1:])
        ress = eval(conditionS)
        if(ress):
            requests.get("http://192.168.45.03?mode=1")
        else:
            requests.get("http://192.168.45.03?mode=0")
        res.append(condition)

    return jsonify({'res':res, 'ress':ress}), 200

@app.route('/node2', methods=['GET'])
def node2():
    file = Path("values")
    if file.is_file():
        f = open("values", "rb")
        values = pickle.load(f)
        f.close()
    else:
        values = {
            'Hum':0,
            'Temp':0,
            'Mois':0
        }
    Temp = request.args.get('Temp')
    values['Temp'] = Temp
    Hum = values['Hum']
    Temp = values['Temp']
    Mois = values['Mois']
    f = open("values", "wb")
    pickle.dump(values, f)
    f.close()
    f = open("file", "rb")
    rules = pickle.load(f)
    f.close()
    res = []
    # return jsonify({'rules':rules}), 200
    for rule in rules:
        condition = rule['condition'].split("!")
        condition.pop()
        # print(condition)
        # res.append(condition)
        conditionS = ' '.join(condition[1:])
        ress = eval(conditionS)
        if(ress):
            requests.get("http://192.168.45.03?mode=1")
        else:
            requests.get("http://192.168.45.03?mode=0")
        res.append(condition)

    return jsonify({'res':res, 'ress':ress}), 200

@app.route('/node3', methods=['GET'])
def node3():
    file = Path("values")
    if file.is_file():
        f = open("values", "rb")
        values = pickle.load(f)
        f.close()
    else:
        values = {
            'Hum':0,
            'Temp':0,
            'Mois':0
        }
    Mois = request.args.get('Mois')
    values['Mois'] = Mois
    Hum = values['Hum']
    Temp = values['Temp']
    Mois = values['Mois']
    f = open("values", "wb")
    pickle.dump(values, f)
    f.close()
    f = open("file", "rb")
    rules = pickle.load(f)
    f.close()
    res = []
    # return jsonify({'rules':rules}), 200
    for rule in rules:
        condition = rule['condition'].split("!")
        condition.pop()
        # print(condition)
        # res.append(condition)
        conditionS = ' '.join(condition[1:])
        ress = eval(conditionS)
        if(ress):
            requests.get("http://192.168.45.03?mode=1")
        else:
            requests.get("http://192.168.45.03?mode=0")
        res.append(condition)

    return jsonify({'res':res, 'ress':ress}), 200

@app.route('/temp', methods=['POST'])
def addTemp():
    file = Path("file")
    if file.is_file():
        f = open("file", "rb")
        tempRules = pickle.load(f)
        f.close()
        id = tempRules[-1]['id']
    else:
        id = 0
        tempRules = []
    print(request.json)
    o = {'id':id+1, 'condition':request.json['condition'], 'then':request.json['then'], 'else':request.json['else']}
    tempRules.append(o)
    f = open("file", "wb")
    pickle.dump(tempRules, f)
    f.close()

    return jsonify({'status':'succcess'}), 200
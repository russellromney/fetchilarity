from flask import Flask, jsonify, request
import requests

from utilities import fetchilarity_score


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message':"welcome to the Fetchilarity API, which determines the similarity of two texts. API POST calls use the /api endpoint with a JSON payload like {'text1':'this is my text','text2':'this is my other text'}, or use the raw endpoint: /api/raw/text1-stuff/text2-wrods "})


@app.route('/api',methods=['POST'])
def api():
    content = request.json
    try:
        text1 = content['text1']
        text2 = content['text2']
    except BaseException as e:
        print(e)
        return jsonify({'message':'something was wrong with those texts. Try again?'})
    
    try:
        return jsonify({'fetchilarity_score':fetchilarity_score(text1,text2,mode='api')})
    except BaseException as e:
        print(e)
        return jsonify({'message':'There was a problem with the submitted text. Please try again.'})



@app.route('/api/raw/<text1>/<text2>',methods=['GET'])
def raw_api(text1,text2):
    try:
        return jsonify({'fetchilarity_score':fetchilarity_score(text1,text2,mode='api')})
    except BaseException as e:
        print(e)
        return jsonify({'message':'There was a problem with the submitted text. Please try again.'})



if __name__ == '__main__':
    app.run(port=5000,debug=True)






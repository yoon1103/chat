from flask import Flask, request, jsonify
import random
 
app = Flask(__name__)
 
@app.route('/skill', methods=['POST'])
def skill():
    number = random.randint(1, 100)
    answer = "뽑힌 숫자는 " + str(number) + " 입니다."
 
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                { "simpleText": { "text": answer } }
            ]
        }
    }
    return jsonify (response)
 
if __name__ == '__main__':
    app.run()

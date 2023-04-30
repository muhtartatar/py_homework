from flask import Flask, jsonify

app = Flask(__name__)
constant = []

# операція GET
@app.route('/constant', methods=['GET'])
def get_constant():
    return jsonify(constant)

# операція POST
@app.route('/constant', methods=['POST'])
def add_constant():
    import random
    constant.append(random.randint(0, 100))
    return 'Element added'

# операція DELETE
@app.route('/constant', methods=['DELETE'])
def delete_constant():
    if constant:
        constant.pop()
        return 'Element deleted'
    else:
        return 'List is empty'

if __name__ == '__main__':
    app.run(debug=True)

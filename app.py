from flask import Flask
from Extensions import Amazon,Flipkart

app=Flask(__name__)

@app.route('/<id>')
def main(id):

    return [
        Amazon.Amazon(id).json,
        Flipkart.Flipkart(id).json
    ]



if __name__=='__main__':
    app.run(debug=True)
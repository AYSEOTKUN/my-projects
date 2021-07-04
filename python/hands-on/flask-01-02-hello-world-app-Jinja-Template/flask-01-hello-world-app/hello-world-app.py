from flask import Flask

app =Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/second') 
def second():
    return 'Bize her yer DENİZLİ'

@app.route('/third/subthird')  
def third() :
     return 'This is the subpage of third page'     







if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,render_template,redirect,url_for


app = Flask(__name__)

@app.route('/')
def aws():
    return '<h1>Clarusway AWS</h1>'

@app.route('/index')
def index() :
    site = 'flask dersleri '
    return render_template('index.html',message = site)

@app.route('/iletisim')
def iletisim() :
    telno = ["Ankara:03125555555","İstanbul:02162222222"]
    return render_template('iletisim.html', object = telno)

@app.route('/hata')
def hata():
    return '<h1>aradığınız sayfa bulunamamaktadır.<h1>'

@app.route('/admin')
def admin() :
    return redirect(url_for('hata'))

#@app.route('/<name>')
#def isim(name) :
#    isim_format =f"""<!DOCTYPE html>
#    <html>
#<head>
#    <title>Greeting Page</title>
#</head>
#<body>
#    <h1>Hello, { name }!</h1>
#    <h1>Welcome to my Greeting Page</h1>
#</body>
#</html> """

#    return isim_format

@app.route('<kullanıcı>')
def uyeol(kullanıcı) :
    return render_template('uyeol.html',kullanıcı = kullanıcı)


if __name__ == "__main__":
   # app.run(debug=True)
   app.run(host='0.0.0.0',port=80)


import urllib.request as urllib2
halaman = 'https://bola.okezone.com/klasemeninggris'
html = urllib2.urlopen(halaman).read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
table = soup.find('table', 'table-klas')
# type(table)
rows = table.find_all('tr')
len(rows)
# for i in range(1,20):
#     rows[i].
texts = []
for row in rows:
    text = list(row.stripped_strings)
    texts.append(text)

kolomNomor = []
kolomKlub = []
kolomMain = []
kolomMenang = []
kolomSeri = []
kolomKalah = []
kolomPoint = []
for index in range(0,21):
    kolomNomor.append(texts[index][0])
    kolomKlub.append(texts[index][1])
    kolomMain.append(texts[index][2])
    kolomMenang.append(texts[index][3])
    kolomSeri.append(texts[index][4])
    kolomKalah.append(texts[index][5])
    kolomPoint.append(texts[index][6])

print(kolomPoint)


# from flask import Flask, Blueprint, render_template
# from werkzeug.contrib.fixers import ProxyFix

# web_app = Blueprint('app', __name__)
# @web_app.route('/')
# def hello():
#     return render_template('index.html', nomor=kolomNomor, klub=kolomKlub)

# if __name__ == '__main__':
#     app = Flask(__name__)
#     app.register_blueprint(web_app, url_prefix='/')

#     app.wsgi_app = ProxyFix(app.wsgi_app)
#     app.run()
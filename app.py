#!/usr/local/bin/python

from flask import *
app = Flask(__name__)

from models import manager
from data import charaset
from twitter_intent import TwitterIntentClient


@app.route('/', methods=['GET', 'POST'])
def render_root():
    return render_template('index.html')

@app.route('/index.html', methods=['GET', 'POST'])
def render_index():
    return render_template('index.html')

@app.route('/result.html', methods=['GET', 'POST'])
def render_result():
    data = manager.get_random()
    name_pfx = request.form['user_name'] + 'さんの引いた名前は、'
    name = '《' + data.name + '》'
    name_sfx = 'です。'
    text_data = name_pfx + name + name_sfx
    tic = TwitterIntentClient(text=text_data, shere_url='hoge.co.jp', hashtags='あなたの番です,あな番,あな番紙交換ツール')
    summary = data.summary
    return render_template('result.html', name_pfx=name_pfx, name=name, name_sfx=name_sfx, summary=summary, tweet_url=tic.url)

def load_charaset():
    for chara in charaset:
        # 登録済みか名前で検索する
        res = manager.Table.query.filter(manager.Table.name == chara['name']).first()
        if res != None:
            res.name = chara['name']
            res.power = chara['power']
            res.summary = chara['summary']
            manager.commit()
        else:
            manager.insert(name=chara['name'], power=chara['power'], summary=chara['summary'])


if __name__ == '__main__':
    #load_charaset()
    app.run()

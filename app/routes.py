from flask import render_template
from flask import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return '', 200

@app.route("/audio")
def audio():
    image = request.args.get('image')
    audio = request.args.get('audio')
    starting_animation = request.args.get('start')
    ending_animation = request.args.get('end')
    animation_delay = request.args.get('delay')
    animation_delay = (int(animation_delay) * 1000)
    return render_template('audio.html',
                           image='images/{}'.format(image),
                           audio='audio/{}'.format(audio),
                           starting_animation=starting_animation,
                           ending_animation=ending_animation,
                           animation_delay=animation_delay)
from flask import Flask, render_template
from flask_socketio import SocketIO
from src.data_src import MainDf

app = Flask(__name__)
socketio = SocketIO(app)
main_df = MainDf()

@socketio.on('click-on-key')
def handle_message(msg):
    # emit response
    data = main_df.show_values(msg)
    socketio.emit('click-on-key', data)


@socketio.on('click-on-value')
def handle_message(msg):
    # emit response
    html = main_df.show_keys(msg)
    level = msg['div_id'].replace('level', '')
    level = int(level) + 1
    socketio.emit('click-on-value', {'div_id': level, 'html': html})


@app.route('/')
def main():
    data = main_df.show_keys()
    return render_template('content.html', data=data)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)

from flask import Flask, render_template, request
from flask_socketio import SocketIO
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('run_code')
def run_code(data):
    code = data['code']
    input_data = data.get('input', '')  # Get input data if available
    
    try:
        process = subprocess.Popen(
            ['python', '-c', code],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output, error = process.communicate(input=input_data, timeout=5)

        if process.returncode == 0:
            socketio.emit('output', {'output': output})
        else:
            socketio.emit('output', {'output': f'Error: {error}'})

    except Exception as e:
        socketio.emit('output', {'output': f'Error: {str(e)}'})

if __name__ == '__main__':
    socketio.run(app, debug=True)

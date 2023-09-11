
from flask import Flask, request, render_template
from flask_cors import CORS

from translation import translate_text


app = Flask(__name__)
# lisätty cors
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['text_to_translate']
        translated_text = translate_text(input_text)
        return render_template('index.html', translated_text=translated_text)
    return render_template('index.html', translated_text=None)

if __name__ == '__main__':
    app.run(debug=False)
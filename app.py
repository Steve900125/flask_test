from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        answer = '這是問題的答案。'  # 在這裡插入你想要顯示的答案
        return render_template('index.html', question=question, answer=answer)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
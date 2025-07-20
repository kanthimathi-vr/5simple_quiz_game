from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'

# Quiz questions
questions = [
    {
        'id': 1,
        'image': 'images/question1.jpg',
        'question': 'What is the capital of France?',
        'choices': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'answer': 'Paris'
    },
    {
        'id': 2,
        'image': None,
        'question': 'Which planet is known as the Red Planet?',
        'choices': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'id': 3,
        'image': None,
        'question': 'Which language is used to style web pages?',
        'choices': ['HTML', 'Python', 'CSS', 'C++'],
        'answer': 'CSS'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for q in questions:
            user_answer = request.form.get(str(q['id']))
            if user_answer == q['answer']:
                score += 1
        session['score'] = score
        return redirect(url_for('result'))
    return render_template('quiz.html', questions=questions)

@app.route('/result/')
def result():
    score = session.get('score', 0)
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)

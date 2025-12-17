from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add this route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Add your login logic here
        print(f"Login attempt: {email} / {password}")
        return redirect(url_for('index'))  # Redirect after login
    return redirect(url_for('index'))  # For GET requests

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # Add your signup logic here
    print(f"Signup: {name} / {email}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

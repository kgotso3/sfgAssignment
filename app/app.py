from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)

users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    # Render the index.html template
    return render_template('landingPage.html')

@app.route('/login', methods=['POST'])
def login():
    usr = request.form['username']
    pas = request.form['password']
    if usr in users and users[usr] == pas:
        return redirect(url_for('carOwner'))
    # Redirect to the landing page after successful login
    else:
        return redirect(url_for('carOwner'))

@app.route('/carOwner')
def carOwner():
    # Render the landingPage.html template
    return render_template('carOwner.html')

@app.route('/pay', methods=['POST'])
def simulate_payment():
    violation_id = request.form['violation_id']
    # Simulate payment logic (replace with actual payment processing logic)
    # For example, you might update the database to mark the violation as paid
    # or call a payment gateway API.
    # For demonstration purposes, we'll simply return a success message.
    return jsonify({'success': True, 'message': f'Payment successful for violation ID {violation_id}'})

if __name__ == '__main__':
    app.run(debug=True)




 
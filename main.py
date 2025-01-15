from flask import Flask, request, render_template

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')
# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Access form data
        user = request.form['user']
        password = request.form['pass']
        # message = request.form['message']
        
        # Process the data (e.g., print it)
        print(f"Received data: user - {user}, password - {password}")
        
        # Optionally, you can send a response back to the client
        return "Form submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)

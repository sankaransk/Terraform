import flask

app = flask.Flask(__name__)

@app.route('/')
def login_page():
    return '''
    <html>
        <head>
            <title>Login Page</title>
            <style>
                body {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f5f5f5;
                }
                .container {
                    background-color: white;
                    padding: 2rem;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
                .form-group {
                    margin-bottom: 1rem;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                input {
                    width: 100%;
                    padding: 0.5rem;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    box-sizing: border-box;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 0.5rem 1rem;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Login</h1>
                <form action="/login" method="post">
                    <div class="form-group">
                        <label for="username">Username:</label><br>
                        <input type="text" id="username" name="username" required="required">
                    </div>
                    <div class="form-group">
                        <label for="password">Password:</label><br>
                        <input type="password" id="password" name="password" required="required">
                    </div>
                    <button type="submit">Login</button>
                </form>
            </div>
        </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = flask.request.form['username']
    password = flask.request.form['password']

    if validate_user(username, password):
        return "Login successful!"
    else:
        return "Invalid credentials!"

def validate_user(username, password):
    # This is a simple validation function
    # In a real application, you would store users in a database
    # And verify the password against stored hash
    if username == "admin" and password == "password":
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True)
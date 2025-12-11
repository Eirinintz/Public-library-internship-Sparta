from flask import Flask

# Create the Flask application (should be __name__)
app = Flask(__name__)

# List of messages to display on the homepage
messages = ["Hello!", "Welcome!"]

@app.route('/')
def home():
    # Return the messages joined with a line break
    return "<br>".join(messages)

# Start the application (should be __name__ == '__main__')
if __name__ == '__main__':
    app.run(debug=True)

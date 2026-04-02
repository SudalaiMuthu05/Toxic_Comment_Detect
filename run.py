from flask import Flask

app = Flask(__name__)

# Load models from the models directory
model_path = 'models/model_name'  # Update with actual model file name

@app.route('/')
def home():
    return 'Welcome to the Toxic Comment Detection API!'

if __name__ == '__main__':
    app.run(debug=True)
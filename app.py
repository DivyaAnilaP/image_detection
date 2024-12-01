from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

# Define the route for the Home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Define the route for the Testing page
@app.route('/testing', methods=['GET', 'POST'])
def testing():
    result = None
    image_path = None

    if request.method == 'POST':
        # Handle file upload
        if 'file' not in request.files:
            return "No file part in request", 400

        file = request.files['file']
        if file.filename == '':
            return "No file selected", 400

        if file:
            # Save the uploaded file
            upload_folder = 'static/images/uploads'
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, file.filename)
            file.save(image_path)

            # Call the API 
            result = call_prediction_api(image_path)

    return render_template('testing.html', result=result, image_path=image_path)

# Placeholder for API call
def call_prediction_api(image_path):
    
    
    return "Prediction not implemented"  # Default message

if __name__ == '__main__':
    app.run(debug=True)

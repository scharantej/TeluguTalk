
# Import necessary modules
from flask import Flask, render_template, request, send_file
import os

# Initialize the Flask application
app = Flask(__name__)

# Define the root route
@app.route('/')
def index():
    """
    Purpose: Handle the root URL ('/') and display the index.html page.
    """

    # Render the index.html page
    return render_template('index.html')


# Define the lessons route
@app.route('/lessons', methods=["GET", "POST"])
def lessons():
    """
    Purpose: To serve the lessons.html page when the user clicks the 
    "Start Learning" button in the index.html form.
    
    Method: POST
    Request: Retrieves the user's selected Hindi proficiency level 
    from the index.html form.
    Response: Renders the lessons.html page, tailoring the content 
    based on the user's proficiency level.
    """
    
    # If the request method is POST, retrieve the Hindi proficiency 
    # level from the form
    if request.method == "POST":
        hindi_proficiency = request.form.get('hindi_proficiency')
    
    # Render the lessons.html page, passing the Hindi proficiency 
    # level as a template variable
    return render_template('lessons.html', 
                          hindi_proficiency=hindi_proficiency)


# Define the audio streaming route
@app.route('/audio/<filename>')
def audio(filename):
    """
    Purpose: To stream the audio files associated with the Telugu 
    phrases in the lessons.html page.
    
    Method: GET
    Request: Accepts a filename as a parameter, which corresponds 
    to the name of the audio file.
    Response: Streams the audio file with the matching filename to 
    the client.
    """
    
    # Construct the path to the audio file
    audio_path = os.path.join('audio', filename)
    
    # Return the audio file as a response, setting the MIME type 
    # to 'audio/mpeg'
    return send_file(audio_path, mimetype='audio/mpeg')


# Define the exercises route
@app.route('/exercises', methods=["GET", "POST"])
def exercises():
    """
    Purpose: To evaluate the user's understanding of the Telugu 
    lessons.
    
    Method: POST
    Request: Receives the user's answers to the interactive exercises 
    in the lessons.html page.
    Response: Processes the user's answers, provides feedback, and 
    suggests further learning resources if needed.
    """
    
    # If the request method is POST, process the user's answers
    if request.method == "POST":
        # Retrieve the user's answers from the request
        answers = request.form.getlist('answers[]')
        
        # Process the answers, provide feedback, and suggest further 
        # learning resources as needed
        feedback, resources = process_answers(answers)
    
    # Render the exercises.html page, passing the feedback and 
    # resources as template variables
    return render_template('exercises.html', feedback=feedback, 
                          resources=resources)


# Define the function to process the user's answers
def process_answers(answers):
    """
    Purpose: To process the user's answers to the interactive 
    exercises, provide feedback, and suggest further learning 
    resources.
    
    Args:
        answers: A list of the user's answers to the exercises.
    
    Returns:
        A tuple containing the feedback and further learning 
        resources for the user.
    """
    
    # Initialize the feedback and resources variables
    feedback = []
    resources = []
    
    # Iterate over the user's answers
    for answer in answers:
        # Check if the answer is correct
        if answer == 'correct_answer':
            # If the answer is correct, provide positive feedback
            feedback.append("Correct! Great job!")
        else:
            # If the answer is incorrect, provide constructive feedback 
            # and suggest further learning resources
            feedback.append("Incorrect. Keep practicing!")
            resources.append("https://example.com/lesson_X")
    
    # Return the feedback and resources
    return feedback, resources


# Run the application
if __name__ == '__main__':
    app.run(debug=True)

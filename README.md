## Flask Application Design for Learning Spoken Telugu

## HTML Files

### 1. index.html

- Purpose: Main landing page of the application.
- Content:
  - A friendly welcome message encouraging the user to learn the beautiful Telugu language.
  - A brief introduction about Telugu, its significance, and its prevalence.
  - A form consisting of:
    - A dropdown list of proficiency levels in Hindi (the user's native language) to help tailor the learning experience.
    - A button labeled "Start Learning."

### 2. lessons.html

- Purpose: To present the user with the Telugu learning content.
- Content:
  - A section dedicated to common Telugu phrases and their pronunciations, both in Telugu script and romanized form.
  - Audio recordings of these phrases, allowing the user to practice listening and pronunciation.
  - A section on basic Telugu grammar, covering essential concepts like sentence structure, tenses, and pronouns.
  - Interactive exercises to test the user's understanding and retention of the learned material.

## Routes

### 1. @app.route('/')

- Purpose: To handle the root URL ('/') and display the index.html page.

### 2. @app.route('/lessons')

- Purpose: To serve the lessons.html page when the user clicks the "Start Learning" button in the index.html form.
- Method: POST
- Request: Retrieves the user's selected Hindi proficiency level from the index.html form.
- Response: Renders the lessons.html page, tailoring the content based on the user's proficiency level.

### 3. @app.route('/audio/<filename>')

- Purpose: To stream the audio files associated with the Telugu phrases in the lessons.html page.
- Method: GET
- Request: Accepts a filename as a parameter, which corresponds to the name of the audio file.
- Response: Streams the audio file with the matching filename to the client.

### 4. @app.route('/exercises')

- Purpose: To evaluate the user's understanding of the Telugu lessons.
- Method: POST
- Request: Receives the user's answers to the interactive exercises in the lessons.html page.
- Response: Processes the user's answers, provides feedback, and suggests further learning resources if needed.
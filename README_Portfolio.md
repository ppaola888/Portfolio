
# Portfolio

This is my personal portfolio website created with Python and Flask framework that displays various projects and provides information about my skills, services and professional background. The portfolio features 3 different projects, each of them on a separate page. Each project has a detailed description as well as a link to its source code on GitHub.

## Features
**Home page**: A brief overview of my skills and services.

**Projects**: Display of different development projects with links to detailed pages.

**Contact Form**: Allows visitors to contact me through a form that sends an email.

**Services**: List of web development services offered.

**Skills**: Overview of technical skills with badges.

**Thank You page**: A page shown after a successful form submission.

**Credits**: A page giving credit to images used.

## Technologies
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Libraries**:
  - Flask
  - SMTP for email handling
  - dotenv for environment variable management
  - Bootstrap for responsive design
  - Type.js for typing animation on the homepage


## Installation

**Clone the repository**: 

- git clone <repository-url>

- cd <repository-folder>

**Create a virtual environment**:

     ```bash
     python -m venv venv

**Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate

**Install the dependencies**:

    pip install -r requirements.txt

**Create an .env file in the root of the project and include the following credentials:**:

- EMAIL_ADDRESS=your_email@example.com
- EMAIL_PASSWORD=your_password

**Run the Flask app**:

    flask run

**Open your browser and navigate to http://127.0.0.1:5000/ in order to view the portfolio.**

## Javascript Functionality
**Typing Effect**

One of the effects in this project is the typing effect, implemented using the Typed.js library. This effect simulates the automatic typing of text on an HTML element, by creating a dynamic animation. In the code, a JavaScript script is used to implement the typing effect.

## Deploy

This project has been easily deployed on Render.

- Create a Render account
- Once you have created an account, go to your Render dashboard and click on New Web Service.
- Select Connect to GitHub repository.
- Grant Render access to your GitHub account and select the project repository.
- Set the start command as gunicorn app:app, where app is the name of your main file (change this configuration according to the structure of your project).
- Click on Deploy to start the deployment process. Render will clone your repository, build the project and start it automatically.
- Once the deployment is completed, Render will provide a public URL to display the portfolio.



























## 🛠 Skills
Flask, Python, Bootstrap for styling, dotenv (for environment variable management), Javascript with Typed.js, Git



## 🚀 About Me
I'm a junior developer!


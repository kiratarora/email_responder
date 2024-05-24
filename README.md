# Multi-Module Application with Recipe Generator and Email Responder

## Overview
This project consists of two primary modules: a Recipe Generator and an Email Responder. The front end is entirely written in HTML and CSS and is deployed on GitHub Pages. The back end is a Flask server handling API calls and is deployed on Render. The application leverages OpenAI's GPT-3.5 Turbo language model to generate recipes and draft email responses.

## Features

### Recipe Generator
The Recipe Generator module allows users to input a list of ingredients and any dietary restrictions they might have. Upon submitting this information, the system returns a recipe that can be made with the provided ingredients, taking into account the dietary restrictions. This module utilizes OpenAI's GPT-3.5 Turbo model to generate the recipe.

#### Key Features:
- Simple and intuitive front end with text areas for ingredients and dietary restrictions.
- Submit button to send the data to the Flask server.
- API call to OpenAI's GPT-3.5 Turbo model to generate a recipe.
- Display the generated recipe on the front end.

### Email Responder
The Email Responder module enables users to input their email ID and an application-specific password. The system then reads the latest email in their inbox and drafts a response to it. The front end displays a summary of the email and the drafted response. Users also have the option to provide notes to customize the response generated by the GPT-3.5 Turbo model.

#### Key Features:
- Input fields for email ID and application-specific password.
- Fetches and summarizes the latest email from the user's inbox.
- Generates a response to the email using OpenAI's GPT-3.5 Turbo model.
- Allows users to provide notes for customizing the response.
- Displays the email summary and the drafted response on the front end.

## Technology Stack
- **Front End:** HTML, CSS (deployed on GitHub Pages)
- **Back End:** Flask (deployed on Render)
- **AI Model:** OpenAI's GPT-3.5 Turbo

## Future Work
- **Recipe Module Enhancements:**
  - Display multiple recipe suggestions.
  - Integrate computer vision to scan ingredients using a camera instead of manual input.
  
- **Email Responder Enhancements:**
  - Allow users to view more than just the latest email.
  - Provide an option for users to manually edit the drafted response.
  - Enable sending responses directly from the application.

## Usage
### Recipe Generator
1. Open the Recipe Generator web page.
2. Enter the ingredients you have.
3. Enter any dietary restrictions you may have.
4. Click the "Submit" button.
5. View the generated recipe on the page.

### Email Responder
1. Open the Email Responder web page.
2. Enter your email ID.
3. Enter your application-specific password (Refer to [Google's App Passwords](https://support.google.com/accounts/answer/185833?sjid=5226502612762553331-NA#app-passwords) for more details).
4. Click the "Submit" button.
5. View the summary of the latest email and the generated response on the page.
6. Optionally, add notes to customize the response.

## Installation and Setup
### Prerequisites
- Python 3.x
- Flask
- OpenAI API key
- GitHub Pages account for deploying the front end
- Render account for deploying the back end

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

#### PS: The first fetch can take up to a few minutes since the inactive server gets shut down and needs to be rebooted.

![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&pause=1500&color=1996F7&width=435&lines=Photo+Web+App)](https://git.io/typing-svg)

This project is a web application for uploading and viewing images. It uses Flask, a Python web framework, and Google Cloud Storage to store uploaded images. Users can upload images to the server, and they will be available for viewing on the main page.

> [!NOTE]
> This project provides a basic implementation. You can customize and expand it according to your needs, such as adding user authentication, error handling, and additional features.

<p align="center">
  <img src="/Screenshot1.png" alt="app" width="500"/>
  
  <img src="/Screenshot2.png" alt="app" width="500"/>
</p>


To complete this project, follow this step-by-step guide:

**Step 1: Prepare the Environment**

1.1. Install the required dependencies by running the command:

`` pip install Flask google-cloud-storage ``

1.2. Create a project on the Google Cloud Console and set up access to the Cloud Storage API.

1.3. Download the service account JSON key, save it as yourname.json, and place it in the keys folder at the root of the project.

**Step 2: Create the Project Structure**

2.1. Create a folder named my_photo_app.

2.2. Inside my_photo_app, create the folders keys, templates, and static.

2.3. In the my_photo_app folder, create the files app.py and styles.css.

2.4. In the templates folder, create the file index.html.

**Step 3: Write the Application Code**

3.1. Copy the code provided in app.py into the app.py file in the my_photo_app folder. This code creates a Flask application, sets up the connection to Google Cloud Storage, and defines routes for the main page and image uploads.

3.2. Copy the code provided in index.html into the index.html file in the templates folder. This file contains HTML code to display the list of images and the upload form.

3.3. Copy the code provided in styles.css into the styles.css file in the static folder. This file contains styles for the web page.

Step 4: Configure Google Cloud Storage

4.1. Replace 'yourname.json' in the app.py file with the actual path to your service account JSON key.

4.2. Replace 'bucketname' in the app.py file with the name of your Google Cloud Storage bucket where you want to store the uploaded images.

**Step 5: Run the Application**

5.1. Open a terminal and navigate to the my_photo_app folder where your app.py file is located.

5.2. Run the following command:

``python app.py``

This will start your web application. You will see a message indicating the address where your application is available (e.g., http://127.0.0.1:5000/ by default).

5.3. Open a web browser and navigate to the specified address (e.g., http://127.0.0.1:5000/).

You can now upload images via the form on the main page and view them on the same page.



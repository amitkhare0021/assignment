**Document Upload and Summarization API.**

#Features:
---------
1.File Upload: Upload text, PDF, or DOCX files to the server.
2.Text Summarization: Summarize the content of uploaded documents.

#Technologies Used:
------------------

 **Flask**: Web framework for building the API.
- **Flask-CORS**: Handles Cross-Origin Resource Sharing (CORS).
- **Flask-Migrate**: Handles database migrations.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **Werkzeug**: Provides utilities for secure filename handling.
- **Gensim**: Library used for text summarization (assumed in `summarize_helper.py`).

#Prerequisites:
-------------
1.Python 
2.MySQL database server

#Configure Database:
-------------------
Make sure you have MySQL installed and running. Update the database.

#API Endpoints:
-------------

1. Upload a File:

Endpoint: /upload
Method: POST
Description: Uploads a file to the server.
Request:
Form data: file (the file to upload)
Response:
201 Created: Returns the document ID if the upload is successful.
400 Bad Request: If the file is not provided or the file type is not allowed.


2. Summarize a Document:
Endpoint: /summarize
Method: POST
Description: Summarizes the content of the uploaded document.
Request:
JSON body: { "id": "<document_id>" }

Response:
200 OK: Returns the document ID and the summarized text.
404 Not Found: If the document is not found.
500 Internal Server Error: If an error occurs during summarization.

#For Running Back-end Application:
----------------------------------
1. pip install -r requirements.txt
2. python app.py


#For Running Front-end Application:
-----------------------------------
1. npm start

#Challenges faced during the development of applications:
--------------------------------------------------------

Improving error reporting and handling for issues like database errors, file decoding problems, or summarization failures.

#References Used:
-----------------
1. Official documentations
2. Web

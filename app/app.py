from flask import Flask, request, render_template, redirect, url_for  # Добавлены импорты redirect и url_for
from google.cloud import storage

app = Flask(__name__)

# Replace 'your-key.json' and 'your-bucket' with your values
storage_client = storage.Client.from_service_account_json('')
bucket = storage_client.get_bucket('')

@app.route('/')
def index():
    blobs = bucket.list_blobs()  # Get the list of objects from the bucket
    image_urls = [blob.public_url for blob in blobs]  # Get the public URLs of the objects

    return render_template('index.html', image_urls=image_urls)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "The file was not uploaded"

    file = request.files['file']

    if file.filename == '':
        return "Please select the file to upload"

    blob = bucket.blob(file.filename)
    blob.upload_from_string(file.read(), content_type=file.content_type)

    # After a successful download, redirect the user to the home page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

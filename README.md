# snappit

Django AWS Photo Gallery
This Django application allows users to view and upload photos in different categories. All photos are stored in AWS Cloud.

#Installation
```
Clone the repository: git clone https://github.com/yourusername/your-repo.git
Navigate to the project directory: cd your-repo
Create a virtual environment: python3 -m venv env
Activate the virtual environment: source env/bin/activate
Install the dependencies: pip install -r requirements.txt
Set up the database: python manage.py migrate
Create a superuser: python manage.py createsuperuser
Run the server: python manage.py runserver
```
# Usage
## Viewing photos
To view the photos, navigate to the homepage:


```
http://localhost:8000/
```
You will see a list of categories on the left-hand side. Click on a category to view the photos in that category.


## Upload Photos
bash

```
http://localhost:8000/add/
```
Select a category from the dropdown menu, and choose a photo file to upload. Click the "Upload" button to submit the form.

**AWS Cloud Storage**
All photos uploaded through this application are stored in AWS Cloud. This allows for scalable, reliable, and secure storage of your photos. To configure the AWS Cloud storage settings, update the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, and AWS_S3_REGION_NAME variables in the settings.py file.

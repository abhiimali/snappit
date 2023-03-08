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
Select a category from the dropdown menu, and choose a photo file to upload. Click the "Submit" button to submit the form.



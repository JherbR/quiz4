Clone and Environment

Bash
python -m venv myenv
source myenv/Scripts/activate  # Windows
pip install requirements.txt

python manage.py makemigrations users project tasks
python manage.py migrate

python manage.py runserver

ROUTES
/api/v1/users/login/
/api/v1/users/	GET	List all registered users.
/api/v1/users/create/
/api/v1/projects/	GET	Dashboard list (filtered by role).	Authenticated
/api/v1/projects/<id>/	GET	Detailed view of project and tasks.	Assigned Users
/api/v1/projects/create/
/api/v1/projects/<id>/task/create/

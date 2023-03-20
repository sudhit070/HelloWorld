each "Build Start"
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
each "Build End"
each "Build End"
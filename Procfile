docker: docker-compose up
assets: npm start
web: PYTHONUNBUFFERED=true gunicorn -b localhost:8000 --reload "catwatch.app:create_app()"
worker: celery worker -A catwatch.blueprints.user.tasks -l info -B
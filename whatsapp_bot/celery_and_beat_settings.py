# Celery
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"

# Celery beat
CELERY_BEAT_SCHEDULE = {
	"check_trades_to_place": {
				"task": "auto_predictor.tasks.check_trades_to_place",
				"schedule": crontab(minute=0, hour='6')),  # Run everyday 6am
	}
}

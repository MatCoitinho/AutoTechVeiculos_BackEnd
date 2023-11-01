from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .models import Anuncio

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, CronTrigger(day_of_week='mon', hour='00', minute='00'),replace_existing=True)
def decrementar_pontos():
    anuncios = Anuncio.objects.all()
    for anuncio in anuncios:
        if anuncio.pontos >= 10:
            anuncio.pontos -= 10
            anuncio.save()

        elif anuncio.pontos < 10 and anuncio.pontos>0:
            anuncio.pontos -= 1
            anuncio.save()

register_events(scheduler)
scheduler.start()

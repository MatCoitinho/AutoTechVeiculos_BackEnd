from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .models import Anuncio
from django.utils import timezone

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

@register_job(scheduler, CronTrigger(hour='01', minute='00'), replace_existing=True)
def remover_destaque_expirado():
    agora = timezone.now()
    veiculos_expirados = Anuncio.objects.filter(destaque=True, data_expiracao_destaque__lte=agora)

    for veiculo in veiculos_expirados:
        veiculo.destaque = False
        veiculo.data_expiracao_destaque = None
        veiculo.save()

register_events(scheduler)
scheduler.start()


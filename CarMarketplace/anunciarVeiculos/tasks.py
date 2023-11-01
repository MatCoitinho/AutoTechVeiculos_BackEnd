from .models import Anuncio  # Importa os modelos aqui


def decrementar_pontos():
    anuncios = Anuncio.objects.all()
    for anuncio in anuncios:
        if anuncio.pontos >= 10:
            anuncio.pontos -= 10
            anuncio.save()

        elif anuncio.pontos < 10 and anuncio.pontos>0:
            anuncio.pontos -= 1
            anuncio.save()




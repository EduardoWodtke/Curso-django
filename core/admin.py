from django.contrib import admin

from .models import categoria, pais, tipoAtucao, produtora, membros, filme, atuacao



admin.site.register(categoria)   

admin.site.register(pais)

admin.site.register(tipoAtucao)

admin.site.register(produtora)

admin.site.register(membros)

admin.site.register(filme)

admin.site.register(atuacao)
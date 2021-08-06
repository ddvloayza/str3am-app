# -*- coding: utf-8 -*-

from logging import getLogger
from os.path import normpath
import hashlib
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.template import Context
from django.core.mail import EmailMessage
from apps.web.util import get_info


log = getLogger('django')


def cache_fragment(fragment_name='', *args):
    '''
        Obtiene la llave para un fragmento de cache de un template
    '''
    return 'template.cache.%s.%s' % (fragment_name, hashlib.md5(
        u':'.join([arg for arg in args])).hexdigest())


def choice_to_dict(choice):
    '''
        Convierte una tupla en formato del tipo choices a un diccionario en el
         que el primer elemento de cada par es la llave del diccionario.
    '''

    d = {}
    for c in choice:
        if c[0] not in d.keys():
            d[c[0]] = c[1]

    return d


def chunks(l, n):
    '''
        Retorna un subgrupos de la lista l de n elementos.
    '''

    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def fix_path(path):
    '''
        Normaliza una ruta y se asegura de que termine en un slash
    '''
    path = normpath(path)
    if path[:-1] != '/':
        path = path + '/'
    return path


def get_ip(request):
    '''
        Retorna la IP de un request, considerando la posibilidad de que el
         usuario puede estar detras de un proxy.
    '''

    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if ip:
        ip = ip.split(", ")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip


def model_to_choice(model, value='nombre', text=''):
    '''
        Convierte los datos de un modelo en una lista que puede ser usada
         como 'choices'.
    '''

    if not text:
        text = value

    total = model.objects.all().order_by(text)
    choice = []
    for el in total:
        choice.append((getattr(el, value), getattr(el, text)))

    return choice


class TextTemplateView(TemplateView):
    '''
        TemplateView que usa el mimetype: text/plain
    '''

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'text/plain;charset="utf-8"'

        return super(TemplateView, self).render_to_response(context,
            **response_kwargs)


def dict_not_have_key(diccionario, key):
    if key in diccionario.keys():
        return diccionario[key]
    return None


def envia_email(template, usuario, asunto):
    htmly = get_template(template)
    # c_d = self.cleaned_data
    c_d = {}
    info = get_info()
    c_d['info'] = info
    c_d['user'] = usuario
    # c_d['user_link'] = usuario.get_absolute_url()
    d = Context(c_d)
    html_content = htmly.render(d)

    mail = info.email
    destino = [usuario.email]

    msg = EmailMessage(asunto, html_content, mail, destino)
    msg.content_subtype = "html"
    print ("AFTER SEND")
    msg.send()
    print ("PASSE SEND")


# -*- coding: utf-8 -*-

import urllib.parse as urlparse


class YoutubeVideo(object):
    def __init__(self, url):
        self.url = url

    @property
    def id(self):
        url_data = urlparse.urlparse(self.url)
        query = urlparse.parse_qs(url_data.query)
        try:
            video = query['v'][0]
        except IndexError:
            video = None
        except KeyError:
            video = None
        return video

    @property
    def embed_url(self):
        return 'https://www.youtube.com/embed/{0}'.format(self.id)

    def get_img(self, size=''):
        '''
        Obtiene "miniaturas" del video escogido.

        Args:
            size: tamaño de la miniatura cuyos valores pueden ser:
                  "s", 'm' o 'l' (120x90, 320x180, 480x360)
        '''
        SIZE = {
            's': '2',
            'm': 'mqdefault',
            'l': '0'
        }

        size_yt = SIZE.get(size, '0')

        return 'https://img.youtube.com/vi/{0}/{1}.jpg'.format(
            self.id, size_yt)

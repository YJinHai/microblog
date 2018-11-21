# -*- coding: utf-8 -*-
import json
import hashlib
import random

import requests
from flask_babel import _
from flask import current_app

# 使用有道智云API
appKey = "3b66b72f5451d6c9"
salt = random.randint(1, 65536)


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    sign = appKey + text + str(salt) + current_app.config['MS_TRANSLATOR_KEY']
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://openapi.youdao.com/api?appKey={}&q={}&from={}&to={}&salt={}&sign={}'.format(
        appKey, text, source_language, dest_language, salt, sign),
        headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))['translation'].pop()

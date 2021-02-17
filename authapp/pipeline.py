from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
import os
from authapp.utils import generate_name_file
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile
from geekshop.settings import MEDIA_ROOT, SOCIAL_AUTH_VK_OAUTH2_SCOPE


def save_user_profile(backend, user, response, *args, **kwargs):
    print(response)
    # print(MEDIA_ROOT)
    if backend.name == 'vk-oauth2':
        api_url = urlunparse(
            ('https',
             'api.vk.com',
             '/method/users.get',
             None,
             urlencode(OrderedDict(fields=','.join(SOCIAL_AUTH_VK_OAUTH2_SCOPE),
                                   access_token=response['access_token'],
                                   v='5.92')),
             None
             )
        )

        resp = requests.get(api_url)
        if resp.status_code != 200:
            return

        data = resp.json()['response'][0]
        if data.get('nickname') and data.get('screen_name'):
            if data['nickname']:
                user.username = data['nickname']
            else:
                user.username = data['screen_name']

        if data.get('email'):
            user.email = data['email']

        if data.get('first_name'):
            user.first_name = data['first_name']

        if data.get('last_name'):
            user.last_name = data['last_name']

        if data.get('about'):
            user.shopuserprofile.aboutMe = data['about']

        if data.get('photo_100') and not user.avatar:
            img = requests.get(data['photo_100'])
            name_file = generate_name_file()
            with open(os.path.join(MEDIA_ROOT, 'users_avatar_images', name_file), "wb") as out:
                out.write(img.content)
            out.close()

            user.avatar = os.path.join('users_avatar_images', name_file)

        # TODO: Доделать расчет даты рождения
        # if data.get('bdate'):
        #     bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        #
        #     age = timezone.now().date().year - bdate.year
        #     if age < 18:
        #         user.delete()
        #         raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        user.save()

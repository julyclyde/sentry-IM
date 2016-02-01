# encoding: utf-8
import logging
from sentry_IM import send_IM, VERSION
from django.conf import settings
from sentry.models import User
from sentry.plugins.bases import notify
from sentry.utils.cache import cache


class IMPlugin(notify.NotificationPlugin):
    author = 'REN Xiaolei'
    version = VERSION
    description = "Integrates IM"

    slug = 'IM'
    title = 'IM'
    conf_key = 'mail'  # 使用和MailPlugin相同的发送列表
    project_conf_form = None
    project_default_enabled = True

    logger = logging.getLogger('sentry.plugins.IM')

    def get_send_to(self, project=None):
        """
        该函数抄自MailPlugin
        """
        if project:
            project_id = project.pk
        else:
            project_id = ''

        if not (project and project.team):
            return []

        conf_key = self.get_conf_key()
        cache_key = '%s:send_to:%s' % (conf_key, project_id)

        send_to_list = cache.get(cache_key)
        if send_to_list is None:
            send_to_list = self.get_sendable_users(project)

            send_to_list = filter(bool, send_to_list)
            cache.set(cache_key, send_to_list, 60)  # 1 minute cache

        return send_to_list

    def notify(self, notification):
        event = notification.event
        group = event.group
        project = group.project
        receiver_IDs = self.get_send_to(project)
        if not receiver_IDs:
            return
        else:
            receivers = []
            for i in receiver_IDs:
                localpart = str(User.objects.get(id=i).email).split('@')[0]
                receivers.append(localpart)

        link = group.get_absolute_url()
        text = "Sentry project %s notification:\n%s.\nOpen %s to see." % (project.name, event.message, link)

        D = send_IM.IM(settings.IM_FROMNAME,
                       settings.IM_FROMUID,
                       settings.IM_CLIENT_ID,
                       settings.IM_CLIENT_SECRET)
        D.send_to(receivers, text)

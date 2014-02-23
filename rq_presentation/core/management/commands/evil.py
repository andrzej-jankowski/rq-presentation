# -*- encoding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import django_rq

from django.core.management.base import BaseCommand

from rq_presentation.core.jobs import evil


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        queue = django_rq.get_queue('default')

        return queue.enqueue_call(
            func=evil,
            timeout=15,
        ).id

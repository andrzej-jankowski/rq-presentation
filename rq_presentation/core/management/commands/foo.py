# -*- encoding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import django_rq
import random

from django.core.management.base import BaseCommand

from rq_presentation.core.jobs import foo


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        queue = django_rq.get_queue('default')

        return queue.enqueue_call(
            func=foo,
            args=(random.randint(1, 100),),
        ).id

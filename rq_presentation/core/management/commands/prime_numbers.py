# -*- encoding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import django_rq
import rq
import sys
import time

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from rq_presentation.core.jobs import prime_numbers


class Command(BaseCommand):
    args = '<limit>'
    help = 'Calculate prime numbers.'
    option_list = BaseCommand.option_list + (
        make_option(
            '-l',
            '--limit',
            dest='limit',
            action='store_true',
            default=False,
            help='Limit...',
        ),
        make_option(
            '-j',
            '--job',
            dest='job_id',
            action='store_true',
            default=False,
            help='Job ID...',
        ),
    )

    def handle(self, *args, **kwargs):
        if sum([kwargs['limit'], kwargs['job_id']]) > 1:
            raise CommandError("You can't mix limit and job_id options.")
        elif sum([kwargs['limit'], kwargs['job_id']]) == 0:
            raise CommandError("Choose something...")
        if not args:
            raise CommandError("Specify limit or job_id.")

        queue = django_rq.get_queue('default')

        if kwargs.get('limit', False):
            try:
                limit = int(args[0])
            except (IndexError, ValueError) as e:
                raise CommandError(e)
            job = queue.enqueue_call(
                func=prime_numbers,
                args=(limit,),
                timeout=3600,
                result_ttl=60,
            )
            self.stdout.write("JOB ID = %s" % job.id)

        if kwargs.get('job_id', False):
            job = rq.job.Job.fetch(args[0], django_rq.get_connection())

        while job.result is None and not job.is_failed:
            time.sleep(0.5)
            sys.stdout.write('.')
            sys.stdout.flush()
        if job.is_failed:
            self.stdout.write('\nJOB FAILED\n')
        else:
            self.stdout.write('\n%s\n' % job.result)

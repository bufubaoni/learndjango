#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/24
from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10 # every 10 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'mysite.test_cron_job'    # a unique code

    def do(self):
        print("666666")   # do your thing here
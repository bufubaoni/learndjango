#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/24
from django_rq import job

@job
def cron_job():
    print("666666")

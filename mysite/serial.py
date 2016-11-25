#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/25
from rest_framework import serializers
from models import MyModel
from river.models import State
import json


class MyModelSerializer(serializers.HyperlinkedModelSerializer):
    state_display = serializers.SerializerMethodField()
    state = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all()
    )

    class Meta:
        model = MyModel
        fields = ('id', 'testflow', 'state', 'state_display')


    def get_state_display(self, obj):
        # import pdb
        # pdb.set_trace()
        return obj.state.label

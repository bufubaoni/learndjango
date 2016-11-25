#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/25
from rest_framework import serializers
from models import MyModel
from river.models import State
import json


class MyModelSerializer(serializers.ModelSerializer):
    state_display = serializers.SerializerMethodField()
    state = serializers.PrimaryKeyRelatedField(
        # many=True,
        queryset=State.objects.all()
    )

    # def get_state_display(self,obj):
    #     return ''.join([state.label for state in obj.state.all()])
    # def get_state(self):
    #     return self.get_state_display(self.state)
    class Meta:
        model = MyModel
        # state = serializers
        fields = ('id', 'testflow', 'state', 'state_display')

    def get_state_display(self, obj):
        # import pdb
        # pdb.set_trace()
        return obj.state.label

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/25
from rest_framework import serializers
from river.utils.exceptions import RiverException

from models import MyModel
from river.models import State
import json


class MyModelSerializer(serializers.HyperlinkedModelSerializer):
    state_display = serializers.SerializerMethodField()

    # state = serializers.PrimaryKeyRelatedField(
    #     queryset=State.objects.all()
    # )

    class Meta:
        model = MyModel
        fields = ('id', 'testflow', 'state_id', 'state_display')

    def get_state_display(self, obj):
        # import pdb
        # pdb.set_trace()
        return obj.state.label

    def create(self, validated_data):
        mymodel = MyModel.objects.create(**validated_data)
        try:
            mymodel.proceed(self.context['request'].user)
            mymodel.save()
        except RiverException as e:
            mymodel.delete()
        return mymodel

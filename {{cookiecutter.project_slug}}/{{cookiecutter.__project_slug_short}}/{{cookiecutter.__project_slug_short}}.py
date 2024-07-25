#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Gonzalo Alvarez

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


{%- if cookiecutter.use_loguru == 'y' %}
from loguru import logger
{%- endif %}

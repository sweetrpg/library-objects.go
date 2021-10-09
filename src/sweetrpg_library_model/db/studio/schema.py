# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from sweetrpg_library_model.model.studio import Studio
from sweetrpg_model_core.schema.base import BaseSchema


class StudioSchema(BaseSchema):
    model_class = Studio

    name = fields.String(required=True)  # , load_only=True)
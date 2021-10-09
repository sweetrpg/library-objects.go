# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from datetime import datetime
import logging
from mongoengine import Document, EmbeddedDocument, fields
from pymongo.operations import IndexModel
from pymongo import ASCENDING
from sweetrpg_library_model.db.volume_property.document import VolumePropertyDocument


class VolumeDocument(Document):
    """A mapping object to convert MongoDB data to a Volume object."""

    meta = {
        "indexes": [
            {"name": "volume_slug", "fields": ["slug"], "unique": True},
            {"name": "volume_name", "fields": ["name"]},
            {"name": "volume_system", "fields": ["system"]},
        ],
        "db_alias": "default",
        "collection": "volumes",
        "strict": False,
    }

    name = fields.StringField(min_length=1, max_length=200, required=True)
    slug = fields.StringField(min_length=2, max_length=50, required=True)
    system = fields.StringField(min_length=1, max_length=20, required=True)
    created_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    updated_at = fields.DateTimeField(default=datetime.utcnow, required=True)
    deleted_at = fields.DateTimeField(null=True)
    authors = fields.ListField(field=fields.ReferenceField("AuthorDocument"))
    properties = fields.ListField(fields.EmbeddedDocumentField(VolumePropertyDocument))
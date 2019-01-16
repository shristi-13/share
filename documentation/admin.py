# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib import admin 
from .models import Document
from .models import Tags
from .models import Product
from.models import Project
from easy_select2 import select2_modelform
from easy_select2 import select2_modelform_meta,Select2Multiple, Select2
from social_django.admin import *
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.models import LogEntry

from django.db.models.fields.related import *




admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)

class DocAdmin(admin.ModelAdmin):
	list_display = ['project','get_product','version','author','created_date_time','modified_date_time']
	def get_product(self, obj):
		return obj.project.product
	get_product.short_description = 'Product'
	get_product.admin_order_field = 'project__product'
	
class ProjectAdmin(admin.ModelAdmin):
	list_display = ['project','get_product']
	def get_product(self, obj):
		return obj.product
	get_product.short_description = 'Product'
	get_product.admin_order_field = 'project__product'

admin.site.register(Tags)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Product)
admin.site.register(Document, DocAdmin)
# Register your models here.


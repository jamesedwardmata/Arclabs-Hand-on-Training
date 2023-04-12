from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from.models import Post
from.models import mock_data

class mockdata(resources.ModelResource):
    class Meta:
        model = mock_data

class adminclass(ImportExportModelAdmin):
    resource_class = mockdata

admin.site.register(Post)
admin.site.register(mock_data, adminclass)
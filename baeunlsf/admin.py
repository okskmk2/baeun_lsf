from django.contrib import admin
from .models import (
    UserInfo, QueueInfo, HostGroupInfo, HostGroupMap, HostInfo, JobInfo, JobInfoHist, ProjectInfo, ProjectUserMap,
    QueueHostMap, QueueUserMap
)


class ProjectUserMapAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'user_name',)


class JobInfoAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'job_status', 'project_name', 'command', 'user_name',
                    'queue_name')
    exclude = ('submit_dt', 'start_dt', 'end_dt',)


class QueueInfoAdmin(admin.ModelAdmin):
    list_display = ('queue_name', 'total_job_limit', 'user_job_limit', 'host_job_limit', 'priority',)


class QueueHostMapAdmin(admin.ModelAdmin):
    list_display = ('queue_name', 'host_name',)


class HostInfoAdmin(admin.ModelAdmin):
    list_display = ('host_name', 'host_status', 'host_job_limit',)
    exclude = ('max_cpu_speed', 'cur_cpu_speed', 'max_mem', 'cur_mem',)


admin.site.register(UserInfo)
admin.site.register(QueueInfo, QueueInfoAdmin)
admin.site.register(HostGroupInfo)
admin.site.register(HostGroupMap)
admin.site.register(HostInfo, HostInfoAdmin)
admin.site.register(JobInfo, JobInfoAdmin)
admin.site.register(JobInfoHist)
admin.site.register(ProjectInfo)
admin.site.register(ProjectUserMap, ProjectUserMapAdmin)
admin.site.register(QueueHostMap, QueueHostMapAdmin)
admin.site.register(QueueUserMap)

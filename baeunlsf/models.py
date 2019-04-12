from django.db import models
from .status_enum import HostStatus, JobStatus


class UserInfo(models.Model):
    user_name = models.CharField(max_length=30, primary_key=True)
    user_job_limit = models.IntegerField(default=-1)
    priority = models.IntegerField(default=0)
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'tb_user_info'
        verbose_name_plural = "user"


class ProjectInfo(models.Model):
    project_name = models.CharField(max_length=30, primary_key=True)
    project_leader = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='project_leader')
    project_job_limit = models.IntegerField(default=-1)
    priority = models.IntegerField(default=0)
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = 'tb_project_info'
        verbose_name_plural = "project"


class ProjectUserMap(models.Model):
    project_name = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE, db_column='project_name')
    user_name = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='host_name')
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    def __str__(self):
        return "%s_%s" % (self.project_name, self.user_name)

    class Meta:
        db_table = 'tb_project_user_map'
        verbose_name_plural = "project_user_map"


class HostInfo(models.Model):
    host_name = models.CharField(max_length=30, primary_key=True)
    host_status = models.CharField(max_length=20, default=HostStatus.busy.name,
                                   choices=((tag.name, tag.name) for tag in HostStatus))
    host_job_limit = models.IntegerField(default=-1)
    host_ip = models.CharField(max_length=39)  # IPv6 max_length
    max_cpu_speed = models.IntegerField(null=True, blank=True)
    cur_cpu_speed = models.IntegerField(null=True, blank=True)
    max_mem = models.IntegerField(null=True, blank=True)
    cur_mem = models.IntegerField(null=True, blank=True)
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.host_name

    class Meta:
        db_table = 'tb_host_info'
        verbose_name_plural = "host"


class HostGroupInfo(models.Model):
    host_group_name = models.CharField(max_length=30, primary_key=True)

    class Meta:
        db_table = 'tb_host_group_info'
        verbose_name_plural = "host_group"


class HostGroupMap(models.Model):
    host_name = models.ForeignKey(HostInfo, on_delete=models.CASCADE, db_column='host_name')
    host_group_name = models.ForeignKey(HostGroupInfo, on_delete=models.CASCADE, db_column='host_group_name')
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    class Meta:
        db_table = 'tb_host_group_map'
        verbose_name_plural = "host_group_map"


class QueueInfo(models.Model):
    queue_name = models.CharField(max_length=30, primary_key=True)
    total_job_limit = models.IntegerField(default=-1)
    user_job_limit = models.IntegerField(default=-1)
    host_job_limit = models.IntegerField(default=-1)
    priority = models.IntegerField(default=0)
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.queue_name

    class Meta:
        db_table = 'tb_queue_info'
        verbose_name_plural = "queue"


class QueueUserMap(models.Model):
    queue_name = models.ForeignKey(QueueInfo, on_delete=models.CASCADE, db_column='queue_name')
    user_name = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='user_name')
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    class Meta:
        db_table = 'tb_queue_user_map'
        verbose_name_plural = "queue_user_map"


class QueueHostMap(models.Model):
    queue_name = models.ForeignKey(QueueInfo, on_delete=models.CASCADE, db_column='queue_name')
    host_name = models.ForeignKey(HostInfo, on_delete=models.CASCADE, db_column='host_name')
    reg_dt = models.DateField(auto_now_add=True)
    upd_dt = models.DateField(auto_now=True)

    def __str__(self):
        return "%s_%s" % (self.queue_name, self.host_name)

    class Meta:
        db_table = 'tb_queue_host_map'
        verbose_name_plural = "queue_host_map"


class JobInfo(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_status = models.CharField(max_length=20, default=JobStatus.void.name,
                                  choices=((tag.name, tag.name) for tag in JobStatus))
    command = models.TextField()
    project_name = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE, db_column='project_name')
    user_name = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='user_name')
    queue_name = models.ForeignKey(QueueInfo, on_delete=models.CASCADE, db_column='queue_name')
    submit_dt = models.DateTimeField(auto_now_add=True)
    start_dt = models.DateTimeField(null=True, blank=True)
    end_dt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.job_id)

    class Meta:
        db_table = 'tb_job_info'
        verbose_name_plural = "job"


class JobInfoHist(models.Model):
    job_id = models.IntegerField()
    command = models.TextField()
    queue_name = models.CharField(max_length=30)
    reg_dt = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'tb_job_info_hist'
        verbose_name_plural = "job_history"

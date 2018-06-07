# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .models import Task

import xlsxwriter
# This schedules the xlsx export to 9:30 am on every monday..can be changed by altering the parameters of crontab
@periodic_task(
    run_every=(crontab(hour=9, minute=30, day_of_week=1)),
    name="task_export_xlsx",
    ignore_result=True
)
#function for exporting the task data from the database to the xlsx file
def task_export_xlsx():
    workbook = xlsxwriter.Workbook('tasks01.xlsx',{'remove_timezone': True})
    worksheet = workbook.add_worksheet()
    row=col=0
    worksheet.write(row,col,"Employee Name")
    worksheet.write(row,col+1,"Task Created")
    worksheet.write(row,col+2,"Task Name")
    worksheet.write(row,col+3,"Task Due")
    row+=1
    tasks = Task.objects.all()
    for task in tasks:
        worksheet.write(row,col,task.user.username)
        worksheet.write(row,col+1,task.created.strftime('%d-%m-%Y %H:%M'))
        worksheet.write(row,col+2,task.task_name)
        worksheet.write(row,col+3,task.task_due.strftime('%d-%m-%Y %H:%M'))
        row+=1
    workbook.close()

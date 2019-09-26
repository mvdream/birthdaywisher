from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from django.conf import settings

class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['18:04'] # every 2 hours
    RUN_EVERY_MINS = 2
    RETRY_AFTER_FAILURE_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    # schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'cron_job.MyCronJob'    # a unique code

    def do(self):
        print("mayur")
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mvdream02@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
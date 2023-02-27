from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Mom_task
from django.contrib.auth.models import User
from django.urls import reverse


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ""
        
        # mom_task = Mom_task.objects.get(id=mom_task_id)

        # url = reverse('edit_task', args=(mom_task.id,))
        # 'edit/<int:mom_task_id>/'
        # url = 'all_tasks.html'
        # get_html_url = f'<a href="all_tasks.html"> test title </a>'

        for event in events_per_day:
            # d += f"<li> {event.get_html_url} </li>"
            # d += f"<li> {event.title} </li>"
            d += f"<li> {event.title} <a href="">test link</a></li>"  # noqa

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr> {week} </tr>"

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, request, withyear=True):
        events = Mom_task.objects.filter(
            user=request.user, start_time__year=self.year, start_time__month=self.month  # noqa
        )
        cal = (
            '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'  # noqa
        )  # noqa
        cal += (
            f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"  # noqa
        )  # noqa
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"
        return cal

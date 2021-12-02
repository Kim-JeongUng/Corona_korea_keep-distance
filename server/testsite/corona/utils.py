from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
import datetime

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		events_per_day2 = events.filter(end_time__day=day)
		events_per_day3 = [0,0,0]

		events_per_day3 = events.filter(start_time__day=day - 2)

		d = ''
		d1 = ''
		d2=[0,0,0]
		d2 = ''

		for event in events_per_day:
			d += f'<li> {event.get_html_url}</li>'
		for event in events_per_day2:
			d1 += f'<li> {event.get_html_url}</li>'
		for i in range(3):
			for event in events_per_day3:
				d2 += f'<li> {event.get_html_url}</li>'

		if day != 0:
			if d != '':
				return f"<td><span class='date'>{day}</span><ul>[시작일]{d}</ul></td>"
			if d1 != '':
				return f"<td><span class='date'>{day}</span><ul>[종료일]{d1}</ul></td>"
			for i in range(3):
				if d2 != '':
					return f"<td><span class='date'>{day}</span><ul>{d2}</ul></td>"

		return '<td></td>'
	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
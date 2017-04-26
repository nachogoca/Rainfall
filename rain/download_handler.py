# TODO Refactor download handlers
from .models import PrecipitationMeasurement
from django.db.models.functions import TruncDay, TruncMonth, TruncYear
from django.db.models import Sum
from djqscsv import render_to_csv_response


def handle_download(observatories, start_date, end_date, time_freq):
    if time_freq == 'observation':
        return handle_download_observations(observatories, start_date, end_date)
    elif time_freq == 'day':
        return handle_download_day(observatories, start_date, end_date)
    elif time_freq == 'month':
        return handle_download_month(observatories, start_date, end_date)
    elif time_freq == 'year':
        return handle_download_year(observatories, start_date, end_date)
    else:
        return None


# Request each observation made
def handle_download_observations(observatories, start_date, end_date):
    query = PrecipitationMeasurement.objects.filter(observatory__in=observatories,
                                                    measure_datetime__gte=start_date,
                                                    measure_datetime__lte=end_date)\
                                            .order_by('observatory','measure_datetime')
    return render_to_csv_response(queryset=query)


# Request by day, group by day and sum rainfall_rate column
def handle_download_day(observatories, start_date, end_date):
    # For each observatory defined in observatories list,
    # With a measure datetime between a range, defined by start_date and end_date,
    # truncate the day
    # group by measure day
    # get the rainfall_rate aggregate by day
    # See http://stackoverflow.com/questions/8746014/django-group-by-date-day-month-year
    query = PrecipitationMeasurement.objects.filter(observatory__in=observatories,
                                                    measure_datetime__gte=start_date,
                                                    measure_datetime__lte=end_date)\
                                            .annotate(measure_day=TruncDay('measure_datetime'))\
                                            .values('observatory','observatory__name','measure_day')\
                                            .annotate(Sum('rainfall_rate'))\
                                            .order_by('observatory', 'measure_day')
    return render_to_csv_response(query)


# Request by month, group by month and sum rainfall_rate column
def handle_download_month(observatories, start_date, end_date):
    query = PrecipitationMeasurement.objects.filter(observatory__in=observatories,
                                                    measure_datetime__gte=start_date,
                                                    measure_datetime__lte=end_date)\
                                            .annotate(measure_month=TruncMonth('measure_datetime'))\
                                            .values('observatory','observatory__name','measure_month')\
                                            .annotate(Sum('rainfall_rate'))\
                                            .order_by('observatory', 'measure_month')
    return render_to_csv_response(query)


# Request by year, group by year and sum rainfall_rate column
def handle_download_year(observatories, start_date, end_date):
    query = PrecipitationMeasurement.objects.filter(observatory__in=observatories,
                                                    measure_datetime__gte=start_date,
                                                    measure_datetime__lte=end_date)\
                                            .annotate(measure_year=TruncYear('measure_datetime'))\
                                            .values('observatory','observatory__name','measure_year')\
                                            .annotate(Sum('rainfall_rate'))\
                                            .order_by('observatory', 'measure_year')
    return render_to_csv_response(query)



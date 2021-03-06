import justpy as jp
import pandas as pd

data = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Day"] = data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating'
    },
    subtitle: {
        text: 'Averaged Rating by Day'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}"""


def by_day():
    wp = jp.QuasarPage()
    # https://quasar.dev/style - for styling, etc.
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h1 text-center q-pa-md")
    p = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)
    # hc.options.title.text = "Average Rating by Day"
    # x = [3, 6, 8]
    # y = [4, 7, 9]
    # hc.options.series[0].data = list(zip(x, y))
    hc.options.xAxis.categories = list(day_average.index)  # Creating a new key in chart_def
    hc.options.series[0].data = list(day_average['Rating'])

    return wp


jp.justpy(by_day)

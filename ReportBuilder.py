import csv
from jinja2 import Template
import json 

def sort_csv_by_column(csv_file, sort_column, ascending=False):
    def get_sort_key(row):
        value = row[header.index(sort_column)]
        try:
            return int(value)
        except ValueError:
            return value

    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        sorted_data = sorted(reader, key=get_sort_key, reverse=not ascending)

    return sorted_data


def create_from_csv(csv_file, sort_column):
    site_data = sort_csv_by_column(csv_file, sort_column)


    with open('test_stats.csv', 'r') as file:
        lines = file.readlines()
    load_test_results = []
    for line in lines[1:]:  
        values = line.strip().split(',')
        if len(values) == 22: 
            method, page, request_count, failure_count, median_response, average_response, min_response, max_response, avg_content_size, requests_per_s, failures_per_s, fifty, sixty_six, seventy_five, eighty, ninety, ninety_five, ninety_eight, ninety_nine, ninety_nine_point_nine, ninety_nine_point_ninety_nine, one_hundred = values
            load_test_results.append({
                '': page, 
                'Min Response Time (ms)': "{:.3f}".format(float(min_response)),  
                'Max Response Time (ms)': "{:.3f}".format(float(max_response)),  
                'Average Response Time (ms)': "{:.3f}".format(float(average_response)),
                'Request Count': int(request_count),
                'Failure Count': int(failure_count),
                'Median Response Time': "{:.3f}".format(float(median_response)),
                'Average Content Size': "{:.3f}".format(float(avg_content_size)),
                'Requests/s': "{:.3f}".format(float(requests_per_s)),
                'Failures/s': "{:.3f}".format(float(failures_per_s)),
                '50%': "{:.3f}".format(float(fifty)),
                '66%': "{:.3f}".format(float(sixty_six)),
                '75%': "{:.3f}".format(float(seventy_five)),
                '80%': "{:.3f}".format(float(eighty)),
                '90%': "{:.3f}".format(float(ninety)),
                '95%': "{:.3f}".format(float(ninety_five)),
                '98%': "{:.3f}".format(float(ninety_eight)),
                '99%': "{:.3f}".format(float(ninety_nine)),
                '99.9%': "{:.3f}".format(float(ninety_nine_point_nine)),
                '99.99%': "{:.3f}".format(float(ninety_nine_point_ninety_nine)),
                '100%': "{:.3f}".format(float(one_hundred))
                })  
    
        

    with open('test_stats_history.csv', 'r') as file:
        lines = file.readlines()

    test_stats_history = []
    for line in lines[1:]:
        values = line.strip().split(',')
        if len(values) == 24: 
            timestamp, user_count, _, _, requests_per_s, failures_per_s, fifty, sixty_six, seventy_five, eighty, ninety, ninety_five, ninety_eight, ninety_nine, ninety_nine_point_nine, ninety_nine_point_ninety_nine, one_hundred, total_request_count, total_failure_count, total_median_response_time, total_average_response_time, total_min_response_time, total_max_response_time, total_average_content_size = values
            
            test_stats_history.append({
                'Timestamp': timestamp,
                'User Count': int(user_count),
                'Requests/s': float(requests_per_s),
                'Failures/s': float(failures_per_s),
                '50%': float(fifty) if fifty != 'N/A' else 0,
                '66%': float(sixty_six) if sixty_six != 'N/A' else 0,
                '75%': float(seventy_five) if seventy_five != 'N/A' else 0,
                '80%': float(eighty) if eighty != 'N/A' else 0,
                '90%': float(ninety) if ninety != 'N/A' else 0,
                '95%': float(ninety_five) if ninety_five != 'N/A' else 0,
                '98%': float(ninety_eight) if ninety_eight != 'N/A' else 0,
                '99%': float(ninety_nine) if ninety_nine != 'N/A' else 0,
                '99.9%': float(ninety_nine_point_nine) if ninety_nine_point_nine != 'N/A' else 0,
                '99.99%': float(ninety_nine_point_ninety_nine) if ninety_nine_point_ninety_nine != 'N/A' else 0,
                '100%': float(one_hundred) if one_hundred != 'N/A' else 0,
                'Total Request Count': float(total_request_count),
                'Total Failure Count': int(total_failure_count),
                'Total Median Response Time': float(total_median_response_time),
                'Total Average Response Time': float(total_average_response_time),
                'Total Min Response Time': float(total_min_response_time),
                'Total Max Response Time': float(total_max_response_time),
                'Total Average Content Size': float(total_average_content_size) if total_average_content_size != 'N/A' else 0
            })
        

    with open('test_exceptions.csv', 'r') as file:
        lines = file.readlines()
    load_exceptions = []
    for line in lines[1:]:
        values = line.strip().split(',')
        if len(values) == 4:
            count, message, traceback, node = line.strip().split(',')

            load_exceptions.append((
                count, message, traceback, node
            ))
        else:
            load_exceptions.append((
                0,0,0,0
            ))
    
    
    tabulator_data = [{
        'URL': row[0],
        'Time to Interactive (ms)': row[1],
        'Time to First Byte (ms)': row[2],
        'LCP (ms)': row[3],
        'Load Time (ms)': row[4],
        'Page Size (Bytes)': row[5]
        } for row in site_data]


    load_exception_data =[{
        'Count': row[0],
        'Message': row[1],
        'Traceback': row[2],
        'noce': row[3],
    } for row in load_exceptions]

    chart_data = [{
        'x': row['Page Size (Bytes)'],
        'y': row['Load Time (ms)'],
        'url': row['URL'],
        'LCP': row['LCP (ms)'],
        'TTFB': row['Time to First Byte (ms)']
    } for row in tabulator_data]     


    load_data = json.dumps(load_test_results)
    tabulator_data = json.dumps(tabulator_data)
    chart_data_json = json.dumps(chart_data, indent=4)
    line_chart_data_json = test_stats_history

    timestamps = []
    avg_response_times = []
    users = []
    total_request_count = []
    failures = []
    start_timestamp = int(test_stats_history[0]['Timestamp'])
    for entry in test_stats_history:
        unix_timestamp = int(entry['Timestamp'])
        time_since_start = unix_timestamp - start_timestamp
        avg_response_times.append(int(entry['Total Average Response Time']))
        hours, remainder = divmod(time_since_start, 3600)
        minutes, seconds = divmod(remainder, 60)
        users.append(int(entry['User Count']))
        total_request_count.append(int(entry['Total Request Count']))
        timestamps.append(f"{hours:02}:{minutes:02}.{seconds:02}")
        failures.append(int(entry['Total Failure Count'])) 

    


    template = Template("""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>{{ title }}</title>
                    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tabulator-tables@5.0.11/dist/css/tabulator.min.css">
                    <link href="https://unpkg.com/tabulator-tables@5.5.0/dist/css/tabulator.min.css" rel="stylesheet">
                    <script type="text/javascript" src="https://unpkg.com/tabulator-tables@5.5.0/dist/js/tabulator.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>
                        
                    <!-- Other CSS and script includes -->
                    <style>
                       body {
                                background-color: #1f1f1f;
                                color: #ffffff;
                                font-family: Arial, sans-serif;
                                }
                                
                                .table-container {
                                  
                                    border: 1px solid #333;
                                    max-height: 500px;
                                    margin: 20px auto;
                                    width: 90%;
                                }
                                h1 {
                                    color: #7b7b7b;
                                    font-size: 36px;
                                    text-align: center;
                                    text-transform: uppercase;
                                    letter-spacing: 2px;
                                }

                                #tabulator-container {
                                margin-top: 20px;
                                border: 1px solid #333;
                                

                                }

                                #chart-container {
                                margin-top: 20px;
                                }

                                .tabulator-cell {
                                
                                border: none;
                                color: #ffffff;
                                background-color: #1f1f1f;
                                }


                                .tabulator-header {
                                background-color:#2b2b2b;
                                color: white ;
                                }

                                .tabulator-col-title, .tabulator-col-content,
                                .tabulator-footer-contents {
                                    background-color:#2b2b2b;
                                    color: white ;
                                }
                                

                                

                                
                                
                            .tabulator-paginator {
                                display: flex;
                                justify-content: center;
                                margin-top: 10px;
                            }
                            
                            .tabulator-paginator label{
                                color: #ffffff;

                            }

                            .tabulator-page {
                                margin: 0 5px;
                                cursor: pointer;
                                color:white;
                                text-decoration: underline;
                            }
                            .tabulator-page.tabulator-page-active {
                                font-weight: bold;
                                text-decoration: none;
                            }

                            .graphs-container {
                                width: fit-content;
                                min-width: 80%;
                                display: flex;
                                justify-content: space-between;
                                margin: auto;
                            }
                            @media (max-width: 1200px) {
                                .graphs-container {
                                    flex-direction: column;
                                    align-items: center;
                                }
                            }
                        </style>
                </head>
                <body>
                    <h1>{{ heading }}</h1>
                    <div class="graphs-container"> 
                        <div style="width: 80%; margin: auto;">
                            <h2>
                            Load Time
                            </h2>
                            <canvas id="scatterPlot"></canvas>
                        </div>
                        
                        <div style="width: 80%; margin: auto;">
                            <h2>
                                Load Test Over Time
                            </h2>
                            <canvas id="lineChart"></canvas>
                        </div>
                    </div>            
                                    
                    <!-- Tabulator Table Container -->
                    <div style="width: 90%; margin: auto;">
                        <h2>Page Metrics</h2>
                         <div id="site-results"></div>
                    </div>
                   
                    <div style="width: 90%; margin: auto; margin-top: 5%;">
                        <H2>Load Test Analysis</H2>
                        <div id="load-analysis"></div>
                    </div>
                        
                    
                    
                    <script>
                        
                        const lineChartCtx = document.getElementById('lineChart').getContext('2d');
                        new Chart(lineChartCtx, {
                            type: 'line',
                            data: {
                                labels: {{ timestamps | tojson }},
                                datasets: [{
                                    label: 'Response Time',
                                    'borderColor': 'rgba(75, 192, 192, 1)',
                                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                                    data: {{ avg_response_times | tojson }},
                                    pointStyle: 'circle',
                                    pointRadius: 2,
                                    pointHoverRadius: 10,
                                    pointHoverBackgroundColor: 'rgba(75, 192, 192, 1)',
                                    pointHoverBorderColor: 'rgba(75, 192, 192, 1)',
                                }, {
                                    label: 'Users',
                                    data: {{ users | tojson }},
                                    type: 'line',
                                    pointRadius: 0,
                                    borderColor: 'rgba(255, 99, 132, 1)', 
                                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                                }, {
                                    label: 'Total Request Count',
                                    data: {{ total_request_count | tojson}},
                                    pointRadius: 0,
                                    borderColor: 'rgba(54, 162, 235, 1)',  
                                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                                }, {
                                    label: 'Total Failures',
                                    data: {{ failures | tojson}},
                                    pointRadius: 0,
                                    borderColor: 'rgba(128, 0, 128, 1)',   // Purple color for border
                                    backgroundColor: 'rgba(128, 0, 128, 0.2)',
                                }],
                            },
                            options: {
                                responsive: true,
                                scales: {
                                    x: {
                                        title: {
                                            display: true,
                                            text: 'Time Elapsed',
                                        },
                                    },
                                    y: {
                                        title: {
                                            display: true,
                                            text: 'Time (ms)',
                                        },
                                    },
                                },

                                plugins: {
                                    zoom: {
                                        zoom: {
                                        wheel: {
                                            enabled: true,
                                        },
                                        pinch: {
                                            enabled: true
                                        },
                                        mode: 'xy',
                                        }
                                    }, tooltip: {
                                            callbacks: {
                                                label: function (context) {
                                                    var dataIndex = context.dataIndex;
                                                    var datasets = context.chart.data.datasets;
                                                    var responseTime = datasets[0].data[dataIndex];
                                                    var users = datasets[1].data[dataIndex];
                                                    var totalRequests = datasets[2].data[dataIndex];
                                                    var totalFailures = datasets[3].data[dataIndex];

                                                    return `Response Time: ${responseTime} ms | Users: ${users} | Total Requests: ${totalRequests} | Total Failures: ${totalFailures}`;
                                                }
                                            }
                                      }
                                } 
                            },
                        });
 

                        var chartDataStr = {{ chart_data | tojson }};
                        
                       

                            var chartData = JSON.parse(chartDataStr);
                            var cd = chartData
                                
                                chartData.forEach(function (point) {
                                    point.x = parseFloat(point.x);
                                    point.y = parseFloat(point.y);
                                });
                            
                                var lcpData = cd.map(function (point) {
                                    return { x: point.x, y: parseFloat(point.LCP), 'url': point.url};
                                });
                            
                                
                                var ttfbData = cd.map(function (point) {
                                    return { x: point.x, y: parseFloat(point.TTFB), 'url': point.url};
                                });

                            
                            var options = {
                                responsive: true,
                                scales: {
                                            x: {
                                                type: 'linear',
                                                position: 'bottom',
                                                title: {
                                                    display: true,
                                                    text: 'Page Size (Bytes)'
                                                }
                                            },
                                            y: {
                                                type: 'linear',
                                                position: 'left',
                                                title: {
                                                    display: true,
                                                    text: 'Time (ms)'
                                                }
                                            }
                                        },
                                 plugins: {
                                            tooltip: {
                                                callbacks: {
                                                    label: function(context) {
                                                        var dataIndex = context.dataIndex;
                                                        var dataPoint = context.dataset.data[dataIndex];
                                                        return dataPoint.url + " - Load Time: "   + dataPoint.y + " (ms) Page Size: " + dataPoint.x + " (bytes)";
                                                    }
                                                }
                                            }, zoom: {
                                                    zoom: {
                                                    wheel: {
                                                        enabled: true,
                                                    },
                                                    pinch: {
                                                        enabled: true
                                                    },
                                                    mode: 'xy',
                                                    }
                                                }
                                        }
                            };

                            
                            var ctx = document.getElementById('scatterPlot').getContext('2d');
                            var scatterChart = new Chart(ctx, {
                                type: 'scatter',
                                    data: {
                                        datasets: [{
                                            label: 'Load Time',
                                            data: chartData,
                                            
                                            pointStyle: 'circle',
                                            pointRadius: 2,
                                            pointStyle: 'circle',
                                            pointRadius: 2,
                                            pointHoverRadius: 10,
                                            backgroundColor: 'rgba(54, 162, 235, 0.2)', 
                                            borderColor: 'rgba(54, 162, 235, 1)',     
                                            pointHoverBackgroundColor: 'rgba(54, 162, 235, 1)', 
                                            pointHoverBorderColor: 'rgba(54, 162, 235, 1)', 
                                        },  {
                                            label: 'LCP',
                                            data: lcpData,
                                            borderColor: 'rgba(75, 192, 192, 1)',
                                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                                            pointStyle: 'circle',
                                            pointRadius: 2,
                                            pointHoverRadius: 10,
                                            pointHoverBackgroundColor: 'rgba(75, 192, 192, 1)',
                                            pointHoverBorderColor: 'rgba(75, 192, 192, 1)'
                                        },
                                        {
                                            label: 'TTFB',
                                            data: ttfbData,
                                            borderColor: 'rgba(255, 99, 132, 1)',  
                                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                                            pointStyle: 'circle',
                                            pointRadius: 2,
                                            pointHoverRadius: 10,
                                            pointHoverBackgroundColor: 'rgba(255, 99, 132, 1)',
                                            pointHoverBorderColor: 'rgba(255, 99, 132, 1)'
                                        }]
                                    },
                                    options: options
                            });
                        
                        var loadanalysistable = new Tabulator('#load-analysis', {
                            data: {{ load_analysis_tabulator_data | tojson }},
                            columns: [
                            
                                { title: 'URL', field: '', formatter: function(cell, formatterParams, onRendered) {
                                    return cell.getRow().getData()[''];  
                                }},
                                { title: 'Min Response Time (ms)', field: 'Min Response Time (ms)' },
                                { title: 'Max Response Time (ms)', field: 'Max Response Time (ms)' },
                                { title: 'Average Response Time (ms)', field: 'Average Response Time (ms)' },
                                { title: 'Request Count', field: 'Request Count' },
                                { title: 'Failure Count', field: 'Failure Count' },
                                { title: 'Median Response Time', field: 'Median Response Time' },
                                { title: 'Average Content Size', field: 'Average Content Size' },
                                { title: 'Requests/s', field: 'Requests/s' },
                                { title: 'Failures/s', field: 'Failures/s' },
                                { title: '50%', field: '50%' },
                                { title: '66%', field: '66%' },
                                { title: '75%', field: '75%' },
                                { title: '80%', field: '80%' },
                                { title: '90%', field: '90%' },
                                { title: '95%', field: '95%' },
                                { title: '98%', field: '98%' },
                                { title: '99%', field: '99%' },
                                { title: '99.9%', field: '99.9%' },
                                { title: '99.99%', field: '99.99%' },
                                { title: '100%', field: '100%' }
                            ],
                        pagination: 'local', 
                        paginationSize: 10,   
                        paginationSizeSelector: [10, 20, 50], 
                        paginationButtonCount: 5
                        });

                       
                        var sitetable = new Tabulator('#site-results', {
                            data: {{ tabulator_data | safe }},
                            columns: [
                                { title: 'URL', field: 'URL' },
                                { title: 'Time to Interactive (ms)', field: 'Time to Interactive (ms)' },
                                { title: 'Time to First Byte (ms)', field: 'Time to First Byte (ms)' },
                                { title: 'LCP (ms)', field: 'LCP (ms)' },
                                { title: 'Load Time (ms)', field: 'Load Time (ms)' },
                                { title: 'Page Size (Bytes)', field: 'Page Size (Bytes)' }
                            ],
                        pagination: 'local', 
                        paginationSize: 10,   
                        paginationSizeSelector: [10, 20, 50], 
                        paginationButtonCount: 5
                        });

                    </script>
                    
                    <script src="https://cdn.jsdelivr.net/npm/tabulator-tables@5.0.11/dist/js/tabulator.min.js"></script>
                    <!-- Other script includes -->
                </body>
                </html>
                """)      
    
    html_code = template.render(title="Result Page", heading="Site Report",failures=failures, total_request_count=total_request_count, users=users, timestamps=timestamps, avg_response_times= avg_response_times, line_chart_data_json=line_chart_data_json, chart_data=chart_data_json, tabulator_data=tabulator_data, load_analysis_tabulator_data=load_data)

    with open("output.html", "w") as file:
        file.write(html_code)

if __name__ == '__main__':
    input_csv = 'sitetestresults.csv'  
    sort_by_column = 'Time to Interactive (ms)'

    create_from_csv(input_csv, sort_by_column)

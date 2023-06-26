'use strict';
document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        floatchart();
    }, 500);
});

function floatchart() {
    var myChart = echarts.init(document.getElementById('chart'));

    // chart
    (function () {
        var option = {
            title: {
                text: "Personal Resource in " + chart_year,
                subtext: chart_username,
                left: "center",
                top: 'top',
                textStyle: {
                    fontSize: 20
                },
                subtextStyle: {
                    fontSize: 15
                }
            },
            legend: {
                top: '12%',
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            grid: {
                top: '16%',
                left: '13%',
                right: '2%',
                bottom: '5%',
                containLabel: false
            },
            textStyle: {
                color: 'black'
            },
            xAxis: {},
            yAxis: {type: 'category'},
            dataset: chart_dataframe,
            color: ['#3C1361', '#5E2D79', '#7B4F8E', '#986EA3',
                '#B18FCF', '#C9B9E8', '#D7D2EE', '#BDD8EA',
                '#A2C8EC', '#7FA3D1', '#5E7FA2', '#3C5F73'],
            series: Array(12).fill(
                {
                    type: 'bar',
                    stack: 'total',
                    // seriesLayoutBy: 'row',
                    label: {show: true},
                    // barWidth: '100%',
                    emphasis: {
                        focus: 'series'
                    }
                }
            ),
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);

        // 根据select标签更新图表
        var chartSelector = document.getElementById('chart-selector');

        chartSelector.addEventListener('change', function () {
            var selectedValue = chartSelector.value;
            if (selectedValue === 'Months for each project') {
                var new_option = {
                    title: {
                        text: "Personal Resource in " + chart_year,
                        subtext: chart_username,
                        left: "center",
                        top: 'top',
                        textStyle: {
                            fontSize: 20
                        },
                        subtextStyle: {
                            fontSize: 15
                        }
                    },
                    legend: {
                        top: '12%',
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    grid: {
                        top: '16%',
                        left: '13%',
                        right: '2%',
                        bottom: '5%',
                        containLabel: false
                    },
                    textStyle: {
                        color: 'black'
                    },
                    xAxis: {},
                    yAxis: {type: 'category'},
                    dataset: chart_dataframe,
                    color: ['#3C1361', '#5E2D79', '#7B4F8E', '#986EA3',
                        '#B18FCF', '#C9B9E8', '#D7D2EE', '#BDD8EA',
                        '#A2C8EC', '#7FA3D1', '#5E7FA2', '#3C5F73'],
                    series: Array(12).fill(
                        {
                            type: 'bar',
                            stack: 'total',
                            // seriesLayoutBy: 'row',
                            label: {show: true},
                            // barWidth: '100%',
                            emphasis: {
                                focus: 'series'
                            }
                        }
                    ),
                };
                myChart.setOption(new_option, true)
            } else if (selectedValue === 'Projects for each month') {
                var new_option = {
                    notMerge: true,
                    title: {
                        text: "Personal Resource in " + chart_year,
                        subtext: chart_username,
                        left: "center",
                        top: 'top',
                        textStyle: {
                            fontSize: 20
                        },
                        subtextStyle: {
                            fontSize: 15
                        }
                    },
                    legend: {
                        top: '12%',
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    grid: {
                        top: '16%',
                        left: '8%',
                        right: '4%',
                        bottom: '5%',
                        containLabel: false
                    },
                    textStyle: {
                        color: 'black'
                    },
                    xAxis: {type: 'category'},
                    yAxis: {},
                    dataset: chart_dataframe,
                    color: ['#562966', '#7d56c1', '#50adff', '#26fdfa'],
                    series: Array(4).fill(
                        {
                            type: 'bar',
                            stack: 'total',
                            seriesLayoutBy: 'row',
                            label: {show: true},
                            // barWidth: '100%',
                            emphasis: {
                                focus: 'series'
                            }
                        }
                    ),
                };
                myChart.setOption(new_option, true)
            }
        });


    })();
    window.onresize = function () {
        myChart.resize();
    };

};


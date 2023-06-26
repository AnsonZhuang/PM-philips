'use strict';
document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        floatchart();
        // floatchart2();
    }, 500);
});

function floatchart() {
    var myChart = echarts.init(document.getElementById('chart'));

    // chart
    (function () {
        var option = {
            title: {
                text: chart_project_name + " (" + chart_year + ")",
                subtext: "Project Resource Overview",
                left: "center",
                // top: '0% ',
                textStyle: {
                    fontSize: 15
                },
                subtextStyle: {
                    fontSize: 12
                }
            },
            toolbox: {
                show: true,
                feature: {
                    mark: {show: true},
                    restore: {show: true},
                    saveAsImage: {show: true}
                }
            },
            legend: {
                top: 55,
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    // Use axis to trigger tooltip
                    type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
                }
            },
            grid: {
                top: 95,
                left: '10%',
                right: '2%',
                bottom: '7%',
                containLabel: false
            },
            textStyle: {
                color: 'black',
                fontSize: 10
            },
            xAxis: {},
            yAxis: {
                type: 'category',
                // max: 10
            },
            dataset: chart_dataframe,
            // ['Project', 'Jan', ……, 'Dec']
            // ['A', '10', ……, '50']
            // ['B', '10', ……, '50']
            // ['C', '10', ……, '50']
            color: ['#3C1361', '#5E2D79', '#7B4F8E', '#986EA3',
                '#B18FCF', '#C9B9E8', '#D7D2EE', '#BDD8EA',
                '#A2C8EC', '#7FA3D1', '#5E7FA2', '#3C5F73'],
            series: Array(12).fill(
                {
                    type: 'bar',
                    interval: ' 10%',
                    stack: 'total',
                    // seriesLayoutBy: 'row',
                    label: {show: true},
                    barGap: '0%',
                    // barCategoryGap: '0%',
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
            if (selectedValue === 'Months(bar)') {
                var new_option = option;
                myChart.setOption(new_option, true)
            } else if (selectedValue === 'Months(pie)') {
                const pie_series = [];
                const x_1 = 14;
                const y_1 = 35;
                const x_step = 23;
                const y_step = 27;
                const col_cnt = 3;
                const row_cnt = 12 / col_cnt
                const list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                for (let i = 0; i < 12; i++) {
                    var center_x = (x_1 + Math.floor(i % row_cnt) * x_step).toString() + '%'
                    var center_y = (y_1 + Math.floor(i / row_cnt) * y_step).toString() + '%'
                    pie_series.push({
                        name: list[i],
                        type: 'pie',
                        radius: ['20%','10%'],
                        center: [center_x, center_y],
                        label: {
                            position: 'outer',
                            show: true,
                            alignTo: 'labelLine',
                            bleedMargin: 20,
                            formatter: '{b}'+'{c}' //自定义显示格式(b:name, c:value, d:百分比)
                            // formatter: '{d}%' //自定义显示格式(b:name, c:value, d:百分比)
                        },
                        encode: {
                            itemName: 'User',
                            // value: list[i%6]
                            value: list[i]
                        },
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    });
                }
                var new_option = {
                    title: [
                        {
                            text: chart_project_name + " (" + chart_year + ")",
                            subtext: "Project Resource Overview",
                            left: "center",
                            // top: '0% ',
                            textStyle: {
                                fontSize: 15
                            },
                            subtextStyle: {
                                fontSize: 12
                            }
                        },
                        {
                            subtext: 'Jan',
                            left: '8%',
                            top: '18%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Feb',
                            left: '31%',
                            top: '18%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Mar',
                            left: '54%',
                            top: '18%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Apr',
                            left: '77%',
                            top: '18%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'May',
                            left: '8%',
                            top: '45%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Jun',
                            left: '31%',
                            top: '45%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Jul',
                            left: '54%',
                            top: '45%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Aug',
                            left: '77%',
                            top: '45%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Sep',
                            left: '8%',
                            top: '72%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Oct',
                            left: '31%',
                            top: '72%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Nov',
                            left: '54%',
                            top: '72%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        },
                        {
                            subtext: 'Dec',
                            left: '77%',
                            top: '72%',
                            textAlign: 'center',
                            subtextStyle: {
                                fontSize: 20
                            }
                        }
                    ],
                    legend: {
                        top: 55,
                    },
                    tooltip: {
                        trigger: 'item',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    grid: {
                        top: '45%',
                        left: '6%',
                        right: '2%',
                        bottom: '7%',
                        containLabel: true,
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            mark: {show: true},
                            restore: {show: true},
                            saveAsImage: {show: true}
                        }
                    },
                    dataset: chart_dataframe_pie,
                    color: ['#516b91', '#59c4e6', '#edafda', '#93b7e3',
                        '#a5e7f0', '#cbb0e3', '#0db3e5', '#b087d0',
                        '#fcd8d4', '#62fce8', '#07a2a4', '#0ee0a7'],
                    // color: ['#3C1361', '#5E2D79', '#7B4F8E', '#986EA3',
                    //         '#B18FCF', ' #C9B9E8', '#D7D2EE', '#BDD8EA',
                    //         '#A2C8EC', '#7FA3D1', '#5E7FA2', '#3C5F73'],
                    series: pie_series,
                };
                myChart.setOption(new_option, true)
            } else if (selectedValue === 'Members(bar)') {
                var new_option = {
                    notMerge: true,
                    title: {
                        text: chart_project_name + " (" + chart_year + ")",
                        subtext: "Project Resource Overview",
                        left: "center",
                        top: 'top',
                        textStyle: {
                            fontSize: 15
                        },
                        subtextStyle: {
                            fontSize: 12
                        }
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            mark: {show: true},
                            restore: {show: true},
                            saveAsImage: {show: true}
                        }
                    },
                    legend: {
                        top: '15%',
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    grid: {
                        top: 95,
                        left: '6%',
                        right: '2%',
                        bottom: '7%',
                        containLabel: false,
                    },
                    textStyle: {
                        color: 'black'
                    },
                    xAxis: {type: 'category'},
                    yAxis: {},
                    dataset: chart_dataframe,
                    color: ['#516b91', '#59c4e6', '#edafda', '#93b7e3',
                        '#a5e7f0', '#cbb0e3', '#0db3e5', '#b087d0',
                        '#fcd8d4', '#62fce8', '#07a2a4', '#0ee0a7'],
                    series: Array(chart_row_cnt).fill(
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


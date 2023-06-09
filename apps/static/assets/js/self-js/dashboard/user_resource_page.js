'use strict';
document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        floatchart();
        floatchart2();
    }, 500);
});

function floatchart() {
    var myChart = echarts.init(document.getElementById('chart'));

    // chart
    (function () {
        var option = {
            title: {
                text: chart_username + " (" + chart_year + ")",
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
                containLabel: true
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
                // var new_option = {
                //     title: {
                //         text: "Personal Resource in " + chart_year,
                //         subtext: chart_project_name,
                //         left: "center",
                //         top: 'top',
                //         textStyle: {
                //             fontSize: 15
                //         },
                //         subtextStyle: {
                //             fontSize: 12
                //         }
                //     },
                //     legend: {
                //         top: '15%',
                //     },
                //     tooltip: {
                //         trigger: 'axis',
                //         axisPointer: {
                //             type: 'shadow'
                //         }
                //     },
                //     grid: {
                //         top: '25%',
                //         left: '10%',
                //         right: '2%',
                //         bottom: '7%',
                //         containLabel: false
                //     },
                //     textStyle: {
                //         color: 'black'
                //     },
                //     xAxis: {},
                //     yAxis: {type: 'category'},
                //     dataset: chart_dataframe,
                //     color: ['#3C1361', '#5E2D79', '#7B4F8E', '#986EA3',
                //         '#B18FCF', '#C9B9E8', '#D7D2EE', '#BDD8EA',
                //         '#A2C8EC', '#7FA3D1', '#5E7FA2', '#3C5F73'],
                //     series: Array(12).fill(
                //         {
                //             type: 'bar',
                //             stack: 'total',
                //             // seriesLayoutBy: 'row',
                //             label: {show: true},
                //             // barWidth: '100%',
                //             emphasis: {
                //                 focus: 'series'
                //             }
                //         }
                //     ),
                // };
                var new_option = option;
                myChart.setOption(new_option, true)
            } else if (selectedValue == 'Months(pie)') {
            } else if (selectedValue === 'Members(bar)') {
                var new_option = {
                    notMerge: true,
                    title: {
                        text: chart_project_name + "(" + chart_year + ")",
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
                    legend: {
                        top: 55,
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
                        containLabel: true,
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
            } else if (selectedValue == 'Members(pie)') {

            }
        });


    })();
    window.onresize = function () {
        myChart.resize();
    };

};


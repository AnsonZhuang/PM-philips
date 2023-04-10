'use strict';
document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
    floatchart();
  }, 500);
});
function floatchart() {
 var myChart = echarts.init(document.getElementById('chart_1'));
      var option = {
        title: {
          text: "Personal Resource in 2023",
          subtext: "Zhuohang Zhuang",
          left: "center",
          top: 'top',
          textStyle: {
            fontSize: 30
          },
          subtextStyle: {
            fontSize: 20
          }
        },
        legend: {
          top: '12%',
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            // Use axis to trigger tooltip
            type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
          }
        },
        grid: {
          top: '16%',
          left: '15%',
          right: '2%',
          bottom: '5%',
          containLabel: false
        },
        textStyle: {
          color: 'black'
        },
        xAxis: {},
        yAxis: { type: 'category' },
        dataset: personal_resource_this_year,
          // {
          // dimensions: ['product', 'Mon', 'Tue', 'Wed'],
          // source: [
          //   { product: 'Matcha Latte', 'Mon': 43.3, 'Tue': 85.8, 'Wed': 93.7 },
          //   { product: 'Milk Tea', 'Mon': 83.1, 'Tue': 73.4, 'Wed': 55.1 },
          //   { product: 'Cheese Cocoa', 'Mon': 86.4, 'Tue': 65.2, 'Wed': 82.5 },
          //   { product: 'Walnut Brownie', 'Mon': 72.4, 'Tue': 53.9, 'Wed': 39.1 }
          // ]
          // },
        color: ['#3C1361', '#5E2D79', '#7B4F8E', '#986EA3',
                '#B18FCF', '#C9B9E8', '#D7D2EE', '#BDD8EA',
                '#A2C8EC', '#7FA3D1', '#5E7FA2', '#3C5F73'],
        series: Array(12).fill(
            {
                type: 'bar',
                stack: 'total',
                label: { show: true },
                emphasis: {
                    focus: 'series'
                }
            }
        ),

      };
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
};


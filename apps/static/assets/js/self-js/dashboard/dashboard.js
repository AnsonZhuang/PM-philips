'use strict';
document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
    floatchart();
  }, 500);
});
function floatchart() {

  // function 1 Resource This Year/Month
  (function () {
    var options = {
      chart: {
        id: 'growthchart',
        type: 'bar',
        height: 480,
        stacked: true,
        toolbar: {
          show: true
        }
      },
      plotOptions: {
        bar: {
          horizontal: true,
          columnWidth: '50%'
        }
      },
      dataLabels: {
        enabled: true

      },
      colors: ['#00fffa', '#2196f3', '#673ab7', '#3a034b', '#cb38ff', '#ac6262'],
      series: personal_resource_months_of_project,
      responsive: [
        {
          breakpoint: 480,
          options: {
            legend: {
              position: 'bottom',
              offsetX: -10,
              offsetY: 0
            }
          }
        }
      ],
      xaxis: {
        type: 'category',
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
      },
      grid: {
        strokeDashArray: 4
      },
      tooltip: {
        theme: 'dark'
      }
    };
    var chart = new ApexCharts(document.querySelector('#growthchart'), options);
    chart.render();

    var chartSelector = document.getElementById('resource-chart-selector');
    chartSelector.addEventListener('change', function (){
      var selectedValue = chartSelector.value;
      // 年度 - 个人资源 - 条形堆叠图
      if (selectedValue === 'This Year - Stack') {
        chart.updateOptions({
          chart: {
            id: 'growthchart',
            type: 'bar',
            height: 480,
            stacked: true,
            toolbar: {
              show: true
            }
          },
          plotOptions: {
            bar: {
              horizontal: true,
              columnWidth: '50%'
            }
          },
          dataLabels: {
            enabled: true

          },
          colors: ['#00fffa', '#2196f3', '#673ab7', '#3a034b', '#cb38ff', '#ac6262'],
          series: personal_resource_months_of_project,
          responsive: [
            {
              breakpoint: 480,
              options: {
                legend: {
                  position: 'bottom',
                  offsetX: -10,
                  offsetY: 0
                }
              }
            }
          ],
          xaxis: {
            type: 'category',
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
          },
          grid: {
            strokeDashArray: 4
          },
          tooltip: {
            theme: 'dark'
          }
        })
      // 年度 - 个人资源 - 条形比较图
      }else if(selectedValue === 'This Year - Parallel'){
        chart.updateOptions({
          chart: {
            id: 'growthchart',
            type: 'bar',
            height: 480,
            stacked: false,
            toolbar: {
              show: true
            }
          },
          plotOptions: {
            bar: {
              horizontal: true,
              columnWidth: '50%'
            }
          },
          dataLabels: {
            enabled: false
          },
          colors: ['#00fffa', '#2196f3', '#673ab7', '#3a034b', '#cb38ff', '#ac6262'],
          series: personal_resource_months_of_project,
          responsive: [
            {
              breakpoint: 480,
              options: {
                legend: {
                  position: 'bottom',
                  offsetX: -10,
                  offsetY: 0
                }
              }
            }
          ],
          xaxis: {
            type: 'category',
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
          },
          grid: {
            strokeDashArray: 4
          },
          tooltip: {
            theme: 'dark'
          }
        })
      }
      // 月度 - 个人资源 - 比例图
      else if(selectedValue === 'This Month - Donut'){
        chart.updateOptions({
          chart: {
              type: 'donut',
              width: '100%',
              height: 400,

          },
          dataLabels: {
            enabled: false,
          },
          plotOptions: {
            pie: {
              customScale: 0.8,
              donut: {
                size: '75%',
              },
              offsetY: 20,
            },
            stroke: {
              colors: undefined
            }
          },
            colors: ['#00D8B6','#008FFB',  '#FEB019', '#FF4560', '#775DD0'],
          title: {
            text: 'Department Sales',
            style: {
              fontSize: '18px'
            }
          },
          series: personal_resource_this_month['series'],
          labels: personal_resource_this_month['labels'],
          responsive: [
            {
              breakpoint: 480,
              options: {
                legend: {
                  position: 'bottom',
                  offsetX: -10,
                  offsetY: 0
                }
              }
            }
          ]
        })
      }
    });
  })();





  //  function 4
  (function () {
    var options = {
      chart: {
        type: 'area',
        height: 95,
        stacked: true,
        sparkline: {
          enabled: true
        }
      },
      colors: ['#673ab7'],
      stroke: {
        curve: 'smooth',
        width: 1
      },
      series: [
        {
          data: [0, 15, 10, 50, 30, 40, 25]
        }
      ]
    };
    var chart = new ApexCharts(document.querySelector('#bajajchart'), options);
    chart.render();
  })();

}

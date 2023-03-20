'use strict';
document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
    floatchart();
  }, 500);
});

function floatchart() {
  //  function 1
  (function () {
    var options = {
      chart: {
        type: 'line',
        height: 90,
        sparkline: {
          enabled: true
        }
      },
      dataLabels: {
        enabled: false
      },
      colors: ['#FFF'],
      stroke: {
        curve: 'smooth',
        width: 3
      },
      series: [
        {
          name: 'series1',
          data: [45, 66, 41, 89, 25, 44, 9, 54]
        }
      ],
      yaxis: {
        min: 5,
        max: 95
      },
      tooltip: {
        theme: 'dark',
        fixed: {
          enabled: false
        },
        x: {
          show: false
        },
        y: {
          title: {
            formatter: function (seriesName) {
              return 'Total Earning';
            }
          }
        },
        marker: {
          show: false
        }
      }
    };
    var chart = new ApexCharts(document.querySelector('#tab-chart-1'), options);
    chart.render();
  })();

  //  function 2
  (function () {
    var options = {
      chart: {
        type: 'line',
        height: 90,
        sparkline: {
          enabled: true
        }
      },
      dataLabels: {
        enabled: false
      },
      colors: ['#FFF'],
      stroke: {
        curve: 'smooth',
        width: 3
      },
      series: [
        {
          name: 'series1',
          data: [35, 44, 9, 54, 45, 66, 41, 69]
        }
      ],
      yaxis: {
        min: 5,
        max: 95
      },
      tooltip: {
        theme: 'dark',
        fixed: {
          enabled: false
        },
        x: {
          show: false
        },
        y: {
          title: {
            formatter: function (seriesName) {
              return 'Total Earning';
            }
          }
        },
        marker: {
          show: false
        }
      }
    };
    var chart = new ApexCharts(document.querySelector('#tab-chart-2'), options);
    chart.render();
  })();

  //  function 3
  (function () {
    var options = {
      chart: {
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
      colors: ['#00fffa', '#2196f3', '#673ab7', '#cb38ff'],
      series: [
        {
          name: 'Rubicon 2.0',
          data: [35, 125, 35, 35, 35, 80, 35, 20, 35, 45, 15, 75]
        },
        {
          name: 'Intrepid NMPA',
          data: [35, 15, 15, 35, 65, 40, 80, 25, 15, 85, 25, 75]
        },
        {
          name: 'DFM100 NBP Overpressue',
          data: [35, 145, 35, 35, 20, 105, 100, 10, 65, 45, 30, 10]
        },
        {
          name: 'ECR Sustaining ALS',
          data: [0, 0, 75, 0, 0, 115, 0, 0, 0, 0, 150, 0]
        }
      ],
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

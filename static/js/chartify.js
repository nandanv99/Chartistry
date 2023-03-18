$('.add-pie-chart').click('click', function() {
    var attribute_name = $(this).text().trim(); // Replace with desired attribute name
    var $existingChart = $('.drop-item canvas[data-attribute="' + attribute_name + '"]');
    if ($existingChart.length) {
      // Chart already exists, update its data
      var chart = $existingChart.data('chart');
      var newData = [];
      for (var i = 0; i < 4; i++) {
        newData.push(Math.floor(Math.random() * 100));
      }
      chart.data.datasets[0].data = newData;
      chart.update();
    } else {
      // Chart doesn't exist, create a new one
      var $el = $('<canvas class="drop-item"></canvas>').attr('data-attribute', attribute_name);
      $el.append($('<button type="button" class="btn btn-default btn-xs remove"><span class="fa-solid fa-trash text-white"></span></button>').click(function () { $(this).parent().detach(); }));
      $('#dropzone').append($el);
  
      // Generate random data for the chart
      var data = [];
      for (var i = 0; i < 4; i++) {
        data.push(Math.floor(Math.random() * 100));
      }
      console.log("data is pie :",data)
  
      // Create the pie chart
      var ctx = $el[0].getContext('2d');
      var chart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4'],
          datasets: [{
            label: attribute_name,
            data: data,
            backgroundColor: [
              '#ff6384',
              '#36a2eb',
              '#ffce56',
              '#d92136'
            ]
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          legend: {
            position: 'bottom'
          },
          title: {
            display: true,
            text: attribute_name
          },
          animation: {
            animateScale: true,
            animateRotate: true
          }
        }
      });
      $el.data('chart', chart);
    }
  });

  function countArray(arr) {
    var count = {};
    for (var i = 0; i < arr.length; i++) {
      var key = arr[i];
      if (!count[key]) {
        count[key] = 1;
      } else {
        count[key]++;
      }
    }
    var result = [];
    for (var prop in count) {
      result.push({name: prop, count: count[prop]});
    }
    return result;
  }

  $('.add-chart').click('click',function() {
    var attribute_name = $(this).text().trim() // Replace with desired attribute name
    var $existingChart = $('.drop-item canvas[data-attribute="' + attribute_name + '"]');
    if ($existingChart.length) {
      // Chart already exists, update its data
      var chart = $existingChart.data('chart');
      var newData = [];
      for (var i = 0; i < 7; i++) {
        newData.push(Math.floor(Math.random() * 100));
      }
      var existingDataset = chart.data.datasets.find(function(dataset) {
        return dataset.label === attribute_name;
      });
      if (existingDataset) {
        // Dataset already exists, update its data
        existingDataset.data = newData;
      } else {
        // Add new dataset with its own y-axis scale
        var maxScale = Math.max.apply(Math, chart.data.datasets.map(function(dataset) {
          return Math.max.apply(Math, dataset.data);
        }));
        var newScale = maxScale + 20; // Add 20 to max value for new scale
        chart.options.scales.yAxes.push({
          id: attribute_name,
          position: 'right',
          ticks: {
            beginAtZero: true,
            suggestedMax: newScale
          }
        });
        chart.data.datasets.push({
          label: attribute_name,
          data: newData,
          borderWidth: 1,
          yAxisID: attribute_name // Use attribute name as ID for new y-axis scale
        });
      }
      chart.update();
    } else {
      // Chart doesn't exist, create a new one with a single dataset
      var $el = $('<canvas class="drop-item"></canvas>').attr('data-attribute', attribute_name);
      console.log("atribute name : ",window[attribute_name],attribute_name)
      $el.append($('<button type="button" class="btn btn-default btn-xs remove"><span class="fa-solid fa-trash text-white "></span></button>').click(function () { $(this).parent().detach(); }));
      $('#dropzone').append($el);

      // Generate random data for the chart
      var data = [];
      for (var i = 0; i < 7; i++) {
        data.push(Math.floor(Math.random() * 100));
      }

      // Create the chart with a single dataset
      var ctx = $el[0].getContext('2d');
      var chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
          datasets: [{
            label: attribute_name,
            data: window[attribute_name],
            borderWidth: 1,
            borderColor: '#d92136',
            yAxisID: attribute_name // Use attribute name as ID for y-axis scale
          }]
        },
        options: {
          scales: {
            yAxes: [{
              id: attribute_name,
              position: 'right',
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });
      $el.data('chart', chart);
    }
  });

  $('.drag').draggable({
    appendTo: 'body',
    helper: 'clone'
  });

  $('#dropzone').droppable({
    activeClass: 'active',
    hoverClass: 'hover',
    accept: ":not(.ui-sortable-helper)", 
    drop: function (e, ui) {
      var attribute_name = ui.draggable.text();
      var $existingChart = $('.drop-item canvas[data-attribute="' + attribute_name + '"]');
      if ($existingChart.length) {
        // Chart already exists, remove the canvas and create a new chart
        var chart = $existingChart.data('chart');
        chart.destroy();
        $existingChart.parent().remove();
      }
    
      // Create the chart with a single dataset
      var $el = $('<div class="drop-item"></div>');
      $el.append($('<canvas></canvas>').attr('data-attribute', attribute_name));
      $el.append($('<button type="button" class="btn btn-default btn-xs remove"><span class="fa-solid fa-trash text-white"></span></button>').click(function () { 
        var $parent = $(this).parent();
        var chart = $parent.find('canvas').data('chart');
        chart.destroy();
        $parent.remove(); 
      }));
      $(this).append($el);

      // Generate random data for the chart
      var data = [];
      for (var i = 0; i < 7; i++) {
        data.push(Math.floor(Math.random() * 100));
      }

      // Create the chart with a single dataset
      var ctx = $el.find('canvas')[0].getContext('2d');
      var chart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
          datasets: [{
            label: attribute_name,
            data: window[attribute_name],
            borderWidth: 1,
            borderColor: '#d92136',
            yAxisID: attribute_name // Use attribute name as ID for y-axis scale
          }]
        },
        options: {
          scales: {
            yAxes: [{
              id: attribute_name,
              position: 'right',
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });
      $el.find('canvas').data('chart', chart);
      // Show success message
      var $successToast = $('<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">\
        <div class="toast-header">\
          <strong class="mr-auto">Success</strong>\
          <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">\
            <span aria-hidden="true">&times;</span>\
          </button>\
        </div>\
        <div class="toast-body">Chart added successfully!</div>\
      </div>');

      $('body').append($successToast);
      $successToast.toast({
        autohide: true,
        delay: 2000,
        animation: true,
        position: 'top-right'
      });

      $successToast.toast('show');
    }
    }).sortable({
      items: '.drop-item',
      sort: function () {
        $(this).removeClass("active");
      }
    });

    $(document).ready(function() {
        console.log("Cool")
        setXAxisLabels(['Nands', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']);
      });

      function setXAxisLabels(labels) {
        console.log("Cool1")
        $('.drop-item ').each(function() {
          console.log("Cool2")
          var chart = $(this).data('chart');
          if (chart) {
            chart.data.labels = labels;
            chart.update();
          }
        });
      }

function showAlert() {
var alertElement = document.getElementById("myAlert");
alertElement.style.display = "block";
setTimeout(function() {
    alertElement.style.display = "none";
}, 5000);
}
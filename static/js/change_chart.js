console.log("Change_chart.js is called! ")


function bar(ty) {
    console.log("bar clicked ")
    $('.drop-item ').each(function() {
      var chart = $(this).data('chart');
      if (chart) {
        chart.config.type = ty;
        chart.update();
      }
    });
}

function color(ty) {
  console.log("color changed ")
  $('.drop-item ').each(function() {
    var chart = $(this).data('chart');
    if (chart) {
      chart.config.type = ty;
      chart.data.datasets.forEach(function(dataset) {
        dataset.backgroundColor = ty; // Change the background color of each dataset to green
      });
      chart.update();
    }
  });
}


function showAlert() {
  var alertElement = document.getElementById("myAlert");
  alertElement.classList.add("animate__animated", "animate__fadeInRight");
  console.log("animattion added")
  alertElement.style.display = "block";
  setTimeout(function() {
    alertElement.classList.remove("animate__fadeInRight");
    alertElement.classList.add("animate__fadeOutRight");
    setTimeout(function() {
      alertElement.style.display = "none";
      alertElement.classList.remove("animate__fadeOutRight");
    }, 1000);
  }, 5000);
}


// table creation
$(document).ready(function() {
    // initial state is content
    var isTableVisible = false;
    
    $("#add-table").click(function(event) {
      event.preventDefault();
      
      // check if table is visible
      if (isTableVisible) {
        // if it is, remove the table and show the original content
        $("#dropzone table").remove();
        $("#dropzone").text("Some content here");
        isTableVisible = false;
      } else {
        // if it isn't, create the table and hide the original content
        var table = $("<table>").addClass("table table-striped table-bordered table-hover");
        var headers = $("<thead><tr><th class='text-white'>ID</th><th class='text-white'>Name</th><th class='text-white'>Email</th></tr></thead>");
        var rows = $("<tbody><tr><td class='text-white'>1</td><td class='text-white'>John Doe</td><td class='text-white'>johndoe@example.com</td></tr><tr><td>2</td><td>Jane Doe</td><td>janedoe@example.com</td></tr></tbody>");
        table.append(headers).append(rows);
  
        $("#dropzone").html(table);
        isTableVisible = true;
      }
    });
});

$(document).ready(function() {
console.log("Cool")
setXAxisLabels(['Nands', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']);
});

function setXAxisLabels(labels) {
$('.drop-item ').each(function() {
    var chart = $(this).data('chart');
    if (chart) {
    chart.data.labels = labels;
    chart.update();
    }
});
};
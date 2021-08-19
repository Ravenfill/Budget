  // форма отплаты    
  var form = document.getElementById("form-add")
  form.hidden = true; 

  // Отркывает форму с выбором хрени которую нужно добавить в таблицу
  function open_form(){
    form.hidden = false;
    document.getElementById("open_button").hidden = true;
  }

  // Тут та же хрень ток закрывает форму
  function close_form(){
    form.hidden = true;
    document.getElementById("open_button").hidden = false;
  }


  // диаграмма

  google.load("visualization", "1", {packages:["corechart"]});
  google.setOnLoadCallback(drawChart);
  function drawChart() {
   var data = google.visualization.arrayToDataTable([
    ['Категория', 'Процент затрат'],
    ['Продукты',     78.09],
    ['Развлечения', 20.95],
   ]);
   var options = {
    title: 'Расходы',
    is3D: false,
    pieResidueSliceLabel: 'Остальное'
   };
   var chart = new google.visualization.PieChart(document.getElementById('air'));
    chart.draw(data, options);
  }

function getBHK() {
  var bhk = document.getElementsByName("uiBHK");
  for (var i in bhk) {
    if(bhk[i].checked) {
      return parseInt(i)+1
    }
  }
  return -1 // invalid number
}

function getBath() {
  var bath = document.getElementsByName("uiBath");
  for (var i in bath) {
    if(bath[i].checked) {
      return parseInt(i)+1
    }
  }
  return -1 // invalid number
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked")
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHK();
  var bath = getBath();
  var location = document.getElementById("uilocations");
  var price = document.getElementById("uiEstimatedPrice")

  var url = "http://127.0.0.1:5000/predict_house_price";

  // call using jquery post calls
  $.post(url, {
    total_sqft: parseFloat(sqft.value),
    bhk: bhk,
    bath: bath,
    location: location.value

  }, function (data,status) {
    console.log(data.estimated_price);
    price.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakhs </h2>";
    console.log(status)
  });


}

function onPageLoad() {
  console.log("document Loaded");
  var url = "http://127.0.0.1:5000/get_location_names";
  $.get(url, function(data,status) {
    console.log("get reponse for get_location_names");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uilocations");
      $("#uilocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i])
        $("#uilocations").append(opt)
      }
    }
  });
}

 window.onload = onPageLoad;

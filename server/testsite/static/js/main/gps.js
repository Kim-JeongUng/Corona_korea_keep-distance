var gps_result;
function get_geo(){
    if(!!navigator.geolocation){
        navigator.geolocation.getCurrentPosition(successCallback,errorCallback);
    }
    else{
        alert("위치 확인 불가");
    }
}
function successCallback(position){
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    var url = "gps/"+lng+"/"+lat;
    var result = $.get(url, function(data){
        document.getElementById("location").innerHTML = data;
        gps_result = data;
        });
}
function errorCallback(){
                alert("error");
}
get_geo();
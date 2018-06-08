function showCity(){
    var city = document.getElementById("city").value;
    var url = 'http://0.0.0.0:8000/app/city?city_name='+city;
    window.location.replace(url);
}
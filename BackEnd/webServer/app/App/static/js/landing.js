function showCity(){
    var city = document.getElementById("city").value;
    var url = city_url+ '?city_name=' + city;
    window.location.replace(url);
}

function writing(){
    window.location.replace(writerUrl);
}

function login(){
    window.location.replace(loginUrl);
}
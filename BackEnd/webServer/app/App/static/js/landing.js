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

function validateCity(){
    // Validate city name
    var cityName = document.getElementById('city').value;
    if (!cityName) {
        alert('Please enter city name');
        return false;
    }
    cityfqcn = cityName;
    if (cityfqcn) {
        jQuery.getJSON(
                "http://gd.geobytes.com/GetCityDetails?callback=?&fqcn="+cityfqcn,
                function (data) {
                    if (data.geobytescityid>0) {
                        showCity();
                    }
                    else alert('Please select city from drop down menu')
                }
            );
    }
}

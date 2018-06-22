function showCity(){
    var city = document.getElementById("city").value;
    var url = cityUrl + '?city_name=' + city;
    window.location.replace(url);
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

function writeStory(){
    var city_name = document.getElementById('city').value;
    window.location.assign(writeUrl+'?city_name='+city_name);
}

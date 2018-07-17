function login(){
    window.location.assign(loginUrl);
}

function finished(){
    // Submit the final information
    var formData = new FormData();
    var url = uploadArticleUrl;
    var comment = document.getElementById('comment').value;
    formData.append('comment', comment);
    // // Append lat/lng data
    // formData.append('latitude', latitude)
    // formData.append('longitude', longitude)
    var xhr = new XMLHttpRequest({mozSystem: true});
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('finishText').innerHTML = 'Comment success!';
            document.getElementById('finish').disabled = false;
            response = JSON.parse(this.responseText);
            story_id = response.story_id;
            }
        }
    xhr.open('POST', url);
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    xhr.send(formData);
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
  }
checklogin()
function login(){
    window.location.replace(loginUrl);
}

function home(){
    window.location.replace(landingUrl);
}

function about(){
    window.location.replace(aboutUrl);
}

function contact(){
    window.location.replace(contactUrl);
}

function writer(){
    window.location.replace(writeUrl);
}

function checklogin(){
    if (logstatus == "True"){
        document.getElementById("writercenter").disable = false;
        document.getElementById("signin").hidden = true;
        document.getElementById("signup").hidden = true;
    }
}
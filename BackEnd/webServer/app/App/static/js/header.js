function login(){
    window.location.assign(loginUrl);
}

function loginRedirect(next){
    window.location.assign(loginUrl+'?next='+ next);
}

function logout(){
    window.location.assign(logoutUrl);
}

function signup(){
    window.location.assign(signupUrl);
}

function home(){
    window.location.assign(landingUrl);
}

function about(){
    window.location.assign(aboutUrl);
}

function contact(){
    window.location.replace(contactUrl);
}

function writer(){
    window.location.assign(writeUrl);
}

function discovery(){
    window.location.assign(discoverUrl);
}

function jump(url){
    window.location.assign(url);
}

function profile(){
    window.location.assign(userURL);
}

// // When the user scrolls the page, execute myFunction
// window.onscroll = function() {myFunction()};

// // Get the header
// var header = document.getElementById("myHeader");

// // Get the offset position of the navbar
// var sticky = header.offsetTop;

// // Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
// function myFunction() {
//   if (window.pageYOffset > sticky) {
//     header.classList.add("sticky");
//   } else {
//     header.classList.remove("sticky");
//   }
// } 
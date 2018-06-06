function loginForm(){
    setLoginTrue(true);
    document.getElementById("loginSignupForm").innerHTML='\
        <div class="form-group">\
        <label for="username"> username </label>\
        <input type="text" class="form-control" id="username" placeholder="username">\
        </div>\
        \
        <div class="form-group">\
        <label for="password">password</label>\
        <input type="password" class="form-control" id="password" placeholder="password">\
        </div>\
        \
        <button class="btn btn-primary" type="submit">Login</button>';
}


function signupForm(){
    setLoginTrue(false);
    document.getElementById("loginSignupForm").innerHTML='\
        <div class="form-group">\
            <label for="username">username</label>\
            <input type="text" class="form-control" id="username" placeholder="username">\
        </div>\
        \
        <div class="form-group">\
        <label for="password">password</label>\
        <input type="password" class="form-control" id="password" placeholder="password">\
        </div>\
        \
        <div class="form-group">\
            <label for="password">password again</label>\
            <input type="password" class="form-control" id="password-again" placeholder="password">\
        </div>\
        \
        <button class="btn btn-primary" type="submit">sign up</button>';
}

function setLoginTrue(isLogin)
{
    if (isLogin)
    {
        document.getElementById('navBar').innerHTML = '\
            <ul class="nav nav-tabs">\
            <li class="nav-item">\
                <a class="nav-link active"> Login </a>\
            </li>\
            <li class="nav-item">\
                <a class="nav-link" href="#" onclick="javascripts:signupForm();"> Signup </a>\
            </li>\
            </ul>'
    }

    else{

        document.getElementById('navBar').innerHTML = '\
            <ul class="nav nav-tabs">\
            <li class="nav-item">\
                <a class="nav-link" href="#" onclick="javascripts:loginForm();"> Login </a>\
            </li>\
            <li class="nav-item">\
                <a class="nav-link" active > Signup </a>\
            </li>\
            </ul>'

    }
}
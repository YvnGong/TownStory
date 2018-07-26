function login(){
    window.location.assign(loginUrl);
}

// function upload(){
//     var formData = new FormData();
//     var url = commentUrl;
//     var comment = document.getElementById('comment').value;
//     formData.append('story_id', story_id);
//     formData.append('comment', comment);
//     var xhr = new XMLHttpRequest({mozSystem: true});
//     xhr.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             response = JSON.parse(this.responseText);
//             // redirect();
//             time = response.time;
//             time = time.substring(0, 19)
//             update(username, comment, time);
//             }
//         }
//     xhr.open('POST', url);
//     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//     xhr.send(formData);
// }

// function getCookie(cname) {
//     var name = cname + "=";
//     var decodedCookie = decodeURIComponent(document.cookie);
//     var ca = decodedCookie.split(';');
//     for(var i = 0; i <ca.length; i++) {
//         var c = ca[i];
//         while (c.charAt(0) == ' ') {
//             c = c.substring(1);
//         }
//         if (c.indexOf(name) == 0) {
//             return c.substring(name.length, c.length);
//         }
//     }
//     return "";
//   }

// function addcomment(){
//     var content = document.getElementById('comment');
//     if(content.value.length < 1){
//         document.getElementById('commentWarning').hidden = false;
//         return false;
//     }
//     else{
//         upload();
//     }
// }

// function redirect(){
//     var url = storyUrl + '?story_id=' + story_id;
//     window.location.reload(true);
// }

// function update(username, content, comment_time){
//     var text = `<li>
//     <div class="username"><strong>` + username + `</strong></div>
//     <span class="date sub-text">`+comment_time+`</span>
//     <div class="commentText">
// 	<p class="">`+content+`</p> 
// 	</div>
// 	<hr>
//     </li>`
//     document.getElementById('commentDisplay').insertAdjacentHTML('afterbegin', text);
// }
'use strict';

const e = React.createElement; 



class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    var heart;
    if (!isLogged){heart = <i className="far fa-heart fa-2x"></i>;}
    else{
      if (isLiked){
        heart = <i className="fas fa-heart fa-2x"></i>;
      } else{
        heart = <a onClick={likeStory}><i className="far fa-heart fa-2x"></i></a>;
      }
    }
    return(<div>{heart} {number_of_like}</div>);
  }
}

function likeStory(){
  var formData = new FormData();
      formData.append('story_id', story_id);
      var xhr = new XMLHttpRequest({mozSystem: true});
      xhr.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
              isLiked = true;
              number_of_like += 1;
              ReactDOM.render(<LikeButton />, document.getElementById('likeButton'));
            }
          }
      xhr.open('POST', likeUrl);
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



// const domContainer = document.querySelector('#like_button_container');
// ReactDOM.render(e(LikeButton), domContainer);
ReactDOM.render(<LikeButton />, document.getElementById('likeButton'));
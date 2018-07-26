'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    var heart;
    var style = { color: '#ce2424' };
    if (!isLogged) {
      heart = React.createElement('i', { className: 'far fa-heart fa-2x' });
    } else {
      if (isLiked) {
        heart = React.createElement('i', { className: 'fas fa-heart fa-2x' });
      } else {
        heart = React.createElement(
          'a',
          { href: '#/', onClick: likeStory, style: style },
          React.createElement('i', { className: 'far fa-heart fa-2x' })
        );
      }
    }
    return React.createElement(
      'div',
      null,
      heart,
      ' ',
      number_of_like
    );
  }
}

function likeStory() {
  var formData = new FormData();
  formData.append('story_id', story_id);
  var xhr = new XMLHttpRequest({ mozSystem: true });
  xhr.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      isLiked = true;
      number_of_like += 1;
      ReactDOM.render(React.createElement(LikeButton, null), document.getElementById('likeButton'));
    }
  };
  xhr.open('POST', likeUrl);
  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
  xhr.send(formData);
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for (var i = 0; i < ca.length; i++) {
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

ReactDOM.render(React.createElement(LikeButton, null), document.getElementById('likeButton'));
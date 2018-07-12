// import 'css/fontawesome.css'; 
'use strict';

const e = React.createElement;


class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    // const element = (<button class="btn btn-light btn-md">like me!</button>);
    if (this.state.liked) {
      //  return element;
      // Submit the final information
      var formData = new FormData();
      formData.append('story_id', story_id);
      var xhr = new XMLHttpRequest({mozSystem: true});
      xhr.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
              return '♥ liked';
            }
          }
      xhr.open('POST', url);
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      xhr.send(formData);
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      '♡ like',
    );
  }
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);
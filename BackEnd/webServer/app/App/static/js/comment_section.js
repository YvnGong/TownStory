var runNum = 5;
var showmore_button = <a href='#/' onClick={showMore}>show more comments</a>



function formatDate(date) {
    return date.substring(0, 19);
}

function showMore(){
    var maxNum = commentList.length;
    runNum = Math.min(runNum+6, maxNum);
    if (runNum >= maxNum){
        showmore_button = <a href="#/" hidden>show more</a>
    } 
    ReactDOM.render(
        <Comment />,
        document.getElementById('comment_section')
        );

}

// function showMore(shownum, index){
//     var length = commentList.length;
//     if(length-shownum>=5){
//         const comments = commentList.slice(index, index+shownum);
//         const listItems = comments.map((comment) =>
//         <li><SingleComment username = {comment.user} 
//         comment_time = {comment.comment_time} content = {comment.content}/></li>
//         );
//     }
//     else{
//         const comments = commentList.slice(index);
//         const listItems = comments.map((comment) =>
//         <li><SingleComment username = {comment.user} 
//         comment_time = {comment.comment_time} content = {comment.content}/></li>
//         /////////disable show more button from here/////////
//         );
//     }
//     return listItems;
// }

class SingleComment extends React.Component {
    constructor(props) {
        super(props);
    }
    render(){
    return(
        <div>
        <div className="username"><strong>{this.props.username}</strong></div>
        <span className="date sub-text">{formatDate(this.props.comment_time)}</span>
        <div className="commentText"><p className="">{this.props.content}</p></div>
        <hr />
        </div>
    );
    }
}


class Comment extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        var submit_button = <button type="button" className="btn btn-default btn-md" onClick={addcomment}>Add Comment</button>

        var numberOfComments = commentList.length;
        if(commentList.length > 0){
            var comments = commentList.slice(0, runNum);
            var listItems = comments.map((comment) =>
            <li><SingleComment username = {comment.user} 
            comment_time = {comment.comment_time} content = {comment.content}/></li>
            );
            return(
            <div>
                <div className="titleBox">
                    <label><h4>{numberOfComments} Comment</h4></label>
                    <div>
                    <ul>
                    {listItems}
                    </ul>        
                    </div>
                    {showmore_button}

                    <form className="form" role="form">
				        <div className="form-group">
					        <span id='commentWarning' className="error text-danger" hidden>You didn't enter any content here :( </span>
                            <span id='loginWarning' className="error text-danger" hidden>Please log in first to leave a comment :) </span>
					        <input className="form-control" type="text" size="45" id="comment" placeholder="Your comments" />
				        </div>
				        <div className="form-group">
                            {submit_button}
				        </div>
			        </form>
                </div>
            </div>
                );
        }
        else{
            return(
                <div>
                <div className="titleBox">
                    <label><h4>{numberOfComments} Comment</h4></label>
                    <p>Do you want to leave first comment here? </p>
                    <form className="form" role="form">
				        <div className="form-group">
					        <span id='commentWarning' className="error text-danger" hidden>You didn't enter any content here :(</span>
                            <span id='loginWarning' className="error text-danger" hidden>Please log in to leave a comment :) </span>
                            <input className="form-control" type="text" size="45" id="comment" placeholder="Your comments" />
				        </div>
				        <div className="form-group">
                            {submit_button}
				        </div>
			        </form>
                </div>
                </div>
                
            )
        }
    }
}



function upload(){
    var formData = new FormData();
    var url = commentUrl;
    var comment = document.getElementById('comment').value;
    formData.append('story_id', story_id);
    formData.append('comment', comment);
    var xhr = new XMLHttpRequest({mozSystem: true});
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(this.responseText);
            var time = response.time;
            time = time.substring(0, 19);
            requestComment();
            document.getElementById('comment').value = '';
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


function addcomment(){
    var content = document.getElementById('comment');
    if (!isLogged){
        document.getElementById('loginWarning').hidden = false;  
        return false;
    }
    else if(content.value.length < 1){
        document.getElementById('commentWarning').hidden = false;  
        return false;
    }
    else{
        // this.props.commentList.push(content);
        upload();
    }
}

let commentList;
function requestComment(){
    var xhr = new XMLHttpRequest();
    var requestURL = commentUrl + '?story_id=' + story_id;
    xhr.onreadystatechange = function() {
        // console.log(this.readyState);
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            commentList = response.commentList;
            // console.log(commentList)
            ReactDOM.render(
                <Comment />,
                document.getElementById('comment_section')
            );
        }
      };
    xhr.open('GET', requestURL);
    xhr.send();
}

requestComment();

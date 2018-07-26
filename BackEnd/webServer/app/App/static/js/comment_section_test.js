var runNum = 5;

function formatDate(date) {
    return date.substring(0, 19);
}

function showMore() {
    var maxNum = commentList.length;
    runNum += Math.min(runNum, maxNum);
    ReactDOM.render(React.createElement(Comment, null), document.getElementById('comment_section'));
}


class SingleComment extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return React.createElement(
            "div",
            null,
            React.createElement(
                "div",
                { className: "username" },
                React.createElement(
                    "strong",
                    null,
                    this.props.username
                )
            ),
            React.createElement(
                "span",
                { className: "date sub-text" },
                formatDate(this.props.comment_time)
            ),
            React.createElement(
                "div",
                { className: "commentText" },
                React.createElement(
                    "p",
                    { className: "" },
                    this.props.content
                )
            ),
            React.createElement("hr", null)
        );
    }
}

class Comment extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        var submit_button = React.createElement(
            "button",
            { type: "button", className: "btn btn-default", onClick: addcomment },
            "Add"
        );
        var showmore_button = React.createElement(
            "a",
            { href: "#/", onClick: showMore },
            "show more comments"
        );
        if (commentList.length > 0) {
            var comments = commentList.slice(0, runNum);
            var listItems = comments.map(comment => React.createElement(
                "li",
                null,
                React.createElement(SingleComment, { username: comment.user,
                    comment_time: comment.comment_time, content: comment.content })
            ));
            return React.createElement(
                "div",
                null,
                React.createElement(
                    "div",
                    { className: "titleBox" },
                    React.createElement(
                        "label",
                        null,
                        "Comment"
                    )
                ),
                React.createElement(
                    "div",
                    null,
                    React.createElement(
                        "ul",
                        null,
                        listItems
                    )
                ),
                showmore_button,
                React.createElement(
                    "form",
                    { className: "form-inline", role: "form" },
                    React.createElement(
                        "div",
                        { className: "form-group" },
                        React.createElement(
                            "span",
                            { id: "commentWarning", className: "error text-danger", hidden: true },
                            "You didn't enter any content here :("
                        ),
                        React.createElement("input", { className: "form-control", type: "text", size: "45", id: "comment", placeholder: "Your comments" })
                    ),
                    React.createElement(
                        "div",
                        { className: "form-group" },
                        submit_button
                    )
                )
            );
        } else {
            return;
            React.createElement(
                "p",
                null,
                "Do you want to leave first comment here? "
            );
        }
    }
}

function upload() {
    var formData = new FormData();
    var url = commentUrl;
    var comment = document.getElementById('comment').value;
    formData.append('story_id', story_id);
    formData.append('comment', comment);
    var xhr = new XMLHttpRequest({ mozSystem: true });
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(this.responseText);
            var time = response.time;
            time = time.substring(0, 19);
            requestComment();
            document.getElementById('comment').value = '';
        }
    };
    xhr.open('POST', url);
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

function addcomment() {
    var content = document.getElementById('comment');
    if (content.value.length < 1) {
        document.getElementById('commentWarning').hidden = false;
        return false;
    } else {
        // this.props.commentList.push(content);
        upload();
    }
}

let commentList;
function requestComment() {
    var xhr = new XMLHttpRequest();
    var requestURL = commentUrl + '?story_id=' + story_id;
    xhr.onreadystatechange = function () {
        // console.log(this.readyState);
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            commentList = response.commentList;
            // console.log(commentList)
            ReactDOM.render(React.createElement(Comment, null), document.getElementById('comment_section'));
        }
    };
    xhr.open('GET', requestURL);
    xhr.send();
}

requestComment();
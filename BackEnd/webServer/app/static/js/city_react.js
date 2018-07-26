// import React from 'react';

var storyCap = 6;

function showMore(){
    var maxCap = storyList.length;
    storyCap = (Math.min(storyCap+6, maxCap));
    ReactDOM.render(
        <Stories />,
        document.getElementById('storyBox')
        );

}

class Story extends React.Component{
    constructor(props) {
        super(props);
    }
    render(){
        return (
            <div className="col-lg-4">
            <div className="card" style={{width: '20rem', height: '90%'}}>
                  <img className="card-img-top" src={this.props.cover} alt="Card image cap" style={{height: '50%'}} />
                  <div className="card-body">
                    <h5 className="card-title">{this.props.title}</h5>
                    <p className="card-text">{this.props.summary}</p>
                    <a href={storyUrl + '?story_id=' + this.props.story_id} className="btn btn-primary">Read</a>
                </div>
            </div>
            </div>
        )
    }

}

class Stories extends React.Component{
    constructor(props) {
        super(props);
    }
    render() {
        var showmore_button = <a href='#/' onClick={showMore}>show more stories</a>
        if (storyCap >= storyList.length){
            var showmore_button = <a href='#/' hidden>show more stories</a>
        }
        console.log(storyList.length)
        if(storyList.length > 0){
            var stories = storyList.slice(0, storyCap);
            var listItems = stories.map((story) =>
            <Story key={Math.random()} cover = {story.fields.cover} 
            title = {story.fields.title} summary = {story.fields.summary} story_id = {story.pk} />
            );
            return(
            <div>
            <div className="row">
                {listItems}
            </div>
            <div className="row align-items-center justify-content-md-center">
            {showmore_button}
            </div>
            </div>
                );
        }
        else{
            console.log('yes')
            return(
            <div className="container">
            <div className="row">
                <div className="col-lg-12">
                    <br />
                    <h4>This city has no story yet. Wanna start the first one? ^_^</h4>
                    <br />
                    <button className="btn btn-primary btn-lg" onClick={redirectWrite}>Start to Write</button>
                </div>
            </div>
            </div>
            )
        }
    }
}

function redirectWrite(){
    var url = writeUrl + '?city_name=' + city_name;
    jump(url);
}

let storyList;
function requestStories(){
    var xhr = new XMLHttpRequest();
    var requestURL = storyListUrl + '?city_name=' + city_name;
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            if (response.status == false && response.errorMessage=='nostory'){
                storyList = [];
            }
            else{
                storyList = JSON.parse(response.storyList);
            }
            //
            console.log(storyList[0]);
            ReactDOM.render(
                <Stories />,
                document.getElementById('storyBox')
            );
        }
      };
    xhr.open('GET', requestURL);
    xhr.send();
}

requestStories();
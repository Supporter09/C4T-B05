let delete_click =  document.getElementById("song_container").getElementsByClassName("delete");
console.log(delete_click);
for (i=0;i<delete_click.length;i++) {
    delete_button = delete_click[i];
    delete_button.addEventListener('click', function(e) {
        var btn = e.target;
        btn.parentNode.remove();
    })
    
}

let song_div = document.getElementById("song_container");
console.log(song_div);

let song_class = document.getElementsByClassName("song");
console.log(song_class);

let title = document.getElementsByClassName('title');
let artist = document.getElementsByClassName('artist');
console.log(title);
console.log(artist);
for (i=0; i<song_class.length;i++) {
    console.log(title[i])
    console.log(artist[i])
}

let box = document.getElementById("box");
console.log(box);
console.log("Height Box :"+ box.clientHeight);
console.log("Width Box :"+ box.clientWidth);
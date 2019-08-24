let delete_click =  document.getElementById("song_container").getElementsByClassName("delete");//Delete Button
console.log(delete_click);
for (i=0;i<delete_click.length;i++) {
    delete_button = delete_click[i];
    delete_button.addEventListener('click', function(e) {
        var btn = e.target;
        btn.parentNode.remove();
    })
    
}

let song_div = document.getElementById("song_container");// print song_container
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

// let edit_button = document.getElementsByClassName('edit')
// let edit_btn_attr = document.getElementsByClassName('edit').getAttribute('song_id')
// console.log(edit_btn_attr)
// console.log(edit_button);
// for (i=0;i<edit_button.length;i++) {
//     edit_btn = edit_button[i];
//     edit_btn.addEventListener('click', function(e) {
//         var btn = e.target;
//         edit_parent=btn.parentNode;
//         console.log(edit_parent);
//         // console.log(edit_parent.getElementById(""))
//     })
    
// }
for(let i = 0; i < song_class.length; i++){
    song_class[i].getElementsByClassName('edit')[0].addEventListener('click', function(){
        console.log(document.getElementsByClassName('song')[i].getAttribute('song_id'));
        let song_id_value = document.getElementsByClassName('song')[i].getAttribute('song_id');

    })
}


let more_button = document.getElementsByClassName('more')
console.log(more_button);
for (let i=0;i<more_button.length;i++) {
    more_btn = more_button[i];
    more_btn.addEventListener('click', function(e) {
        var btn = e.target;
        more_parent=btn.parentNode;
        let song = more_parent.getElementsByClassName("song");
        let artist = more_parent.getElementsByClassName("artist")[0].innerHTML;
        let song_id = document.getElementsByClassName('song')[i].getAttribute('song_id');
        console.log(song);
        console.log(artist);
        console.log(song_id);
        // console.log(edit_parent.getElementById(""))
    })
    
}

let add_button = document.getElementById('add');
add_button.addEventListener('click', function(){
    new1 = document.createElement('div');
    new2 = document.createElement('h4');
    new3 = document.createElement('h5');
    new4 = document.createElement('button')
    new5 = document.createElement('button')
    new6 = document.createElement('button')
    new4.innerHTML = "Delete";
    new5.innerHTML = "Edit";
    new6.innerHTML = "More";
    add_button.appendChild(new1)
    new1.appendChild(new2);
    new1.appendChild(new3)
    new1.appendChild(new4)
    new1.appendChild(new5)
    new1.appendChild(new6)

})

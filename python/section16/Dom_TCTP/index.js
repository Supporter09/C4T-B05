let delete_click =  document.getElementById("song_container").getElementsByClassName("delete");
console.log(delete_click);
for (i=0;i<delete_click.length;i++) {
    delete_button = delete_click[i];
    delete_button.addEventListener('click', function(e) {
        var btn = e.target;
        btn.parentNode.remove();
    })
    
}
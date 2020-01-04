function hideElement(e_id) {
    var x = document.getElementById(e_id);
    var btn = document.getElementById('btn');
    if(x.style.display == "none") {
        x.style.display = "block";
        btn.innerText="Hide Resume";
    }
    else {
        x.style.display = "none";
        btn.innerText="Show Resume";
    }
}
function hideElement(e_id) {
    var x = document.getElementById(e_id);
    if(x.style.display == "none") {
        x.style.display = "block";
    }
    else {
        x.style.display = "none";
    }
}
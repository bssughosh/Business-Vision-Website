$(document).ready(function () {
    var list = document.getElementsByClassName("clicker");
    for (var i = 0; i < list.length; i++) {
        list[i].setAttribute("id", "obj-" + i);
        list[i].setAttribute("name", "obj-" + i);
        list[i].nodeValue = "obj-" + i;
    }


});

$(document).ready(function () {
    var list = document.getElementsByClassName("clicker");
    for (var i = 0; i < list.length; i++) {
        list[i].setAttribute("id", "obj-" + i);
        list[i].setAttribute("name", "obj-" + i);
    }


});

// $(".clicker").click(function () {
//     var pid;
//     pid = $(this).attr("id");
//     // var inp = document.getElementsByName("pid");
//     // $(".inp").text(pid);
//     alert(pid);
//
// });











// $.ajax({
//     type: "POST",
//     url: "/cust/description/",
//     data: {
//         pid: pid,
//         csrfmiddlewaretoken: '{{ csrf_token }}'
//     },
//     headers: {'X-CSRFToken': '{% csrf_token %}'},
//     success: function (data) {
//         alert(data.result);
//     }
// });
$(document).ready(function () {
    $(".login2").click(function () {
        $(".clogin").show();
        $(".slogin").hide();
        $(".login2").addClass('active');
        $(".login1").removeClass('active');
    });


    $(".login1").click(function () {
        $(".slogin").show();
        $(".clogin").hide();
        $(".login1").addClass('active');
        $(".login2").removeClass('active');
    });
});
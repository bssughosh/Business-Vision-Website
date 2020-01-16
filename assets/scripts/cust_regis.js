$(document).ready(function () {
    $('#b1').click(function () {
        var error_email = '';
        var error_name = '';
        var error_mobile = '';
        var mobile_validation = /^\d{10}$/;
        var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

        if ($.trim($('#email').val()).length == 0) {
            error_email = 'Email is required';
            $('#error_email').text(error_email);
            $('#email').addClass('has-error');
        } else {
            if (!filter.test($('#email').val())) {
                error_email = 'Invalid Email';
                $('#error_email').text(error_email);
                $('#email').addClass('has-error');
            } else {
                error_email = '';
                $('#error_email').text(error_email);
                $('#email').removeClass('has-error');
            }
        }


        if ($.trim($('#name').val()).length == 0) {
            error_first_name = 'Name is required';
            $('#error_name').text(error_first_name);
            $('#name').addClass('has-error');
        } else {
            error_name = '';
            $('#error_name').text(error_name);
            $('#name').removeClass('has-error');
        }


        if ($.trim($('#mobile').val()).length == 0) {
            error_mobile = 'Mobile Number is required';
            $('#error_mobile').text(error_mobile);
            $('#mobile').addClass('has-error');
        } else {
            if (!mobile_validation.test($('#mobile').val())) {
                error_mobile = 'Invalid Mobile Number';
                $('#error_mobile').text(error_mobile);
                $('#mobile').addClass('has-error');
            } else {
                error_mobile = '';
                $('#error_mobile').text(error_mobile);
                $('#mobile').removeClass('has-error');
            }
        }


        if (error_email != '' || error_name != '' || error_mobile != '') {
            return false;
        } else {
            $('#p1').removeClass('active active_tab1');
            $('#p1').removeAttr('href data-toggle');
            $('#p1id').removeClass('active');
            $('#p1').addClass('inactive_tab1');
            $('#p2').removeClass('inactive_tab1');
            $('#p2').addClass('active_tab1 active');
            $('#p2').attr('href', '#p2id');
            $('#p2').attr('data-toggle', 'tab');
            $('#p2id').addClass('active in');
        }
    });



    $('#b2').click(function () {

        $('#p2').removeClass('active active_tab1');
        $('#p2').removeAttr('href data-toggle');
        $('#p2id').removeClass('active in');
        $('#p2').addClass('inactive_tab1');
        $('#p1').removeClass('inactive_tab1');
        $('#p1').addClass('active_tab1 active');
        $('#p1').attr('href', '#p1id');
        $('#p1').attr('data-toggle', 'tab');
        $('#p1id').addClass('active in');
    });
});
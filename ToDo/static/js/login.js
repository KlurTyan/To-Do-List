$(document).ready(function () {
    $(".tabs .tab").click(function () {
        if ($(this).hasClass("signin")) {
            $(".tabs .tab").removeClass("active");
            $(this).addClass("active");
            $(".cont").hide();
            $(".signin-cont").show();
        }
        if ($(this).hasClass("signup")) {
            $(".tabs .tab").removeClass("active");
            $(this).addClass("active");
            $(".cont").hide();
            $(".signup-cont").show();
        }
    });

    $(".container .bg").mousemove(function (e) {
        var amountMovedX = (e.pageX * -1) / 30;
        var amountMovedY = (e.pageY * -1) / 9;
        $(this).css(
            "background-position",
            amountMovedX + "px " + amountMovedY + "px"
        );
    });

    $("#login_btn").click(function () {
        $.ajax({
            url: "http://localhost:8000/token/",
            crossDomain: true,
            method: "POST",
            data: JSON.stringify({
                login: $("#login").val(),
                password: $("#pass").val(),
            }),
            headers: {
                accept: "application/json",
            },
            contentType: "application/json"
        }).done(function(resp){
            localStorage.setItem('access_token', resp['access'])
            window.location.href = 'http://localhost:8000/'
        }).fail(function(msg){
            console.log(msg)
        });
    });

    $("#sign_up_btn").click(function () {
        $.ajax({
            url: "http://localhost:8000/user/register/",
            crossDomain: true,
            method: "POST",
            data: JSON.stringify({
                "login": $('#name').val(),
                "password": $('#pass-sign').val(),
                "email": $('#email').val() 
              }),
            headers: {
                accept: "application/json",
            },
            contentType: "application/json"
        }).done(function(resp){
            console.log(resp)
        }).fail(function(){
            alert('Пользователь с таким Логин уже существует!')
            window.location.href = 'http://localhost:8000/login/'
        });;
    });
});

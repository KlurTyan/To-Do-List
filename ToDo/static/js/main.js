$(document).ready(function () {
    if (window.localStorage.getItem("access_token") == null) {
        window.location.href = "http://localhost:8000/login";
    }


    $.ajax({
        url: "http://localhost:8000/user/me",
        headers: {
            Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        },
    }).done(function(data){
        $('.dropbtn').text(data['login'])
    })

    $("#log-out").click(function () {
        localStorage.removeItem("access_token");
    });



    $(".form").submit(function (event) {
            $.ajax({
                url: "http://localhost:8000/api/post/",
                method: "POST",
                headers: {
                    Authorization: `Bearer ${localStorage.getItem(
                        "access_token"
                    )}`,
                },
                data: {
                    text: $(".form-control").val(),
                    done: false,
                    user: 1
                },
            }).done(function(data){
                console.log(data)
            }).fail(function(msg){
                console.log(msg)
            });
    });

    $.ajax({
        url: "http://localhost:8000/api/post/",
        headers: {
            Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        },
    })
        .done(function (data) {
            len = data["results"].length;
            for (let i = 0; i < len; i++) {
                const card = document.createElement("div");
                card.className = "input-group-text";

                const cb = document.createElement("input");
                cb.type = "checkbox";
                cb.name = "checkbox";
                cb.id = "checkbox" + data["results"][i].id;

                const text_label = document.createElement("label");
                text_label.setAttribute(
                    "for",
                    "checkbox" + data["results"][i].id
                );
                text_label.className = "text";
                text_label.id = "c" + data["results"][i].id;
                text_label.innerText = data["results"][i].text;

                const del = document.createElement("a");
                del.id = "del" + data["results"][i].id;

                card.appendChild(cb);
                card.appendChild(text_label);
                card.appendChild(del);

                if (data["results"][i].done == true) {
                    document
                        .getElementById("card-container-completed")
                        .appendChild(card);
                    $(String("#checkbox" + data["results"][i].id)).prop(
                        "checked",
                        true
                    );
                    $(String("#c" + data["results"][i].id)).css(
                        "text-decoration",
                        "line-through"
                    );
                } else {
                    document.getElementById("card-container").appendChild(card);
                    $(String("#c" + data["results"][i].id)).css(
                        "text-decoration",
                        "none"
                    );
                }

                // POST REQUEST

                // DELETE REQUEST

                $("#del" + data["results"][i].id).click(function () {
                    $.ajax({
                        url : `http://localhost:8000/api/post/${data["results"][i].id}/`,
                        method: "DELETE",
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem(
                                "access_token"
                            )}`,
                        },
                    })
                        .done(function () {
                            card.style = "display: none";
                        })
                        .fail(function (msg) {
                            console.log(msg["responseJSON"]["detail"]);
                        });
                });

                // PATCH REQUEST

                $(String("#checkbox" + data["results"][i].id)).click(
                    function () {
                        $.get(
                            `http://localhost:8000/api/post/${data["results"][i].id}/`,
                            async function (data) {
                                console.log(data);
                                if (data.done == false) {
                                    $.ajax({
                                        url: `http://localhost:8000/api/post/${data.id}/`,
                                        method: "PATCH",
                                        data: {
                                            text: data.text,
                                            date: data.date,
                                            done: true,
                                        },
                                    });
                                    $(String("#c" + data.id)).css({
                                        "text-decoration": "line-through",
                                    });
                                    document
                                        .getElementById(
                                            "card-container-completed"
                                        )
                                        .appendChild(card);
                                } else {
                                    $.ajax({
                                        url: `http://localhost:8000/api/post/${data.id}/`,
                                        method: "PATCH",
                                        data: {
                                            text: data.text,
                                            date: data.date,
                                            done: false,
                                        },
                                    });
                                    $(String("#c" + data.id)).css({
                                        "text-decoration": "none",
                                    });
                                    document
                                        .getElementById("card-container")
                                        .appendChild(card);
                                }
                            }
                        );
                    }
                );
                // if (window.localStorage.getItem)
            }
        })
        .fail(function (msg) {
            console.log(msg);
        });
});
``;

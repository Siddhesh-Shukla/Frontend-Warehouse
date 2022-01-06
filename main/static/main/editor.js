$("#HTML").on("input", function (e) {
e.preventDefault();
$.ajax({
    type: "POST",
    url: '{% url "home" %}',
    data: {
    text:
        "<style> " + $("#CSS").val() + " </style> " + $("#HTML").val(),
    csrfmiddlewaretoken: "{{ csrf_token }}",
    dataType: "json",
    },
    success: function (data) {
    $("#output").html(data.msg);
    },
    failure: function () {
    console.log("Failed!");
    },
});
});
$("#CSS").on("input", function (e) {
e.preventDefault();
$.ajax({
    type: "POST",
    url: '{% url "home" %}',
    data: {
    text:
        "<style> " + $("#CSS").val() + " </style> " + $("#HTML").val(),
    csrfmiddlewaretoken: "{{ csrf_token }}",
    dataType: "json",
    },
    success: function (data) {
    $("#output").html(data.msg);
    },
    failure: function () {
    console.log("Failed!");
    },
});
});
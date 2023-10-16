$("#contactForm").submit(function (e) {
  e.preventDefault();

  $("#loading").css("display", "block");

  $.ajax({
    type: "POST",
    url: "/support/contact/",
    data: {
      sender_name: $("#name").val(),
      sender_phone: $("#phone").val(),
      message_subject: $("#subject").val(),
      message_text: $("#message").val(),
      datatype: "json",
      csrfmiddlewaretoken: csrftoken,
    },

    success: function () {
      $("#loading").css("display", "none");
      $("#sent-message").css("display", "block");
      $("#sent-message").delay(3000).fadeOut("slow");
      $("#contactForm")[0].reset();
    },
  });
});

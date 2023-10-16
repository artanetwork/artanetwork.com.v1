$("#newsletterSignupForm").submit(function (e) {
  e.preventDefault();

  $.ajax({
    type: "POST",
    url: "/support/signup/",
    data: {
      user_email: $("#email").val(),
      datatype: "json",
      csrfmiddlewaretoken: csrftoken,
    },

    success: function () {
      $("#signupNewsletter").css("display", "block");
      $("#signupNewsletter").delay(3000).fadeOut("slow");
      $("#newsletterSignupForm")[0].reset();
    },
  });
});

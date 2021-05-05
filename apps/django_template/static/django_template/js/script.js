$(document).ready(function () {
  $('form[id="registration_form"]').validate({
    rules: {
      profile_picture: "required",
      first_name: "required",
      last_name: "required",
      username: "required",
      email: "required",
      password1: "required",
      password2: "required",
      mobile_no: "required",
      description: "required",
    },
    messages: {
      profile_picture: "Upload your Profile Picture:",
      first_name: "Enter your First Name",
      last_name: "Enter your Last Name",
      username: "Choose a unique username",
      email: "Enter your email address",
      password1: "Enter password",
      password2: "Enter password again",
      mobile_no: "Enter your mobile No",
      description: "Enter your job description",
    },
    submitHandler: function (form) {
      form.submit();
    },
  });
});

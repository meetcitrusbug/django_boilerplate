$(document).ready(function () {
    $('form[id="blog-form"]').validate({
      rules: {
        blog_title: "required",
        blog: "required",
        language: "required",
        category: "required",
        image: "required",
        author: "required",
      },
      messages: {
        blog_title: "Please Enter Your Blog title",
        blog: "Please Add Your Content",
        category: "Please select Blog's Category",
        language: "Add Language Of Your Blog",
        image: "Please Add Image",
        author: "Please Add Author",
      },
      submitHandler: function (form) {
        form.submit();
      },
    });
  });
  
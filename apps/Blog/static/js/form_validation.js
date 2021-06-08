$(document).ready(function () {
        var keyword_arr = []
        $('#keyword').keypress(function(event){
          if(event.key === 'Enter'){
              var keyword = $("#keyword").val();
              var csrf_token = $("[name='csrfmiddlewaretoken']").val()
              $("#keyword-list-display").append("<li><a id='keyword-word' href='#'>" + keyword + "<span class='remove-keyword'><i class='fa fa-times'></i></span></a></li>");
              $("#keyword").val("");
              keyword_arr.push(keyword)
              $('#keyword_list').val(keyword_arr)
              console.log(keyword_arr)
          }
          event.stopPropagation();
      });
      $('#keyword-list-display').on("click", " li i ",function(){
        $(this).parent().parent().remove();
      });

      $('#publish_blog').on('click',function(){
        $('#blog_title-error').empty()
        $('#blog-error').empty()
        $('#category-error').empty()
        $('#document-image-error').empty()
        $('#author-error').empty()
        var csrf_token = $("[name='csrfmiddlewaretoken']").val();
        var blog_title = $('#blog_title').val()
        var blog = $('#blog').val()
        var exist_blog = $('#update_blog').val()
        var keyword = $('#keyword_list').val()
        var category = $('#hidden_category').val()
        var author = $('#author').val()
        var document_image = $("#document_image").attr("src");
        if(blog_title=='' || blog_title==null){
          $('#blog_title-error').append('<div class="text-danger">'+ "This field is required" + '</div>')
        }
        if(blog=='' || blog==null){
          $('#blog-error').append('<div class="text-danger">'+ "This field is required" + '</div>')
        }
        if(document_image=='' || document_image==null){
          $('#document-image-error').append('<div class="text-danger">'+ "This field is required" + '</div>')
        }
        if(author=='' || author==null){
          $('#author-error').append('<div class="text-danger">'+ "This field is required" + '</div>')
        }
        else{
          $.ajax({
              url: '/createblog',
              type: 'POST',
              data: {
                  csrfmiddlewaretoken: csrf_token,
                  blog_title:blog_title,
                  blog:blog,
                  exist_blog,exist_blog,
                  'keyword[]':keyword,
                  category:category,
                  author:author,
                  document_image:document_image
              },
              success: function (response) {
                  window.location = 'http://127.0.0.1:8000/'
                  return true;
              }
        })
      }
    })
    $(".custom-file-input").on("change", function () {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
  });
  var readURL = function (input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $(".profile-pic").attr("src", e.target.result);
      };
      reader.readAsDataURL(input.files[0]);
    }
  };
  $(".file-upload").on("change", function () {
    readURL(this);
  });

  $(".upload-button").on("click", function () {
    $(".file-upload").click();
  });
  });
  
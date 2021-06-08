$(document).ready(function(){
    // Blog search function
    $('#search_btn').on('click',function(){
        var blog_content = $('#blog_content').val()
        var category_id = $('#cat_value').val()
        var year = $('#yearselect').val()

        $.ajax({
            url:'/blog-search',
            data: {
                'blog_content': blog_content,
                'category_id':category_id,
                'year':year
            },
            success: function (response) {
              $(".blog-list").html(response)
            },
        });
    })
})
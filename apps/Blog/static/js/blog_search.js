$(document).ready(function(){
    // Blog search function
    $('#search_btn').on('click',function(){
        var blog_content = $('#blog_content').val()

        $.ajax({
            url:'/blog-search',
            data: {
                'blog_content': blog_content,
            },
            success: function (response) {
              $(".blog-list").html(response)
            },
        });
    })

    // Category filter function
    $('#category-Filter').on('change',function(){
        var category = $(this).val()

        $.ajax({
            url:'/blog-search',
            data: {
                'category': category,
            },
            success: function (response) {
              $(".blog-list").html(response)
            },
        });
    })
    $('#month-Filter').on('change',function(){
        var month = $(this).val()

        $.ajax({
            url:'/blog-search',
            data: {
                'month': month,
            },
            success: function (response) {
              $(".blog-list").html(response)
            },
        });
    })
})
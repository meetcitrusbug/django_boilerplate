/*global $ */
'use strict';

var userroles = {

    // ------------------------------------------------------------------------
    // Users
    // ------------------------------------------------------------------------
    users: {

        index: function () {
            $('#user-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'username', name: 'username' },
                    { data: 'name', name: 'name' },
                    // { data: 'mobile', name: 'mobile' },
                    // { data: 'dob', name: 'dob' },
                    { data: 'is_active', name: 'is_active' },
                    { data: 'instructor', name: 'instructor' },
                    { data: 'language', name: 'language' },
                    { data: 'created_at', name: 'created_at' },
                    { data: 'actions', name: 'actions' }
                ],
            });

        },

        details: function () {
            $('.groups-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available groups',
                selectedListLabel: 'Chosen groups',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });

            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------
    // Groups
    // ------------------------------------------------------------------------
    groups: {

        index: function () {
            $('#group-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },]
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },


    // ------------------------------------------------------------------------

    app_contents: {

        index: function () {
            $('#appcontent-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'title', name: 'title' },
                    { data: 'key', name: 'key' },
                    { data: 'description', name: 'description' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------


    genre: {
        index: function () {
            $('#genre-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'title', name: 'title' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------

    artist: {
        index: function () {
            $('#artist-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },


    // ----------------------------------------------------------------

    language: {
        index: function () {
            $('#language-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'title', name: 'title' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    //-------------------------------------------------------------------------
    plan: {
        index: function () {
            $('#plan-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'title', name: 'title' },
                    { data: 'price', name: 'price' },
                    { data: 'duration_month', name: 'duration_month' },
                    { data: 'high', name: 'high' },
                    { data: 'family', name: 'family' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },
    //------------------------------------------------------------------------

    playlist: {
        index: function () {
            $('#playlist-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: [ -1, -2 ]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'is_featured', name: 'is_featured' },
                    { data: 'likes', name: 'likes' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    //------------------------------------------------------------------------
    song: {
        index: function () {
            $('#song-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: [ -1, -2 ]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'artist', name: 'artist' },
                    { data: 'genre', name: 'genre' },
                    { data: 'language', name: 'language' },
                    { data: 'duration', name: 'duration' },
                    { data: 'likes', name: 'likes' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },
    //------------------------------------------------------------------------

    channel: {
        index: function () {
            $('#channel-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: [ -1, -2, -3 ]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'category', name: 'category' },
                    { data: 'likes', name: 'likes' },
                    { data: 'follows', name: 'follows' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },
    //-------------------------------------------------------------------------
    podcast: {
        index: function () {
            $('#podcast-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: [ -1, -2 ]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'speaker', name: 'speaker' },
                    { data: 'category', name: 'category' },
                    { data: 'date', name: 'date' },
                    { data: 'likes', name: 'likes' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    //------------------------------------------------------------------------
    
    live_streaming: {
        index: function () {
            $('#livestreaming-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: [ -1, -2 ]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'category', name: 'category' },
                    { data: 'price', name: 'price' },
                    { data: 'type', name: 'type' },
                    { data: 'date', name: 'date' },
                    { data: 'time', name: 'time' },
                    { data: 'ticket', name: 'ticket' },
                    { data: 'likes', name: 'likes' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    //-------------------------------------------------------------------------
    podcastpart: {
        index: function () {
            $('#podcastpart-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'likes', name: 'likes' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },
    // ------------------------------------------------------------------------

    podcast_category: {
        index: function () {
            $('#podcastcategory-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'title', name: 'title' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------

    live_streaming_category: {
        index: function () {
            $('#livestreamingcategory-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'title', name: 'title' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------

    channel_category: {
        index: function () {
            $('#channelcategory-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'title', name: 'title' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------

    live_streaming_order: {
        index: function () {
            $('#livestreamingorder-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'user', name: 'user' },
                    { data: 'live_streaming', name: 'live_streaming' },
                    { data: 'final_price', name: 'final_price' },
                    { data: 'payment_status', name: 'payment_status' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------

    plan_order: {
        index: function () {
            $('#planorder-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'user', name: 'user' },
                    { data: 'plan', name: 'plan' },
                    { data: 'final_price', name: 'final_price' },
                    { data: 'payment_status', name: 'payment_status' },
                    { data: 'mobile_invite_1', name: 'mobile_invite_1' },
                    { data: 'mobile_invite_2', name: 'mobile_invite_2' },
                    { data: 'updated_at', name: 'updated_at' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------


    video: {
        index: function () {
            $('#video-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2, -3]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'video_type', name: 'video_type' },
                    { data: 'focus_topic', name: 'focus_topic' },
                    { data: 'likes', name: 'likes' },
                    { data: 'seen', name: 'seen' },
                    { data: 'offline', name: 'offline' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },
    },
    
    category: {
        index: function () {     
            $('#category-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },

    },
    program: {
        index: function () {
            $('#program-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2, -3]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'program_type', name: 'program_type' },
                    { data: 'focus_topic', name: 'focus_topic' },
                    { data: 'created_by', name: 'created_by' },
                    { data: 'favorite_count', name: 'favorite_count' },
                    { data: 'offline', name: 'offline' },
                    { data: 'public', name: 'public' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },
    },
    subscription: {
        index: function () {
            $('#subscription-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'user', name: 'user' },
                    { data: 'amount', name: 'amount' },
                    { data: 'charge_id', name: 'charge_id' },
                    { data: 'date', name: 'date' },
                    // { data: 'actions', name: 'actions' }
                ],
            });
        },
    },
    focus_topic: {
        index: function () {
            $('#focustopic-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'actions', name: 'actions' }
                ],
            });
        },
    },
    share_program: {
        index: function () {
            $('#shareprogram-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'program__name', name: 'program__name' },
                    { data: 'message', name: 'message' },
                    { data: 'free_month', name: 'free_month' },
                    { data: 'created_at', name: 'created_at' },
                    { data: 'share_by', name: 'share_by' },
                    { data: 'share_to', name: 'share_to' }
                ],
            });
        },
    },
    article: {
        index: function () {
            $('#article-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'actions', name: 'actions' },
                ],
            });
        },
    },
    articlecontent: {
        index: function () {
            $('#articlecontent-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'name', name: 'name' },
                    { data: 'language', name: 'language' },
                    { data: 'actions', name: 'actions' },
                ],
            });
        },
    },
    favorite_video: {
        index: function () {
            $('#favoritevideo-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'user', name: 'user' }
                ],
            });
        },
    },
    favorite_program: {
        index: function () {
            $('#favoriteprogram-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1, -2]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'user', name: 'user' }
                ],
            });
        },
    },
    seen: {
        index: function () {

            $('#seen-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'user', name: 'user' },
                    { data: 'timeline', name: 'timeline' },
                    { data: 'date', name: 'date' },
                ],
            });
        },
    },
    video_offline: {
        index: function () {

            $('#videooffline-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'user', name: 'user' }
                ],
            });
        },
    },
    program_offline: {
        index: function () {

            $('#programoffline-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[0, "desc"]],
                columnDefs: [{
                    orderable: false,
                    targets: [-1]
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'user', name: 'user' }
                ],
            });
        },
    },
};


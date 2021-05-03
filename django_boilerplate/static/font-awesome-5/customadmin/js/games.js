/*global $ */
'use strict';

var games = {

    // ------------------------------------------------------------------------
    // Company
    // ------------------------------------------------------------------------
    company: {

        index: function () {
            $('#game-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                // processing: true,
                // serverSide: true,
                // ajax: {
                //     url: window.pagination_url,
                //     type: 'get',
                // },
                // columns: [
                //     { data: 'first_name', name: 'first name' },
                //     { data: 'last_name', name: 'last name' },
                //     { data: 'title', name: 'title' },
                //     { data: 'company', name: 'company' },
                //     { data: 'email', name: 'email' },
                //     { data: 'phone', name: 'phone' },
                //     { data: 'actions', name: 'actions' }
                // ],
            });

        },

        details: function () {

        }

    },

    // ------------------------------------------------------------------------

};

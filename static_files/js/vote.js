/*
   Function that send up/down vote request to server and updates
   up/down vote count with data recieved from the server.
 */
function postVote(event) {
    var action = $(this).data('on-click-action');
    var pk = $(this).data('name');

    var postData = {
        pk: pk,
        type: action
    };

    $.ajax({
        type: 'POST',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        url: event.data.voteUrl,
        data: postData,
        dataType: 'json',
        encode: true
    })

    .done(function(data) {

        var upbtn = $('#upbtn_' + pk);
        var dwnbtn = $('#dwnbtn_' + pk);

        if (action == 'upvote') {
            if ((upbtn.hasClass("clicked") && !dwnbtn.hasClass("clicked")) ||
               (!upbtn.hasClass("clicked") && !dwnbtn.hasClass("clicked"))) {
                upbtn.toggleClass("clicked");
            } else if (!upbtn.hasClass("clicked") && dwnbtn.hasClass("clicked")) {
                upbtn.toggleClass("clicked");
                dwnbtn.toggleClass("clicked");
            }
        } else {
            if ((!upbtn.hasClass("clicked") && dwnbtn.hasClass("clicked")) ||
               (!upbtn.hasClass("clicked") && !dwnbtn.hasClass("clicked"))) {
                dwnbtn.toggleClass("clicked");
            } else if (upbtn.hasClass("clicked") && !dwnbtn.hasClass("clicked")) {
                upbtn.toggleClass("clicked");
                dwnbtn.toggleClass("clicked");
            }
        }

        $('#upvote_count_' + pk).html(data.upvotes);
        $('#downvote_count_' + pk).html(data.downvotes);
    })
    .error(function(jqXHR) {
        console.log(jqXHR.status);
    })
}
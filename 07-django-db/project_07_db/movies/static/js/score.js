$(document).ready(function () {
    $('.rating').rating({ maxRating: 5 });
    $('#submitRating')
        .rating({
            initialRating: 0,
            maxRating: 5,
            onRate: function (rate) {
                $('#ratingNum').attr('value', rate);
            }
        })
    ;
    $('#ReadonlyRating')
        .rating('disable')
    ;
});
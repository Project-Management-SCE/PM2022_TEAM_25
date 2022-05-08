$(document).ready(function() {
    $("a").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('body,html').animate({
                scrollTop: $(hash).offset().top
            }, 1200, function() {
                window.location.hash = hash;
            });
        }
    });
});

var width = $(window).width();

window.onscroll = function() {
    if ((width >= 900)) {
        if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
            $("#middle").css("background-size", "150% auto");
        } else {
            $("#middle").css("background-size", "100% auto");
        }
    }
};

setTimeout(function() {
    $("#loading").addClass("animated fadeOut");
    setTimeout(function() {
        $("#loading").removeClass("animated fadeOut");
        $("#loading").css("display", "none");
    }, 800);
}, 1450);

function magnify(imglink) {
    $("#img_here").css("background", `url('${imglink}') center center`);
    $("#magnify").css("display", "flex");
    $("#magnify").addClass("animated fadeIn");
    setTimeout(function() {
        $("#magnify").removeClass("animated fadeIn");
    }, 800);
}

function linkedin() {
    window.location.href = "https://www.linkedin.com/in/ali-abu-abid-22a15820b/";
}



function Coffeeshop() {
    window.location.href = "https://github.com/AliAbuAbid/Coffeeshop";


}
var data = {
    resource_id: '680dfd9f-42a0-45b1-a418-a1cd6cff7417', // the resource id
    limit: 5, // get 5 results
    q: 'jones' // query for 'jones'
};
$.ajax({
    url: 'https://data.gov.il/api/3/action/datastore_search',
    data: data,
    dataType: 'jsonp',
    success: function(data) {
        alert('Total results found: ' + data.result.total)
    }
});
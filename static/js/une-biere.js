$(document).ready(function () {
    $(".ajout-biere-panier").each(function () {
        $(this).find(".redirect-url").val(window.location.href.replace(window.location.origin, ''));
    });
});

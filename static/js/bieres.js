$(document).ready(function () {
    $("#bouton-bieres").addClass("active");
    $("#selecteur-sous-sorte").select2({width: '350px'});
});

$(".ajout-biere-panier").submit(function () {
    $(this).find(".redirect-url").val(window.location.href.replace(window.location.origin, ''));
});

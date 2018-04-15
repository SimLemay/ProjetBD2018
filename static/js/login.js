$(document).ready(function () {
    // Par mesure de securite
    $('#courriel').val("");
    $('#mot_de_passe').val("");

    if ($('#message-erreur-connexion').length) {
        $("#modal-connexion").modal('show');
    }
});

$('.connexion-form').submit(function () {
    $(this).find(".page-courante").val(window.location.href.replace(window.location.origin, ''));
});

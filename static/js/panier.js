$(document).ready(function () {
    $("#bouton-panier").addClass("active");
});

$('.input-quantite').change(function () {
    $(this).closest('tr').find('.quantite').val($(this).val());
});

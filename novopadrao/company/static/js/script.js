$(document).ready(function () {

    var baseUrl = 'http://localhost:8000/';
    var deleteBtn = $('.delete-btn');
    var editBtn = $('.edit-btn')
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');
    var ocultDivBtn = $('#button_ocult');


    $(function () {



        $(".btn-toggle").click(function (e) {
            e.preventDefault();

            el = $(this).data('element');
            $(el).slideToggle('hidden');
        });
    });


    $(deleteBtn).on('click', function (e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Deseja deletar este cliente?');

        if (result) {
            window.location.href = delLink;
        }

    });


    $(searchBtn).on('click', function () {
        searchForm.submit();
    });

    $(filter).change(function () {
        var filter = $(this).val();
        window.location.href = baseUrl + "clients/" + '?filter=' + filter;
    });
    var options = {
        onKeyPress: function (phone, e, field, options) {
            var masks = ['(00) 0000-0000', '(00) 0 0000-0000'];
            var mask = (phone[5] == "9") ? masks[1] : masks
            [0];

            console.log("1:" + mask)
            $('#id_telefone1').mask(mask, options);
            $('#id_phone1').mask(mask, options);

        }
    };

    var options2 = {
        onKeyPress: function (phone, e, field, options2) {
            var masks2 = ['(00) 0000-0000', '(00) 0 0000-0000'];
            var mask2 = (phone[5] == "9") ? masks2[1] : masks2
            [0];

            console.log("2" + mask2)

            $('#id_phone2').mask(mask2, options2);
        }
    };



    $('#id_telefone1').mask('(00) 0000-0000', options)
    $('#id_telefone2').mask('(00) 0000-0000', options2)
    $('#id_phone1').mask('(00) 0000-0000', options)
    $('#id_phone2').mask('(00) 0000-0000', options2)

    $('#id_cnpj').mask('00.000.000/0000-00')

    // Mascara de dinheiro
    $(function () {
        $('.money').maskMoney({ prefix: 'R$ ', allowNegative: true, thousands: '.', decimal: ',', affixesStay: true });
    });
    // Mascara de quantidade
    $('.quantity').maskMoney({ allowNegative: true, thousands: '', decimal: ',', affixesStay: true });

    // Formula que calcula o preço x a quantidade
    $('.money').blur(function () {

        var price = $("#currency").val();
        price = price.replace("R$", "").trim();
        var arrayPrice = price.split(',');

        var real = arrayPrice[0].replace(".", "");
        var cents = arrayPrice[1];

        var result = `${real}.${cents}`

        var amount = $("#id_amount").val()

        amount = amount.replace(",", ".")

        var total = parseFloat(result) * parseFloat(amount);

        var valorFormatado = total.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    

        if (amount == "" || price == "") {
            $("#id_total").val("");
            console.log('error');
        } else {
            $("#id_total").val(valorFormatado);
        };

    });

    $("#new_service_button").click(function(){
        $(".minhaDiv2_item").clone(true|true).appendTo(".minhaDiv2");
      });



});
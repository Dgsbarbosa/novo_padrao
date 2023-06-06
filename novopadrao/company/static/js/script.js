$(document).ready(function () {

    var baseUrl = 'http://localhost:8000/';
    var deleteBtn = $('.delete-btn');
    var editBtn = $('.edit-btn')
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');
    var ocultDivBtn = $('#button_ocult');


    $(function () {

        $(".btn-toggle-budgets").click(function (e) {
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



    // mascaras de valores do primeiro formulario
    $("#id_service_form_1-price").maskMoney({ prefix: 'R$ ', allowNegative: true, thousands: '.', decimal: ',', affixesStay: true });
    $("#id_service_form_1-amount").maskMoney({ allowNegative: true, thousands: '', decimal: ',', affixesStay: true });





    $("#id_service_form_1-price").keypress(calculateTotal)
    $("#id_service_form_1-amount").keypress(calculateTotal)
    // função que adiciona um novo formario e serviço

    var serviceCount = 0;

    function addService() {
        serviceCount++;


        var newServiceForm = $('.service-item').first().clone();

        newServiceForm.find(':input').each(function () {

            // novo name para cada novo formulario de serviços
            var name = $(this).attr('name');
            var newName = name.replace('service_form_1-', `service_form_${serviceCount + 1}-`);

            $(this).attr('name', newName)
            name = $(this).attr('name');

            // Novo id para cada novo formulario de serviços
            var id = $(this).attr('id');
            var newId = id.replace('service_form_1-', `service_form_${serviceCount + 1}-`);
            $(this).attr('id', newId)
            id = $(this).attr('id');

            $(this).val('');

            // mascaras de valores dos formulario criados
            if (name.includes('price')) {
                $(this).maskMoney({ prefix: 'R$ ', allowNegative: true, thousands: '.', decimal: ',', affixesStay: true });
                $(this).keypress(calculateTotal);
            } else if (name.includes('amount')) {
                $(this).maskMoney({ allowNegative: true, thousands: '', decimal: ',', affixesStay: true });
                $(this).keypress(calculateTotal);
            }
        });

        newServiceForm.find('input[name$=id]').val('');
        newServiceForm.insertAfter($('.service-item').last());
        totalServices();

    }


    // calcula o campo total
    function calculateTotal() {
        $('.service-item').each(function () {
            var $serviceItem = $(this);
            var $priceInput = $serviceItem.find('input[name$="price"]');
            var $amountInput = $serviceItem.find('input[name$="amount"]');
            var $totalInput = $serviceItem.find('input[name$="total"]');

            var price = parseFloat($priceInput.val().replace('R$ ', '').replace('.', '').replace(',', '.'));
            var amount = parseFloat($amountInput.val().replace('.', '').replace(',', '.'));

            if (!isNaN(price) && !isNaN(amount)) {

                var total = price * amount;
                $totalInput.val('R$ ' + total.toLocaleString('pt-BR', { minimumFractionDigits: 2 }));
            } else if (!isNaN(price)) {
                var total = price * 1;
                $totalInput.val('R$ ' + total.toLocaleString('pt-BR', { minimumFractionDigits: 2 }));
            } else {
                $totalInput.val('');
            }

        });
    }



    $("#new_service_button").click(function (e) {
        e.preventDefault();
        addService();

        console.log('teste ' + $('#total_forms').val());


    });



    $(document).on('click', '.service-delete-btn', function (event) {

        event.preventDefault()
        if (serviceCount < 1) {

            alert("Esse serviço não pode ser excluido");

        } else {

            var result = confirm("Deseja excluir este serviço?");
            var serviceItem = $(this).closest('.service-item');


            if (result) {


                serviceItem.remove();
                serviceCount--;
                totalServices()
                editNameCamposForm();

            }


        };
        // 

    });

    // funcao que atuliza a quantidade formularios para passar para views
    function totalServices() {
        var countServices = document.querySelectorAll('.service-item')
        $('#total_forms').val(countServices.length);

    }

    // funcao que atualiza o name dos serviços apos excluido

    function editNameCamposForm() {
        var serviceItems = $('.service-item');
        var countServices = serviceItems.length;

        serviceItems.each(function (index) {
            $(this).find(':input').each(function () {
                var name = $(this).attr('name');
                var newName = name.replace(/service_form_\d+/, `service_form_${index + 1}`);
                $(this).attr('name', newName);

                var id = $(this).attr('id');
                var newId = id.replace(/service_form_\d+/, `service_form_${index + 1}`);
                $(this).attr('id', newId);
            });
        });
    }


});
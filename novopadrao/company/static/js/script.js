$(document).ready(function () {

    var baseUrl = 'http://localhost:8000/';
    var deleteBtn = $('.delete-btn');
    var editBtn = $('.edit-btn')
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');
    var ocultDivBtn = $('#button_ocult');

    // botão que esconde items do orcamento
    $(function () {

        $(".btn-toggle-budgets").click(function (e) {
            e.preventDefault();
            el = $(this).data('element');

            $('.my_div').not(el).slideUp('hidden');

            $(el).slideToggle('hidden');
        });
    });

    // botão que deleta um cliente
    $(deleteBtn).on('click', function (e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Deseja deletar este cliente?');

        if (result) {
            window.location.href = delLink;
        }

    });



    // botao que faz a busca
    $(searchBtn).on('click', function () {
        searchForm.submit();
    });

    $(filter).change(function () {
        var filter = $(this).val();
        window.location.href = baseUrl + "clients/" + '?filter=' + filter;
    });
    $('#filter-budgets option').each(function () {
        var text = $(this).text()
        $(this).val(text)
        console.log("teste");
    });

    $('#filter-budgets').change(function () {
        var filter = $(this).val();
        window.location.href = baseUrl + "budgets/" + '?filter-budgets=' + filter;
    });


    // mascaras de 

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


    $("#id_service_form_1-price").keypress(function () {
        calculateTotal('.service-item');
    });
    $("#id_service_form_1-amount").keypress(function () {
        calculateTotal('.service-item');

    });

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
    function calculateTotal(selector) {
        $(selector).each(function () {
            var $item = $(this);
            var $priceInput = $item.find('input[name*="price"]');
            var $amountInput = $item.find('input[name*="amount"]');

            console.log('$priceInput' + $priceInput);
            var $totalInput = $item.find('input[name*="total"]');

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


    });



    $(document).on('click', '.service-delete-btn', function (event) {

        event.preventDefault()
        if (serviceCount < 1) {

            alert("Esse serviço não pode ser excluido");

        } else {

            var result = confirm("Deseja excluir este serviço?");
            var item = $(this).closest('.service-item');


            if (result) {


                item.remove();
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
        var items = $('.service-item');
        var countServices = items.length;

        items.each(function (index) {
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


    // Criação de materiais

    //  adicionar mascara ao primeiro formulario

    $("#material-price").maskMoney({ prefix: 'R$ ', allowNegative: true, thousands: '.', decimal: ',', affixesStay: true });

    $("#material-amount").maskMoney({ allowNegative: true, thousands: '', decimal: ',', affixesStay: true });

    $("#material-price").keypress(function () {
        calculateTotal('.material-item');
    });
    $("#material-amount").keypress(function () {
        calculateTotal('.material-item');

    });


    // novo material

    var materialCount = 0
    function addMaterial() {
        materialCount++;

        var newMaterialForm = $('.material-item').first().clone();

        newMaterialForm.find(':input').each(function () {

            // novo name para cada novo formulario de serviços
            var name = $(this).attr('name');
            var newName = name.replace(/material_form_[0-9]-/, `material_form_${materialCount + 1}-`);
            $(this).attr('name', newName);

            // console.log('name: ' + name);
            // console.log('newName: ' + newName);

            var id = $(this).attr('id');
            var newId = id.replace(/material-descript/, `material-descript_${materialCount + 1}`);
            $(this).attr('id', newId);

            $(this).val('');
            // mascaras de valores dos formulario criados
            if (name.includes('price')) {
                $(this).maskMoney({ prefix: 'R$ ', allowNegative: true, thousands: '.', decimal: ',', affixesStay: true });
                $(this).keypress(function () {
                    calculateTotal('.material-item');



                });


            } else if (name.includes('amount')) {
                $(this).maskMoney({ allowNegative: true, thousands: '', decimal: ',', affixesStay: true });
                $(this).keypress(function () {
                    calculateTotal('.material-item');

                });

            }
        });

        newMaterialForm.find('input[name*=id]').val('');
        newMaterialForm.insertAfter($('.material-item').last());
        totalMaterials();

    }




    $("#new_material_button").click(function (e) {
        e.preventDefault();
        addMaterial();

    });



    $(document).on('click', '.material-delete-btn', function (event) {

        event.preventDefault()
        if (materialCount < 1) {

            alert("Esse material não pode ser excluido");

        } else {

            var result = confirm("Deseja excluir este material?");
            var materialItem = $(this).closest('.material-item');


            if (result) {

                materialItem.remove();
                materialCount--;
                totalMaterials()
                editCamposForm();

            }


        };
        // 

    });

    // funcao que atuliza a quantidade formularios para passar para views
    function totalMaterials() {
        var countMaterials = document.querySelectorAll('.material-item')
        $('#total_forms_materials').val(countMaterials.length);

    }

    // funcao que atualiza o name dos serviços apos excluido

    function editCamposForm() {
        var materialItems = $('.material-item');
        var countMaterial = materialItems.length;

        materialItems.each(function (index) {
            $(this).find(':input').each(function () {
                var name = $(this).attr('name');
                var newName = name.replace(/material_form_[0-9]/, `material_form_${index + 1}`) ;

                
            console.log('name: ' + name);
            


                $(this).attr('name', newName);
                
                console.log('newName: ' + newName);

                var id = $(this).attr('id');
                var newId = id.replace(/[0-9]+$/, "") + (index + 1);
                $(this).attr('id', newId);
            });
        });
    }








});
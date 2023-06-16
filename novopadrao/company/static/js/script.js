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

            if (el === '#minhaDiv5') {
                calculateTotalBudgets();
                writeValuesHtml();
            }
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


            $('#id_telefone1').mask(mask, options);
            $('#id_phone1').mask(mask, options);

        }
    };

    var options2 = {
        onKeyPress: function (phone, e, field, options2) {
            var masks2 = ['(00) 0000-0000', '(00) 0 0000-0000'];
            var mask2 = (phone[5] == "9") ? masks2[1] : masks2
            [0];


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
                $(this).keypress(function () {
                    calculateTotal('.service-item');



                });
            } else if (name.includes('amount')) {
                $(this).maskMoney({ allowNegative: true, thousands: '', decimal: ',', affixesStay: true });
                $(this).keypress(function () {
                    calculateTotal('.service-item');



                });;
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
        editCamposForm();

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
                var newName = name.replace(/material_form_[0-9]/, `material_form_${index + 1}`);

                $(this).attr('name', newName);


                var id = $(this).attr('id');
                var newId = id.replace(id, newName);
                $(this).attr('id', newId);
            });
        });
    }


    // Formas de pagamento

    // desconto
    $('input[name=discount]').on('change', function () {
        var valueSelect = $(this).val()
        $(this).closest('.form-group').find('#input_discount').remove();

        if (valueSelect === 'valor') {
            var newInput = '<input type="text" class="form-control form-control-input" id="input_discount" placeholder="Valor (R$ 0,00)" />';

            $(this).closest('.form-check').after(newInput);

            $("#input_discount").maskMoney({ prefix: 'R$ ', allowNegative: true, thousands: '.', decimal: ',', affixesStay: true });

        } else if (valueSelect === 'porcentagem') {
            var newInput = '<input type="text" class="form-control form-control-input" id="input_discount" placeholder="Porcentagem (%)" />';
            $(this).closest('.form-check').after(newInput);
            $('#input_discount').mask('##000%', { reverse: true })
        }

    });

    //condiçoes de pagamento

    $('input[name=condition]').on('change', function () {

        var valueSelect = $(this).val();

        $(this).closest('.form-group').find('#input_condition').remove();

        if (valueSelect === "sinal") {
            var newElement = '<input class="form-control form-control-input" type="text" id="input_condition" placeholder="Sinal de ..." />';

            $(this).closest('.form-check').after(newElement)

        }

        else if (valueSelect === "parcelas") {

            var newElement = '<select class="form-control form-control-input" id="input_condition" >';

            for (var i = 1; i <= 12; i++) {
                if (i === 1) {
                    newElement += '<option value="' + i + '" selected>' + i + 'x' + '</option>';
                } else {
                    newElement += '<option value="' + i + '">' + i + 'x' + '</option>';
                }
            }
            newElement += '</select>';

            $(this).closest('.form-check').after(newElement);
        }

    });


    function totalValuesServices() {

        var services = document.querySelectorAll('input[id^="id_service_form_"][id$="-total"]')

        var values = [];

        let control = 1
        services.forEach(service => {
            valueTxt = service.value
            if (valueTxt) {

                service = valueTxt.replace("R$", "").replace(".", "").replace(",", ".")
                service = parseFloat(service);
            } else {
                service = 0.00;
            }
            values.push(service);


            console.log(`service: ${control}: ${service}`)

            control++;
        });

        var result = values.reduce(function (acumulador, elemento) {
            return acumulador + elemento;
        }, 0)

        return result

    }

    function totalValuesMaterials() {
        let control = 1
        var materials = document.querySelectorAll('input[id^="material"][id$="-total"]')

        var values = [];

        materials.forEach(material => {
            valueText = material.value
            if (valueText) {
                service = valueText.replace("R$", "").replace(".", "").replace(",", ".")
                service = parseFloat(service)
            } else {
                service = 0
            }
            values.push(service)
            console.log(`material ${control}: ${service}`);

        });
        var result = values.reduce(function (acumulador, elemento) {
            return acumulador + elemento;
        }, 0)



        return result



    }


    // calcula o todal do orçamento

    function calculateTotalBudgets() {
        var totalServices = totalValuesServices();


        var totalMaterials = totalValuesMaterials();

        var totalBudgets = totalServices + totalMaterials;

        var discountTxt = $("#input_discount").val();

        var discount = 0;



        if (discountTxt) {
            if (discountTxt.includes("R$")) {
                discount = discountTxt.replace('R$', "").replace(".", "").replace(",", ".")
                discount = parseFloat(discount)

                totalBudgets = totalBudgets - discount

            }
            else {
                discount = discountTxt.replace("%", "");
                discount = discount / 100;
                totalBudgets = totalBudgets - (totalBudgets * discount)
            }

        }


        return totalBudgets;

    }

    // escreve os valores na aba total

    function writeValuesHtml() {

        $(".total-item").remove();

        var totalBudgets = calculateTotalBudgets();

        // escreve o valor total de serviços

        var totalServices = totalValuesServices()
        totalServices = parseFloat(totalServices).toFixed(2)
        var formattedTotalServices = parseFloat(totalServices).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });


        var writeTotalService = '' +

            '<div class="total-item">' +

            `<h2>Total Services: ${formattedTotalServices}</h2>` +
            '</div>';

        $("#minhaDiv5").append(writeTotalService);


        // ESCREVE O TOTAL DE MATERIAL

        var totalMaterials = totalValuesMaterials()
        totalMaterials = parseFloat(totalMaterials).toFixed(2)
        var formattedTotalMaterials = parseFloat(totalMaterials).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });


        var writeTotalMaterials = '' +

            '<div class="total-item" style="display:flex; justify-content: space-between;">' +

            `<h2>Total Materials: <span> ${formattedTotalMaterials}</span></h2>` +
            '</div>';

        $("#minhaDiv5").append(writeTotalMaterials);

        // escreve o desconto

        var discount = $("#input_discount").val();

        if (!discount) {
            discount = "";
        }


        var writeDiscount = '' +

            '<div class="total-item" style="display:flex; justify-content: space-between;">' +

            `<h2>Desconto: <span> ${discount}</span></h2>` +
            '</div>';

        $("#minhaDiv5").append(writeDiscount);


        // escreve a quantidade de parcelas

        var conditionPay = $("#input_condition").val();
        
        var conditionSelected = $('input[name=condition]:checked').val();

        var conditionText = ""
        
        
        if (!conditionPay) {
            conditionPay = ""
        }

        if (conditionSelected === "a vista"){
            conditionText = "A vista"
        }else if(conditionSelected === "sinal"){
            conditionText = `Sinal de ${conditionPay}`

        }else if(conditionSelected == "parcelas"){
            var valueParcel = totalBudgets / conditionPay
            valueParcel = parseFloat(valueParcel).toFixed(2)
            var formatedValueParcel = parseFloat(valueParcel).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

            conditionText = `Parcelado em ${conditionPay}x de ${formatedValueParcel} `
        }

        var writeConditionPay = '' +

            '<div class="total-item" style="display:flex; justify-content: space-between;">' +

            `<h2>Condição de pagamento: <span>${conditionText} </span></h2>` +
            '</div>';

        $("#minhaDiv5").append(writeConditionPay);

        console.log("condicao de pagamento: " + conditionText);

        // total do orçamento

        
        totalBudgets = parseFloat(totalBudgets).toFixed(2)

        var formatedTotalBudgets = parseFloat(totalBudgets).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });



        var writeTotalBudgets = '' +

            '<div class="total-item" style="display:flex; justify-content: space-between;">' +

            `<h2>Total do orçamento: <span> ${formatedTotalBudgets}</span></h2>` +
            '</div>';

        $("#minhaDiv5").append(writeTotalBudgets);

    }

















    //fechamento final 

});
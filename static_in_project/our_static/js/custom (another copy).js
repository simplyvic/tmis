
$(document).ready(function() {


    if ($(".success")[0]){
      // alert("Item successfully created.\n Click here to receive this from vendor");
          $(function() {
            $( ".success" ).dialog({
                open: function(event, ui){
                 setTimeout("$('.success').dialog('close')",5000);
                },
                modal: false,
                // position: [100, 100],
                resizeable: false,
                draggable: false,
                autoOpen: true,
                show: {
                  effect: "fade",
                  duration: 1000,
                  },

                hide: {
                  effect: "fade",
                  duration: 500
                }
            });
          });

    // } else {
    //     alert("An Error occured")
    }


    if ($(".error")[0]){
      // alert("Item successfully created.\n Click here to receive this from vendor");
          $(function() {
            $( ".error" ).dialog({
              open: function(event, ui){
                 setTimeout("$('.error').dialog('close')",100000);
                },
                autoOpen: true,
                show: {
                  effect: "bounce",
                  duration: 1000,
                },

                hide: {
                  effect: "bounce",
                  duration: 500
                }
            });
          });
    }

  
  $('.tabs').tabs();
  $('.pannel').accordion({collapsible: true},{heightStyle: 'content'},{icons: {
                                                                                header: "ui-icon-plus",
                                                                                activeHeader: "ui-icon-minus"
                                                                              }
                                                                      }
                        );


    // REMEMBER THE LAST SETTINGS TAB
    function tab() { //tab with cookie function
      $( ".tabs" ).tabs({
        active   : $.cookie('activetab'),
        activate : function( event, ui ){
            $.cookie( 'activetab', ui.newTab.index(),{
                expires : 10
            });
        }
      });
    }


    var url      = window.location.href;     // Returns full URL
      // var pathname = window.location.pathname; // Returns path only

    var store = "store_";
    var fixAsset = "fix_assets";
    var settings = "settings";

    storeResults = url.search(store);
    assetResults = url.search(fixAsset);
    settingsResults = url.search(settings);

    // if ((storeResults != -1) || (assetResults != -1)){
    //   $('#settings').show();
    // }else $('#settings').hide();

    // if (settingsResults != -1){
    //   $('#settings').hide();
    //   tab(); //calling the tab with coockie function
    // }

  
    var elementsToReset = $('.store-form #id_issue_amount, .store-form #id_issue_to, .store-form #id_department, .store-form #id_unit, .store-form #id_receive_amount, .store-form #id_supplier_name, .store-form #id_serial_number_begins, .store-form #id_serial_number_ends, .store-form #id_phone_number, .store-form #id_ministry_or_department');

    elementsToReset.val('');

    var endDate = $('#id_enddate');
    endDate.val('2037-12-31');
    // $('#id_reorder_level').val(0);


    var assetVehicle = $('.asset-form #div_id_number_plate, .inline-search #div_id_number_plate, .inline-search #div_id_chasis_number, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number');
    var assetBuildingLand = $('#div_id_plot_or_building_number, #div_id_size, .inline-search #div_id_plot_or_building_number');
    var assetFurniture = $('#div_id_serial_number');
    var hideWarrantyMinistry = $('.asset-form #div_id_delivery_date, .asset-form #div_id_waranty_starts, .asset-form #div_id_waranty_ends, .asset-form #div_id_ministry_or_department,  .asset-form #div_id_unit');


    hiddenFields = $('.form-edit #div_id_serial_number, .form-edit #div_id_plot_or_building_number, .form-edit #div_id_size, .form-edit #div_id_serial_number, .form-edit #div_id_delivery_date, .form-edit #div_id_waranty_starts, .form-edit #div_id_waranty_ends, #div_id_depreciation_commencement_date, #div_id_depreciation_percentage')
    hiddenFields.hide()

    // Note in USE On Clicking View More
      $('.viewmore, .edit').click(function() {
        hiddenFields.slideToggle()
    });


    var disableFormFields = ('.form-edit :text, .form-edit .select, .form-edit .textarea, .form-edit .checkboxinput, .form-edit :input[type="number"], form .save, form-edit .update, form #show_update_button');
    $(disableFormFields).prop('disabled', true)
    $('.edit').click(function(){
      $(disableFormFields).prop('disabled', false);
      $('html, body').animate({scrollTop : 0},800);
      return false;
    });

    $('#show_update_button').click(function(){
      if(document.getElementById('show_update_button').checked) {
        $('.update').show(200)
      }else{
        $('.update').hide(200)
      }

    });

    // $('.show_update_button').click(function(){
    //     alert('Clicked')
    //     if ($('#div_id_vehicles .checked')[0]) {
    //       $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideDown();
    //     }else if ($('#id_vehicles').not(':checked')) {
    //       $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideUp()
    //     }
    //   });

    // if(document.getElementById('isAgeSelected').checked) {
    // $("#txtAge").show();
    // } else {
    //     $("#txtAge").hide();
    // }



   // Scroll Top Script
   //Check to see if the window is top if not then display button
    $(window).scroll(function(){
      if ($(this).scrollTop() > 300) {
        $('.scrollToTop').fadeIn();
      } else {
        $('.scrollToTop').fadeOut();
      }
    });

    //Click event to scroll to top
    $('.scrollToTop').click(function(){
      $('html, body').animate({scrollTop : 0},800);
      return false;
    });
   //END Scroll Top Script



    $(".jumbotron, .navbar").hide().fadeIn(1000);
    $('.jumbotron').ready(function () {
      $(".display-icons").hide().fadeIn(1000);
    })
    

    
    if ($(".help-block")[0]){
          $(function() {
            $( "#error-dialog" ).attr('title', 'Check Fields').text('ERROR!!\nPlease correct all the fields marked RED.')
          });
    }



    $('ul.nav li.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideDown(300);
      }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideUp(300);
      });



    $('<br />').insertAfter('#div_id_buildings_and_lands');

    $('<br /><br /><strong>For vouchers on hold</strong><hr class="form-divider">').insertAfter('#div_id_payment_method');

    $('<div class="head_of_section_to_be_signed_message"><br /><br /><strong>Select this section if voucher is returned to BE to be signed by Head Of Unit</strong><hr class="form-divider"></div>').insertAfter('#div_id_for_head_of_section');

    $('<div class="head_of_section_after_sign_message"><br /><br /><strong>Select this section if voucher is returned from BE after being signed by Head Of Unit</strong><hr class="form-divider"></div>').insertAfter('#div_id_date_voucher_and_cheque_received_by_BE');


    for_head_of_section_divs = $('.head_of_section_to_be_signed_message, #div_id_voucher_and_cheque_received_by_BE, #div_id_voucher_and_cheque_received_by, #div_id_date_voucher_and_cheque_received_by_BE,    .head_of_section_after_sign_message,    #div_id_received_from_BE_by_cage1_2nd_time,     #div_id_date_received_from_BE_by_cage1_2nd_time')
    $(for_head_of_section_divs).slideUp()

    if ( $('#id_for_head_of_section').val() =="Yes"){
      $(for_head_of_section_divs).slideDown()
    }
    else{
        $(for_head_of_section_divs).slideUp()
      }

    $('#id_for_head_of_section').on('change',function(){
      if( $(this).val()=="Yes"){
        $(for_head_of_section_divs).slideDown()
      }
      else{
        $(for_head_of_section_divs).slideUp()
      }
    });


    $('.comments').click(function(){
      $('#div_id_comments').slideToggle()
    });


    $('.another-gratuity').click(function(){
      $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_other_deduction, #div_id_second_date_paid').slideToggle()
    });



    $('.comments').click(function(){
      $('#div_id_comments').slideToggle()
    });






    // Pagination Script
    $('.table').paging({limit:15});
    // END Pagination Script
     

     // $('input').iCheck({
     //    checkboxClass: 'icheckbox_square-blue',
     //    radioClass: 'iradio_square-blue',
     //    increaseArea: '20%' // optional
     //  });

     



      if ($(".help-block")[0]){
        // alert("Item successfully created.\n Click here to receive this from vendor");
            $(function() {
              $( "#error-dialog" ).attr('title', 'Check Fields').text('ERROR!!\nPlease correct all the fields marked RED.')
              // alert('There are errors in fields marked red.')
            });
      }


      // hide and show asset fields for vehicle (WithOUT iCheck)

      if ($('#div_id_vehicles .checked')[0]) {
        $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideDown();
      }else if ($('#id_vehicles').not(':checked')) {
        $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideUp()
      };


      $('.icheckbox_square-blue').click(function(){
        alert('Clicked')
        if ($('#div_id_vehicles .checked')[0]) {
          $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideDown();
        }else if ($('#id_vehicles').not(':checked')) {
          $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideUp()
        }
      });
      // END hide and show asset fields for vehicle


    NProgress.start();
    NProgress.done();


    $(".dateinput").datepicker({yearRange: '1930:2100', showButtonPanel: true, changeMonth: true, changeYear: true, dateFormat: 'yy-mm-dd'});
    // $(".datetimeinput").datetimepicker({format:'Y-m-d H:i',}); //Pick date and time manually
    $("#id_start_date, #id_end_date").datetimepicker({format:'Y-m-d H:i',}); //Pick date and time manually

    // document.getElementById('id_date_received_by_bank_transfer').value = moment().format('YYYY-MM-DD HH:mm');

    var currentDateAndTime = moment().format('YYYY-MM-DD HH:mm');
    var autoDateFields = $('.voucher-input-form .datetimeinput').not('#id_date_hold');
    $(autoDateFields).val(currentDateAndTime); //Auto-Add datetTime
    // $(autoDateFields).prop('disabled', true); //Disable Auto-Add dateTime field
    $('.voucher-input-form #id_date_hold').datetimepicker({format:'Y-m-d H:i'}) //Pick date and time manually for Date hold in voucher generation
    

      // Reload page without losing whats already entered in the form
      window.onbeforeunload = function() {
        localStorage.setItem(category, $('#id_category').val());
        localStorage.setItem(item_name, $('#id_item_name').val());
        localStorage.setItem(quantity, $('#id_quantity').val());
        localStorage.setItem(serial_number_begins, $('#id_serial_number_begins').val());
        localStorage.setItem(serial_number_ends, $('#id_serial_number_ends').val());
        // ...
    }

    window.onload = function() {

        var quantity = localStorage.getItem(quantity);
        if (quantity !== null) $('#id_quantity').val(quantity);

        // ...
    }

  (function blink() { 
    $('.blink-me').fadeOut(500).fadeIn(500, blink); 
  });

});//Document.ready closing brace

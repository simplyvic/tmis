
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
  $('.pannel').accordion({active: false},{collapsible: true},{heightStyle: 'content'},{icons: {
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

  
    var elementsToReset = $('.store-form #id_issue_amount, .store-form #id_issue_to, .store-form #id_department, .store-form #id_unit, .store-form #id_receive_amount, .store-form #id_supplier_name, .store-form #id_serial_number_begins, .store-form #id_serial_number_ends, .store-form #id_phone_number, .store-form #id_ministry_or_department, .store-form #id_returned_by');

    elementsToReset.val('');

    var endDate = $('#id_enddate');
    endDate.val('2037-12-31');

    var DueOnDate = $('#id_due_on');
    DueOnDate.val('2500-12-31');
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


    // var disableFormFields = ('.form-edit :text, .form-edit .select, .form-edit .textarea, .form-edit .checkboxinput, .form-edit :input[type="number"], form .save, form-edit .update, form #show_update_button');
    // $(disableFormFields).prop('disabled', true)
    // $('.edit').click(function(){
    //   $(disableFormFields).prop('disabled', false);
    //   $('html, body').animate({scrollTop : 0},800);
    //   return false;
    // });

    // $('#show_update_button').click(function(){
    //   if(document.getElementById('show_update_button').checked) {
    //     $('.update').show(200)
    //   }else{
    //     $('.update').hide(200)
    //   }

    // });

    // $('#id_conversation').prop('disabled', true)
    $('#id_add_comment').val('');
    
    var disableFields = ('.time_ended :text, .time_ended .select, .time_ended .textarea,\
                              .time_ended .checkboxinput, .time_ended :input[type="number"]');
    $(disableFields).prop('disabled', true)

    $('.time_ended #div_id_audit_phase, .time_ended #div_id_completed, .time_ended #div_id_date_completed').hide(200)
    $('#id_ext').prop('disabled', false)

    $('#id_ext').click(function(){
      if(document.getElementById('id_ext').checked) {
        $('.time_ended').prop('disabled', false)
      }else{
        $('.time_ended').prop('disabled', true)
      }

    });

    var receive = "/receive";
    var receive_ = "/receive_";
    receiveResults = url.search(receive);
    receive_Results = url.search(receive_);

    // -1 means false

    if ((receiveResults != -1) && (receive_Results == -1)){
        if(document.getElementById('id_returns').checked) {
          $('#div_id_returned_by').show(200)
          $('#div_id_supplier_name').hide(200)
        }else{
          $('#div_id_returned_by').hide(200)
          $('#div_id_supplier_name').show(200)
        }
    }

    // $('<div class="form-group"> <div id="div_id_returns" class="checkbox"> <label for="id_returns" class=""> <input class="checkboxinput" id="id_returns" name="returns" type="checkbox">Returns</label> </div> </div>').insertAfter('#div_id_serial_number_ends');

    
    $('<br /><div id="div_id_show_management_response" class="checkbox"> \
      <label for="id_show_management_response" class="">\
      <input class="checkboxinput" id="id_show_management_response" name="id_show_management_response" \
      type="checkbox">Show management response</label> </div><br /><br />'
      ).insertAfter('#div_id_recommendation');
    
    
    $('#id_show_management_response').click(function(){
      if(document.getElementById('id_show_management_response').checked) {
        $('#div_id_mgt_response').show(200)
        $('#div_id_mgt_action').show(200)
        $('#div_id_mgt_impl_timeline').show(200)
        $('#div_id_mgt_person').show(200)
        $('#div_id_rec_implemented').show(200)
      }else{
        $('#div_id_mgt_response').hide(200)
        $('#div_id_mgt_action').hide(200)
        $('#div_id_mgt_impl_timeline').hide(200)
        $('#div_id_mgt_person').hide(200)
        $('#div_id_rec_implemented').hide(200)
      }

    });
    // $('.bucket #div_id_audit_phase').hide(200)//hide Audit phase when page loads

    // $('#div_id_audit_task').click(function(){//hide or show Audit phase when checkbox(This is an audit task) is selected
    //   if(document.getElementById('id_audit_task').checked) {
    //     $('#div_id_audit_phase').show(200)
    //   }else{
    //     $('#div_id_audit_phase').hide(200)
    //   }

    // });

    // $('#div_id_rec_implemented').click(function(){
    //     alert('Clicked')
    //     if ($('#div_id_vehicles .checked')[0]) {
    //       $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideDown();
    //     }else if ($('#id_vehicles').not(':checked')) {
    //       $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideUp()
    //     }
    //   });

   



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


    // <div id="div_id_rec_implemented" class="checkbox"> <label for="id_rec_implemented" class=""> <input class="checkboxinput" id="id_rec_implemented" name="rec_implemented" type="checkbox">Recommendation Implemented / Response Accepted</label> </div>
    
    // <label><input class="checkboxinput" id="id_show_management_response" name="show_management_response" type="checkbox">Show management response</label>


    


    
    for_head_of_section_divs = $('.head_of_section_to_be_signed_message, #div_id_voucher_and_cheque_received_by_BE,\
      #div_id_voucher_and_cheque_received_by, #div_id_date_voucher_and_cheque_received_by_BE,\
      .head_of_section_after_sign_message,    #div_id_received_from_BE_by_cage1_2nd_time,\
      #div_id_date_received_from_BE_by_cage1_2nd_time')
    
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

      // if ($('#div_id_audit_task .checked')[0]) {
      //   $('.bucket #id_audit_phase').slideDown();
      // }else if ($('#id_vehicles').not(':checked')) {
      //   $('.bucket #id_audit_phase').slideUp()
      // };


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
    $("#id_start_date, #id_end_date, #id_due_date").datepicker({format:'Y-m-d H:i',}); //Pick date and time manually

    // document.getElementById('id_date_received_by_bank_transfer').value = moment().format('YYYY-MM-DD HH:mm');

    var currentDateAndTime = moment().format('YYYY-MM-DD HH:mm');
    // var autoDateFields = $('.voucher-input-form .datetimeinput').not('#id_date_hold');************ Removed after adding the click function
    // $(autoDateFields).val(currentDateAndTime); //Auto-Add datetTime
    
    // $(autoDateFields).prop('disabled', true); //Disable Auto-Add dateTime field
    $('.voucher-input-form #id_date_hold').datetimepicker({format:'Y-m-d H:i'}) //Pick date and time manually for Date hold in voucher generation
    

    $('#id_received_from_BE_by_cage1').click(function(){
      if(document.getElementById('id_received_from_BE_by_cage1').checked) {
        $('#id_date_received_from_BE_by_cage1').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_from_BE_by_cage1').val(''); //Auto-Add datetTime
      }
    });

    $('#id_voucher_generated').click(function(){
      if(document.getElementById('id_voucher_generated').checked) {
        $('#id_date_generated').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_generated').val(''); //Auto-Add datetTime
      }
    });

    $('#id_hold_voucher').click(function(){
      if(document.getElementById('id_hold_voucher').checked) {
        $('#id_date_hold').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_hold').val(''); //Auto-Add datetTime
      }
    });

    $('#id_received_by_bank_transfer').click(function(){
      if(document.getElementById('id_received_by_bank_transfer').checked) {
        $('#id_date_received_by_bank_transfer').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_by_bank_transfer').val(''); //Auto-Add datetTime
      }
    });

    $('#id_received_by_store').click(function(){
      if(document.getElementById('id_received_by_store').checked) {
        $('#id_date_received_by_store').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_by_store').val(''); //Auto-Add datetTime
      }
    });

    $('#id_received_by_accounting_unit').click(function(){
      if(document.getElementById('id_received_by_accounting_unit').checked) {
        $('#id_date_received_by_accounting_unit').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_by_accounting_unit').val(''); //Auto-Add datetTime
      }
    });

    $('#id_received_by_revenue').click(function(){
      if(document.getElementById('id_received_by_revenue').checked) {
        $('#id_date_received_by_revenue').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_by_revenue').val(''); //Auto-Add datetTime
      }
    });

    $('#id_received_by_CPO').click(function(){
      if(document.getElementById('id_received_by_CPO').checked) {
        $('#id_date_received_by_CPO').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_by_CPO').val(''); //Auto-Add datetTime
      }
    });

    $('#id_received_from_CPO_by_cage2').click(function(){
      if(document.getElementById('id_received_from_CPO_by_cage2').checked) {
        $('#id_date_received_from_CPO_by_cage2').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_from_CPO_by_cage2').val(''); //Auto-Add datetTime
      }
    });

    $('#id_received_from_CPO_by_cage1').click(function(){
      if(document.getElementById('id_received_from_CPO_by_cage1').checked) {
        $('#id_date_received_from_CPO_by_cage1').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_from_CPO_by_cage1').val(''); //Auto-Add datetTime
      }
    });

    $('#id_voucher_and_cheque_received_by_BE').click(function(){
      if(document.getElementById('id_voucher_and_cheque_received_by_BE').checked) {
        $('#id_date_voucher_and_cheque_received_by_BE').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_voucher_and_cheque_received_by_BE').val(''); //Auto-Add datetTime
      }
    });

    $('#id_received_from_BE_by_cage1_2nd_time').click(function(){
      if(document.getElementById('id_received_from_BE_by_cage1_2nd_time').checked) {
        $('#id_date_received_from_BE_by_cage1_2nd_time').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_received_from_BE_by_cage1_2nd_time').val(''); //Auto-Add datetTime
      }
    });

    $('#id_voucher_returned_to_BE').click(function(){
      if(document.getElementById('id_voucher_returned_to_BE').checked) {
        $('#id_date_returned').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_returned').val(''); //Auto-Add datetTime
      }
    });

    $('#id_collected_from_store').click(function(){
      if(document.getElementById('id_collected_from_store').checked) {
        $('#id_date_collected_from_store').val(currentDateAndTime); //Auto-Add datetTime
      }else{
        $('#id_date_collected_from_store').val(''); //Auto-Add datetTime
      }
    });

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


// on click, save it in localStorage.selectedTab
localStorage.selectedTab = $(this).index() + 1;

// on document ready, after click handler was added search for it
if (localStorage.selectedTab) {
  $(".tabs:eq(" + (localStorage.selectedTab - 1) + ")").click();
}


// or use this below

// $(".tabs").tabs({
//     activate: function( event, ui ) {
//         localStorage.selectedTab = ui.newTab.index() + 1;
//     },
//     active: localStorage.selectedTab ? localStorage.selectedTab - 1 : 0
// });

});//Document.ready closing brace


$(document).ready(function() {

    $(".jumbotron, .navbar, #version-display").hide().fadeIn(1000);
    $('.jumbotron').ready(function () {
      $(".display-icons").hide().fadeIn(1000);
    })
    

    // $("button").click(function() {
    //   $("#right").slideToggle();
    // });
    // $(".jumbotron").hide().slideDown(1000);
    // $(".dateinput").datepicker({minDate: new Date (1930,00,01), showButtonPanel: true, changeMonth: true, changeYear: true});
    $(".dateinput").datepicker({yearRange: '1930:2100', showButtonPanel: true, changeMonth: true, changeYear: true});

    // $(".btn-process").click(function(){
    // alert("Your transaction is being processed");
    // });

    if ($(".help-block")[0]){
      // alert("Item successfully created.\n Click here to receive this from vendor");
          $(function() {
            $( "#error-dialog" ).attr('title', 'Check Fields').text('ERROR!!\nPlease correct all the fields marked RED.')
          });
    }

    // if ($("#error_1_id_position_last_held")[0]){
    //   alert("Message");
    // // } else {
    // //     alert("An Error occured")
    // }

    $('ul.nav li.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(0).slideDown(300);
      }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(0).slideUp(300);
      });

    if ($(".success")[0]){
      // alert("Item successfully created.\n Click here to receive this from vendor");
          $(function() {
            $( ".success" ).dialog({
                open: function(event, ui){
                 setTimeout("$('.success').dialog('close')",3000);
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
                 setTimeout("$('.error').dialog('close')",60000);
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

// $('#div_id_second_position_last_held').click(function(){
//   $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_igp_deduction, #div_id_second_cfo_deduction, #div_id_second_date_paid').slideToggle()
// });


// $('#div_id_second_position_last_held').is(':ckecked')

if ($('#id_add_additional_gratuity').is(':checked')) {
  // alert('is Ckecked');
  $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_igp_deduction, #div_id_second_cfo_deduction, #div_id_second_date_paid').slideDown();
}else if ($('#id_add_additional_gratuity').not(':checked')) {
  $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_igp_deduction, #div_id_second_cfo_deduction, #div_id_second_date_paid').slideUp()
};


$('#id_add_additional_gratuity').click(function(){
  if ($('#id_add_additional_gratuity').is(':checked')) {
    // alert('is Ckecked');
    $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_igp_deduction, #div_id_second_cfo_deduction, #div_id_second_date_paid').slideDown();
  }else if ($('#id_add_additional_gratuity').not(':checked')) {
    $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_igp_deduction, #div_id_second_cfo_deduction, #div_id_second_date_paid').slideUp()
  }
});


$('.another-gratuity').click(function(){
  $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_igp_deduction, #div_id_second_cfo_deduction, #div_id_second_date_paid').slideToggle()
});


//   if ($('#id_approved_and_sumitted_to_NAO' && '#id_approved_by_NAO_and_sumitted_to_PMO').is(':checked')) {
//     $('#id_disapproved_by_AGD_and_returned_to_ministry_or_department, #id_disapproved_by_NAO_and_returned_to_ministry_or_department').attr('disabled', true);
//     // alert(state);
//   }else if ($('#id_approved_and_sumitted_to_NAO' && '#id_approved_by_NAO_and_sumitted_to_PMO').not(':checked')) {
//     $('#id_disapproved_by_AGD_and_returned_to_ministry_or_department, #id_disapproved_by_NAO_and_returned_to_ministry_or_department').attr('disabled', false);
//   //   alert(state);
//   }




// $('#id_approved_and_sumitted_to_NAO').click(function(){
//   if ($(this && '#id_approved_by_NAO_and_sumitted_to_PMO').is(':checked')) {
//     $('#id_disapproved_by_AGD_and_returned_to_ministry_or_department, #id_disapproved_by_NAO_and_returned_to_ministry_or_department').attr('disabled', true);
//     alert('NAO Checked');
//   }else if ($(this && '#id_approved_by_NAO_and_sumitted_to_PMO').not(':checked')) {
//     $('#id_disapproved_by_AGD_and_returned_to_ministry_or_department, #id_disapproved_by_NAO_and_returned_to_ministry_or_department').attr('disabled', false);
//     alert('NAO Unchecked');
//   }
// });



// $('#id_approved_by_NAO_and_sumitted_to_PMO').click(function(){
//   if ($(this && '#id_approved_and_sumitted_to_NAO').is(':checked')) {
//     $('#id_disapproved_by_AGD_and_returned_to_ministry_or_department, #id_disapproved_by_NAO_and_returned_to_ministry_or_department').attr('disabled', true);
//     alert('PMO Checked');
//   }else if ($(this && '#id_approved_by_NAO_and_sumitted_to_PMO').not(':checked')) {
//     $('#id_disapproved_by_AGD_and_returned_to_ministry_or_department, #id_disapproved_by_NAO_and_returned_to_ministry_or_department').attr('disabled', false);
//     alert('PMO Unchecked');
//   }
// });//id_approved_by_NAO_and_sumitted_to_PMO function closing brace

    // $('#div_id_ministry_or_department').on('change',function(){
    //     if( $(this).val()=="Judiciary"){
    //     $("#id_received_from_ministry_or_department").slideDown()
    //     }
    //     else{
    //     $("#id_received_from_ministry_or_department").slideUp()
    //     }
    // });

    // $('#div_id_ministry_or_department').change(function(){
    // selection = $(this).val();    
    // switch(selection)
    //   { 
    //    case 'Judiciary':
    //        $('#id_received_from_ministry_or_department').show();
    //        break;
    //    default:
    //        $('#id_received_from_ministry_or_department').hide();
    //        break;
    //   }
    // });

});//Document.ready clossing brace
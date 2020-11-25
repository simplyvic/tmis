
$(document).ready(function() {

  
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




// $(function () {
//     var icons = {
//         header: "ui-icon-triangle-1-e",
//         activeHeader: "ui-icon-triangle-1-s",
//         headerSelected: "ui-icon-triangle-1-s"
//     };
//     var act = 0;
//     $( ".pannel" ).accordion({
//         icons: icons,
//         collapsible: true,
//         clearStyle: true,
//         heightStyle: "content",
//         autoHeight: false,
//         create: function(event, ui) {
//             //get index in cookie on accordion create event
//             if($.cookie('saved_index') != null){
//                act =  parseInt($.cookie('saved_index'));
//             }
//         },
//         activate: function(event, ui) {
//             //set cookie for current index on change event
//             var active = jQuery(".pannel").accordion('option', 'active');
//             $.cookie('saved_index', null);
//             $.cookie('saved_index', active);
//         },
//         active:parseInt($.cookie('saved_index'))
//     });
//     $( "#toggle" ).button().toggle(function() {
//         $( ".pannel" ).accordion( "option", "icons", false );
//     },
//     function() {
//         $( ".pannel" ).accordion( "option", "icons", icons );
//     });
// });










var url      = window.location.href;     // Returns full URL
  // var pathname = window.location.pathname; // Returns path only

var store = "store_";
var fixAsset = "fix_assets";
var settings = "settings";

storeResults = url.search(store);
assetResults = url.search(fixAsset);
settingsResults = url.search(settings);

if ((storeResults != -1) || (assetResults != -1)){
  $('#settings').show();
}else $('#settings').hide();

if (settingsResults != -1){
  $('#settings').hide();
  tab(); //calling the tab with coockie function
}


  
  var elementsToReset = $('.store-form #id_issue_amount, .store-form #id_issue_to, .store-form #id_department, .store-form #id_unit, .store-form #id_receive_amount, .store-form #id_supplier_name');

  elementsToReset.val('');

  var endDate = $('#id_enddate');
  endDate.val('2037-12-31');
  // $('#id_reorder_level').val(0);


  var assetVehicle = $('.asset-form #div_id_number_plate, .inline-search #div_id_number_plate, .inline-search #div_id_chasis_number, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number');
  var assetBuildingLand = $('#div_id_plot_or_building_number, #div_id_size, .inline-search #div_id_plot_or_building_number');
  var assetFurniture = $('#div_id_serial_number');
  var hideWarrantyMinistry = $('.asset-form #div_id_delivery_date, .asset-form #div_id_waranty_starts, .asset-form #div_id_waranty_ends, .asset-form #div_id_ministry_or_department,  .asset-form #div_id_unit');

//   jQuery(function($){
//    $("#div_id_estimated_useful_life").Watermark("Number of years");
//    // $("#mi").Watermark("MI");
//    // $("#last").Watermark("Last");
//    // $("#suffix").Watermark("Suffix");
// });

  var e = document.getElementById("id_asset_class");
  // var strUser = e.options[e.selectedIndex].value;
    
    // if ((this.value) == 'Furniture & Fixtures'){
    //     assetFurniture.slideDown(); $('#div_id_location').slideDown()
    //   }else{assetFurniture.slideDown();}


    // if ((this.value) == 'Land & Buildings'){
    //   assetBuildingLand.slideDown(); $('#div_id_location').slideDown()
    // }else{assetBuildingLand.slideUp(); hideWarrantyMinistry.slideUp();}


    // if ((this.value) == 'Motor Vehicles'){
    //   // alert( this.value );
    //   assetVehicle.slideDown();
    // }else{assetVehicle.slideUp();}


    // if ((this.value) == 'Office Equipment'){
    //   assetFurniture.slideDown(); $('#div_id_location').slideDown()
    // }else{assetFurniture.slideDown();}
// On page load
  // $('.form-edit #div_id_serial_number, .form-edit #div_id_plot_or_building_number, .form-edit #div_id_size, .form-edit #div_id_serial_number, .form-edit #div_id_delivery_date, .form-edit #div_id_waranty_starts, .form-edit #div_id_waranty_ends, #div_id_depreciation_commencement_date, #div_id_depreciation_percentage').hide();
//   $('.form-edit #div_id_serial_number, .form-edit #div_id_plot_or_building_number, .form-edit #div_id_size, .form-edit #div_id_serial_number, .form-edit #div_id_delivery_date, .form-edit #div_id_waranty_starts, .form-edit #div_id_waranty_ends').hide();
// // On Clicking View More
//     $('.viewmore, .edit').click(function() {

//    if ((this.value) == 'Computer Equipments'){
//       $('#div_id_location').slideDown()
//     }else{assetFurniture.slideDown();}


//     if ((this.value) == 'Furniture & Fixtures'){
//       assetFurniture.slideDown(); $('#div_id_location').slideDown()
//     }else{assetFurniture.slideDown();}


//     if ((this.value) == 'Land & Buildings'){
//       assetBuildingLand.slideDown(); $('#div_id_location').slideDown(); hideWarrantyMinistry.slideUp();
//     }else{assetBuildingLand.slideUp(); hideWarrantyMinistry.slideDown();}


//     if ((this.value) == 'Motor Vehicles'){
//       // alert( this.value );
//       assetVehicle.slideDown();  $('#div_id_location').slideUp()
//     }else{assetVehicle.slideUp();}


//     if ((this.value) == 'Office Equipment'){
//       assetFurniture.slideDown();
//     }else{assetFurniture.slideDown();}


//     // if ((this.value) == 'Power Equipments'){
//     //   // alert( this.value );
//     // }else{alert("Computer not selected")}
//   });




// // On change event
//   $(e).on('change', function() {

//    if ((this.value) == 'Computer Equipments'){
//       $('#div_id_location').slideDown()
//     }else{assetFurniture.slideDown();}


//     if ((this.value) == 'Furniture & Fixtures'){
//       assetFurniture.slideDown(); $('#div_id_location').slideDown()
//     }else{assetFurniture.slideDown();}


//     if ((this.value) == 'Land & Buildings'){
//       assetBuildingLand.slideDown(); $('#div_id_location').slideDown(); hideWarrantyMinistry.slideUp();
//     }else{assetBuildingLand.slideUp(); hideWarrantyMinistry.slideDown();}


//     if ((this.value) == 'Motor Vehicles'){
//       // alert( this.value );
//       assetVehicle.slideDown();  $('#div_id_location').slideUp()
//     }else{assetVehicle.slideUp();}


//     if ((this.value) == 'Office Equipment'){
//       assetFurniture.slideDown();
//     }else{assetFurniture.slideDown();}


//     // if ((this.value) == 'Power Equipments'){
//     //   // alert( this.value );
//     // }else{alert("Computer not selected")}
//   });


  
//   // $('.enable-depreciation').click(function(){
//   //   $('#div_id_depreciation_commencement_date, #div_id_depreciation_percentage').slideToggle();
//   //   // $('#div_id_estimated_useful_life').slideToggle();
//   // });


hiddenFields = $('.form-edit #div_id_serial_number, .form-edit #div_id_plot_or_building_number, .form-edit #div_id_size, .form-edit #div_id_serial_number, .form-edit #div_id_delivery_date, .form-edit #div_id_waranty_starts, .form-edit #div_id_waranty_ends, #div_id_depreciation_commencement_date, #div_id_depreciation_percentage')
  hiddenFields.hide()
  // $('.asset-form #div_id_serial_number, .asset-form #div_id_plot_or_building_number, .asset-form #div_id_size, .asset-form #div_id_serial_number, .asset-form #div_id_delivery_date, .asset-form #div_id_waranty_starts, .asset-form #div_id_waranty_ends, .asset-form #div_id_depreciation_percentage, .asset-form #div_id_depreciation_commencement_date, .asset-form #div_id_user, .asset-form #div_id_department,  .asset-form #div_id_unit').hide();
  // Note in USE On Clicking View More
    $('.viewmore, .edit').click(function() {
      hiddenFields.slideToggle()
  //   var selected = $( "#id_category option:selected" ).text();

  //  if (selected == 'Computer and Networks'){
  //     allAssetFields.slideDown();
  //     hiddenForAssetComputerMachinery.hide();
  //   }  

  //   if (selected == 'Plant and Machinery'){
  //     allAssetFields.slideDown();
  //     hiddenForAssetComputerMachinery.hide()
  //   }

  //   if (selected == 'Furniture and Fittings'){
  //     allAssetFields.slideDown();
  //     hiddenForFurnitureFitting.hide();
  //   }

  //   if (selected == 'Lands'){
  //     allAssetFields.slideDown();
  //     hiddenForLand.hide();
  //   }

  //   if (selected == 'Buildings'){
  //     allAssetFields.slideDown();
  //     hiddenForBuilding.hide();
  //   }


  //   if (selected == 'Motor Vehicles and Motor Cycles'){
  //     allAssetFields.slideDown();
  //     hiddenForMotoVehiclesCycle.hide();
  //   }


  //   if (selected == 'Office Equipments'){
  //     allAssetFields.slideDown();
  //     hiddenForOfficeEquipment.hide();
  //   }


  });

  var disableFormFields = ('.form-edit :text, .form-edit .select, .form-edit .textarea, .form-edit .checkboxinput, .form-edit :input[type="number"], form .save');
  $(disableFormFields).prop('disabled', true)
  $('.edit').click(function(){
      $(disableFormFields).prop('disabled', false);
      $('html, body').animate({scrollTop : 0},800);
      return false;
    });









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
    

    // $("button").click(function() {
    //   $("#right").slideToggle();
    // });
    // $(".jumbotron").hide().slideDown(1000);
    
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
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideDown(300);
      }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideUp(300);
      });

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

// $('#div_id_second_position_last_held').click(function(){
//   $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_other_deduction, #div_id_second_date_paid').slideToggle()
// });


// $('#div_id_second_position_last_held').is(':ckecked')

// if ($('#id_add_additional_gratuity').is(':checked')) {
//   // alert('is Ckecked');
//   $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_other_deduction, #div_id_second_date_paid').slideDown();
// }else if ($('#id_add_additional_gratuity').not(':checked')) {
//   $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_other_deduction, #div_id_second_date_paid').slideUp()
// };


// $('#id_add_additional_gratuity').click(function(){
//   if ($('#id_add_additional_gratuity').is(':checked')) {
//     // alert('is Ckecked');
//     $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_other_deduction, #div_id_second_date_paid').slideDown();
//   }else if ($('#id_add_additional_gratuity').not(':checked')) {
//     $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_other_deduction, #div_id_second_date_paid').slideUp()
//   }
// });


// // hide and show asset fields for vehicle (WithOUT iCheck)

// if ($('#id_vehicles').is(':checked')) {
//   $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideDown();
// }else if ($('#id_vehicles').not(':checked')) {
//   $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideUp()
// };


// $('#id_vehicles').click(function(){
//   if ($('#id_vehicles').is(':checked')) {
//     $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideDown();
//   }else if ($('#id_vehicles').not(':checked')) {
//     $('.asset-form #div_id_number_plate, .asset-form #div_id_make, .asset-form #div_id_model, .asset-form #div_id_chasis_number').slideUp()
//   }
// });
// // END hide and show asset fields for vehicle



$('<br />').insertAfter('#div_id_buildings_and_lands');

// hide and show asset fields for buildings and lands

// if ($('#id_buildings_and_lands').is(':checked')) {
//   $('#div_id_plot_or_building_number, #div_id_size').slideDown();
// }else if ($('#id_buildings_and_lands').not(':checked')) {
//   $('#div_id_plot_or_building_number, #div_id_size').slideUp()
// };


// $('#id_buildings_and_lands').click(function(){
//   if ($('#id_buildings_and_lands').is(':checked')) {
//     $('#div_id_plot_or_building_number, #div_id_size').slideDown();
//   }else if ($('#id_buildings_and_lands').not(':checked')) {
//     $('#div_id_plot_or_building_number, #div_id_size').slideUp()
//   }
// });
// END hide and show asset fields for buildings and lands

$('.another-gratuity').click(function(){
  $('#div_id_second_ministry_or_department, #div_id_second_position_last_held, #div_id_second_date_of_retirement, #div_id_second_voucher_number, #div_id_second_gratuity_amount, #div_id_second_pension_p_a_amount, #div_id_second_pension_p_m_amount, #div_id_second_one_by_six_deduction, #div_id_second_salary_deduction, #div_id_second_other_deduction, #div_id_second_date_paid').slideToggle()
});



$('.comments').click(function(){
  $('#div_id_comments').slideToggle()
});






// Pagination Script
$('.table').paging({limit:15});
// END Pagination Script
 

 $('input').iCheck({
    checkboxClass: 'icheckbox_square-blue',
    radioClass: 'iradio_square-blue',
    increaseArea: '20%' // optional
  });




  // if ($(".help-block")[0]){
  //   // alert("Item successfully created.\n Click here to receive this from vendor");
  //       $(function() {
  //         $( "#error-dialog" ).attr('title', 'Check Fields').text('ERROR!!\nPlease correct all the fields marked RED.')
  //       });
  // }

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


// nanobar starts
//  var options = {
//   classname: 'my-class',
//   id: 'my-id',
//   target: document.getElementById('myDivId')
// };

// var nanobar = new Nanobar( nanobar );

// // move bar

// for (i = 0; i <= 100; i++) { 
//     nanobar.go( i ); // size bar 30%
// }
// size bar 100% and and finish
// nanobar.go(100);

// nanabar ends

NProgress.start();
NProgress.done();


  // if ( $.browser.msie ) {
  // alert( $.browser.version );
  // }

  // IE Warning script
    // var ua = window.navigator.userAgent;
    // var msie = ua.indexOf("MSIE ");

    // if (msie > 0) // If Internet Explorer, return version number
    // {
    //     // alert(parseInt(ua.substring(msie + 5, ua.indexOf(".", msie))));
    //       $(function() {
    //         $( ".iewarning" ).dialog({
    //             open: function(event, ui){
    //              setTimeout("$('.iewarning').dialog('close')",100000);
    //             },
    //             modal: false,
    //             // position: [100, 100],
    //             resizeable: false,
    //             draggable: false,
    //             autoOpen: true,
    //             show: {
    //               effect: "fade",
    //               duration: 1000,
    //               },

    //             hide: {
    //               effect: "fade",
    //               duration: 500
    //             }
    //         });
    //       });
    // }
    // else  // If another browser, return 0
    // return false;
    // // // IE Warning script

  // $(".dateinput").datepicker({minDate: new Date (1930,00,01), showButtonPanel: true, changeMonth: true, changeYear: true});
    $(".dateinput").datepicker({yearRange: '1930:2100', showButtonPanel: true, changeMonth: true, changeYear: true, dateFormat: 'yy-mm-dd'});
    $(".datetimeinput").datetimepicker({format:'Y-m-d H:i',});



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

});//Document.ready clossing brace

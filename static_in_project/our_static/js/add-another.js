(function($) {
    $(document).ready(function() {
        $('.add-another').click(function(e) {
            e.preventDefault();
            showAddAnotherPopup(this);
        });
        $('.related-lookup').click(function(e) {
            e.preventDefault();
            showRelatedObjectLookupPopup(this);
        });
    
        $('form#server_form :input:visible:enabled:first').focus()
    
    });
})(django.jQuery);
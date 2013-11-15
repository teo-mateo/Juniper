/**
 * Created by teo on 11/15/13.
 */

$(document).ready(function(){
    $("#new_contraption")
        .button()
        .click(function(event){
            event.preventDefault();
            $("#create_contraption_container").dialog("open");
        });

    $("#create_contraption_container")
        .dialog({
            autoOpen: false,
            height: 360,
            width: 800,
            modal: true,
            buttons: {
                "Save": function(){
                    //do the form submit
                    $("#create_contraption_form").submit();
                    $(this).dialog("close");
                },
                Cancel: function(){
                    $(this).dialog("close");
                }
            }
        });
});
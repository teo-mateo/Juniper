/**
 * Created by teo on 11/15/13.
 */

function editPage(id){
    var url = APP_SETTINGS.base_url + 'section/contraptions/get/page/raw/?id='+id;
    $.getJSON(url, function(data){
       var x = 1;
       var editor = new EpicEditor().load();
    });
}

function editContraption(id){
    var url = APP_SETTINGS.base_url + 'section/contraptions/get/contraption/raw/?id='+id;
    $.getJSON(url, function(data){
        $("#edit_contraption_form").find("#id")[0].value = id;
        $("#edit_contraption_form").find("#order")[0].value = data.order;
        $("#edit_contraption_form").find("#title")[0].value = data.title;
        $("#edit_contraption_form").find("#description")[0].value = data.description;
        $("#edit_contraption_form").find("#visible")[0].checked = data.visible;
        $("#edit_contraption_container").dialog("open");
    });
}

function deleteContraption(id){
    $("#dialog-confirm")[0].dataset["customdata"] = id;
    $("#dialog-confirm").dialog("open");
}

$(document).ready(function(){
    $("#dialog-confirm")
        .dialog({
            autoOpen: false,
            resizable: false,
            height:240,
            width: 500,
            modal: true,
            buttons: {
                "Delete item": function() {
                    var id = $(this)[0].dataset['customdata'];
                    var docUrl = document.URL;
                    var url = docUrl + 'delete/contraption/?id='+id;
                    $.getJSON(url, function(data){
                        location.reload();
                        });

                    delete $( this )[0].dataset['customdata'];

                    $( this ).dialog( "close" );
                },
                Cancel: function() {
                $( this ).dialog( "close" );
                }
            }
        });

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

    $("#edit_contraption_container")
        .dialog({
            autoOpen: false,
            height: 360,
            width: 800,
            modal: true,
            buttons: {
                "Save": function(){
                    //do the form submit
                    $("#edit_contraption_form").submit();
                    $(this).dialog("close");
                },
                Cancel: function(){
                    $(this).dialog("close");
                }
            }
        });
});
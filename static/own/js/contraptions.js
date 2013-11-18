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
    var dialog = $("#dialog-confirm")[0];
    dialog.dataset["delete_what"] = "contraption";
    dialog.dataset["delete_url"] = "section/contraptions/delete/contraption/";
    dialog.dataset["delete_id"] = id;
    $("#dialog-confirm").dialog("open");
}

function deletePage(cid, pid){
    var dialog = $("#dialog-confirm")[0];
    dialog.dataset["delete_what"] = "page";
    dialog.dataset["delete_url"] ="section/contraptions/page/delete/";
    dialog.dataset["delete_cid"] = cid;
    dialog.dataset["delete_pid"] = pid;
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
                    var delete_what     = $(this)[0].dataset["delete_what"];
                    if (delete_what == "contraption"){
                        var id          = $(this)[0].dataset["delete_id"];
                        var delete_url  = $(this)[0].dataset["delete_url"];
                        var url         = APP_SETTINGS.base_url + delete_url +"?id="+id;
                        $.getJSON(url, function(data){
                            location.reload();
                            });

                        delete $( this )[0].dataset["delete_id"];
                        delete $( this )[0].dataset["delete_url"];
                    } else if (delete_what == "page"){
                        var cid         = $(this)[0].dataset["delete_cid"];
                        var pid         = $(this)[0].dataset["delete_pid"];
                        var delete_url  = $(this)[0].dataset["delete_url"];
                        var url         = APP_SETTINGS.base_url + delete_url +"?cid="+cid+"&pid="+pid;
                        $.getJSON(url, function(data){
                            location.reload();
                            });

                        delete $( this )[0].dataset["delete_cid"];
                        delete $( this )[0].dataset["delete_pid"];
                        delete $( this )[0].dataset["delete_url"];
                        delete $( this )[0].dataset["delete_what"];
                    }

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

function togglePageVisibility(event, id){
    var plusminus_id = "plusminus_" + id;
    var plusminus = $("#plusminus_" + id)[0];

    var page_content_id = "page_content_" + id;
    var page_content = $("#"+page_content_id)[0];

    if (page_content.style.display == "none"){
        page_content.style.display = "block";
        plusminus.innerHTML = "-";
    } else {
        page_content.style.display = "none";
        plusminus.innerHTML = "+";
    }
}
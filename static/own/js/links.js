    $(document).ready(function(){
        $("#dialog").dialog({
            autoOpen: false,
            modal: true,
            buttons: {
                "confirm": function() {
                    window.location.href = targetUrl;
                },
                "cancel": function() {
                    $(this).dialog("close");
                }
            }
        });

        $("#dialog-form").dialog({
            autoOpen: false,
            height: 300,
            width: 500,
            modal: true,
            buttons: {
                "Save": function(){
                    var bJ = true
                }
            }
        });
    });

    function edit(id,url,title,comments){
        $('#linkid').value = id;
        $('#url').value = url;
        $('#dialog-form').dialog("open");
    }

    function confirm(targetUrl){
        $("#dialog").dialog("open");
    }

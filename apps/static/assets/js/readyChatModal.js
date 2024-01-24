$("#btnCloseModal").click(function() {
    
    $("#txt_question").val("");
    $("#txt_question").focus();
    $("#modal").css('display', 'none');    
})

$("#btnRephraseQuestion").click(function() {
        
    $("#txt_question").val($("#txt_question_modal").val());
    $("#txt_question").focus();
    $("#modal").css('display', 'none');    
})





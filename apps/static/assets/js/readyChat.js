// Cookie to make ajax works
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
             const cookie = cookies[i].trim();
             // Does this cookie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
             }
          }
    }
    return cookieValue;
 }



// 
$("#btnQuestion").click(function(){

    const question = $("#txt_question").val()


    console.log("Question: " + question);

    $.ajax({
        type: 'POST',
        headers: {'X-CSRFToken': getCookie("csrftoken")},    
        url: "/ready/",
        data: { 'question' : question },
        dataType: "json", 
  
        success: function (response) {            
            get_answer(JSON.parse(response))
        },
        error: function (response) {
            console.log("Fail")
        }
    })
})


// Ajax response
function get_answer(answer) {    
    $("#txt_question_modal").val($("#txt_question").val())
    $("#txt_answer_modal").val(answer['answer'])

    $("#modal").css('display','block')
}



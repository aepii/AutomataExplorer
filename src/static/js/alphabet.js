function setAlphabet(){
    var alphabet = $("#alphabetInput").val();

    $.ajax({
        type: "POST",
        url: "/",
        data: { alphabet: alphabet },
        success: function(response) {
            // Update the content on the page with the response
            $("#result1").text(response.result);
        },
        error: function(error) {
            // Handle errors
            console.error("Error:", error);
        }
    });
}

function generateStrings(length){
    var length = $("#stringLength").val();

    $.ajax({
        type: "POST",
        url: "/",
        data: { length: length },
        success: function(response) {
            // Update the content on the page with the response
            $("#result2").text(response.result);
        },
        error: function(error) {
            // Handle errors
            console.error("Error:", error);
        }
    });
}


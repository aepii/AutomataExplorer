function setAlphabet(){
    var alphabet = $("#alphabetInput").val();

    $.ajax({
        type: "POST",
        url: "/",
        data: { alphabet: alphabet },
        success: function(response) {
            // Update the content on the page with the response
            $("#result").text(response.result);
        },
        error: function(error) {
            // Handle errors
            console.error("Error:", error);
        }
    });
}


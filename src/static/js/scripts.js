function setAlphabet() {
    var alphabet = $("#alphabetInput").val();

    $.ajax({
        type: "POST",
        url: "/",
        data: {
            alphabet: alphabet
        },
        success: function (response) {
            // Update the content on the page with the response
            $("#alphabetResult").text(response.result);
        },
        error: function (error) {
            // Handle errors
            console.error("Error:", error);
        }
    });
}

function generateStrings(length) {
    var length = $("#stringLength").val();

    $.ajax({
        type: "POST",
        url: "/",
        data: {
            length: length
        },
        success: function (response) {
            // Update the content on the page with the response
            $("#stringGenerationResult").text(response.result);
        },
        error: function (error) {
            // Handle errors
            console.error("Error:", error);
        }
    });
}

function toggleFormalLang() {
    var formalLang = document.getElementById("formalLang");
    if (formalLang.style.display === "none") {
        formalLang.style.display = "block";
    } else {
        formalLang.style.display = "none";
    }
}
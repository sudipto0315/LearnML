function getBathValue() {
    let uiBathrooms = document.getElementsByName("uiBathrooms");
    for (let i of uiBathrooms) {
        if (i.checked) return parseInt(i.value);
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    let uiBHK = document.getElementsByName("uiBHK");
    for (let i of uiBHK) {
        if (i.checked) return parseInt(i.value);
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    let sqft = document.getElementById("uiSqft");
    let bhk = getBHKValue();
    let bathrooms = getBathValue();
    let location = document.getElementById("uiLocations");
    let estPrice = document.getElementById("uiEstimatedPrice");

    let url = "http://127.0.0.1:5000/predict_home_price";
    // let url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards


    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    }, function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = `<h2>${data.estimated_price} Lakh</h2>`;
        estPrice.classList.add("show");
    });
}

function onPageLoad() {
    console.log("document loaded");
    let url = "http://127.0.0.1:5000/get_location_names";
    // let url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            let locations = data.locations;
            let uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (let loc of locations) {
                $('#uiLocations').append(new Option(loc));
            }
        }
    });
}

window.onload = onPageLoad;
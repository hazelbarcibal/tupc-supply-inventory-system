$(document).ready(function() {

    $("#propertyNo").on('change', function() {
        var propertyNo = $(this).val();

        $.ajax ({
            url: '/validateInfo/',
            data: {
                'arequest_equipment_property_no': propertyNo
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    alert("Existing Property Number!")
                    $('#propertyNo').css({'border': 'solid red 1.5px'});
                    $("#propertyNo").val('');
                } else {
                    $('#propertyNo').css({'border': 'solid #3E3E3E 1.5px'});
                }
            }
        });

    });

});


$(document).ready(function() {

    $("#modelNo").on('change', function() {
        var modelNo = $(this).val();

        $.ajax ({
            url: '/validateInfo1/',
            data: {
                'arequest_equipment_model_no': modelNo
            },
            dataType: 'json',
            success: function (data1) {
                if (data1.is_taken) {
                    alert("Existing Model Number!")
                    $('#modelNo').css({'border': 'solid red 1.5px'});
                    $("#modelNo").val('');
                } else {
                    $('#modelNo').css({'border': 'solid #3E3E3E 1.5px'});
                }
            }
        });

    });

});


$(document).ready(function() {

    $("#serialNo").on('change', function() {
        var serialNo = $(this).val();

        $.ajax ({
            url: '/validateInfo2/',
            data: {
                'arequest_equipment_serial_no': serialNo
            },
            dataType: 'json',
            success: function (data2) {
                if (data2.is_taken) {
                    alert("Existing Serial Number!")
                    $('#serialNo').css({'border': 'solid red 1.5px'});
                    $("#serialNo").val('');
                } else {
                    $('#serialNo').css({'border': 'solid #3E3E3E 1.5px'});
                }
            }
        });

    });

});



const container = document.querySelector(".qrimage");

const propertyNo = document.getElementById("propertyNo");
const issuedTo = document.getElementById("issuedTo");
const itemname = document.getElementById("itemname");
const description = document.getElementById("description");
const brand = document.getElementById("brand");
const quantity = document.getElementById("quantity");
const yrAcquired = document.getElementById("yrAcquired");
const serialNo = document.getElementById("serialNo");
const modelNo = document.getElementById("modelNo");
const certifiedCorrect = document.getElementById("certified");
const dateAccepted = document.getElementById("DateAccepted");
const qrSize = document.getElementById("qrSize");

const primary = document.getElementById('formSubmit'); // hidden withdraw button
const submitBtn = document.getElementById("createBtn"); // create QR button
const downloadBtn = document.getElementById("download_link"); // download button
const sizeOptions = document.querySelector(".sizeOptions");

let QR_Code;
let sizeChoice;

//Set size
sizeOptions.addEventListener("change", () => {
    sizeChoice = sizeOptions.value;
});
  
  
  
//Format input
const inputFormatter = (value) => {
    value = value.replace(/[^a-z0-9A-Z]+/g, "");
    return value;
};


submitBtn.addEventListener("click", async () => {  //create QR btn
    //QR code generation

    if (propertyNo.value.trim().length < 1 || yrAcquired.value.trim().length < 1 ||
    modelNo.value.trim().length < 1 || serialNo.value.trim().length < 1 || certifiedCorrect.value.trim().length < 1
    || sizeOptions.value.trim() < 1 ) {
        alert('Some field/s is empty!')
    } else {
        document.getElementById('download_link').style.pointerEvents="auto";
        document.getElementById('download_link').style.cursor="pointer";
        container.innerHTML = "";
        QR_Code = await new QRCode(container, {
            text: "Property No: " + propertyNo.value + ' ' + 'Issued To: ' + issuedTo.value + '\n'
            + 'Itemname: ' + itemname.value + '\n' + 'Description: ' + description.value + '\n'
            + 'Brand: ' + brand.value + '\n' + 'Model No: ' + modelNo.value + '\n' + 'Serial No: ' + serialNo.value 
            + '\n' + 'Date: ' + dateAccepted.value,
            width: sizeChoice,
            height: sizeChoice,
            
        });
    }

});


function pressBtn() {

    if (propertyNo.value.trim().length < 1 || yrAcquired.value.trim().length < 1 ||
    modelNo.value.trim().length < 1 || serialNo.value.trim().length < 1 || certifiedCorrect.value.trim().length < 1
    || sizeOptions.value.trim() < 1 ) {
        alert('Some field/s is empty!')
    } else {
        // primary.click();
        
        // alert('withdraw button clicked!');
        const src = container.firstChild.toDataURL("image/png"); // Set url for download
        downloadBtn.href = src;
        let userValue = issuedTo.value + '_' + propertyNo.value;
        // userValue = inputFormatter(userValue);
        downloadBtn.download = `${userValue}`;
        setTimeout('getstatus()', 10000);
        document.getElementById('download_link').style.pointerEvents="none";
        document.getElementById('download_link').style.cursor="default";

    }
    

}

function getstatus() {
    primary.click();
    // alert('withdraw button clicked!');
}



window.onload = () => {
    container.innerHTML = "";
    sizeChoice = 100;
    sizeOptions.value = 100;
    propertyNo.value = "";
    yrAcquired.value = "";
    serialNo.value = "";
    modelNo.value = "";
    certifiedCorrect.value = "";

    document.getElementById('download_link').style.pointerEvents="none";
    document.getElementById('download_link').style.cursor="default";

};
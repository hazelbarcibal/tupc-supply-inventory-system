qrItemName = document.getElementById('itemname');
qrUnit = document.getElementById('unit');
qrColor = document.getElementById('colorInput');
qrType = document.getElementById('typeInput');


const qrCode = new QRCodeStyling({
  width: 200,
  height: 200,
  data: "Please enter data and then try to scan me.",
  image: "",
  dotsOptions: {
    color: "#000",
    type: "square"
  },
});

const updateQrItemName = () => {
  newQrData = qrItemName.value;
  qrCode.update({
    data: newQrData
  });
};

const updateQrUnit = () => {
  newQrData =  "Item name: " + qrItemName.value + " Unit: " + qrUnit.value;
  qrCode.update({
    data: newQrData
  });
};



const updateQrColor = () => {
  newQrColor = qrColor.value;
  qrCode.update({
    dotsOptions: {
      color: newQrColor
    }
  });
};

const updateQrType = () => {
  newQrType = qrType.value;
  qrCode.update({
    dotsOptions: {
      type: newQrType
    }
  });
};

const download = () => qrCode.download("jpeg");

//function download(){
//  x = document.getElementById('itemname').value;
//  y = document.getElementById('unit').value;
//  if (x || y == ''){
//    alert('Please enter QR details.');
//  } 
//  else qrCode.download('jpeg');

//}

//function validateForm() {
   
//  let x = document.forms["qrForm"]["dataInput"].value;
//    if (x == "") {
//        alert("Please enter all given QR code informations.");
//        return false;
//    }
    
//}

qrCode.append(document.getElementById('canvas'));
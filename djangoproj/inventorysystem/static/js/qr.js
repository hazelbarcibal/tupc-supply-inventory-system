qrItemName = document.getElementById('itemname');
qrUnit = document.getElementById('unit');
qrColor = document.getElementById('colorInput');
qrType = document.getElementById('typeInput');


const qrCode = new QRCodeStyling({
  width: 200,
  height: 200,
  data: "Please enter the data and then try to scan me.",
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

qrCode.append(document.getElementById('canvas'));
qrData = document.getElementById('dataInput');
qrUnit = document.getElementById('unit');


const qrCode = new QRCodeStyling({
  width: 300,
  height: 300,
  data: "Please enter the data and then try to scan me.",
  image: "",
  dotsOptions: {
    color: "#000",
    type: "square"
  },
});

const updateQrItemName = () => {
  newQrData = qrData.value;
  qrCode.update({
    data: newQrData
  });
};
const updateQrUnit = () => {
  newQrData = qrData.value + '\n' + qrUnit.value;
  qrCode.update({
    data: newQrData
  });
};




const download = () => qrCode.download("jpeg");

qrCode.append(document.getElementById('canvas'));
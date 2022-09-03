//upload qr ui script
const wrapper = document.querySelector(".wrapper"),
form = document.querySelector("form"),
fileInp = form.querySelector("input"),
infoText = form.querySelector("p"),
closeBtn = document.querySelector(".close"),
copyBtn = document.querySelector(".copy");
function fetchRequest(file, formData) {
    infoText.innerText = "Scanning QR Code...";
    fetch("http://api.qrserver.com/v1/read-qr-code/", {
        method: 'POST', body: formData
    }).then(res => res.json()).then(result => {
        result = result[0].symbol[0].data;
        infoText.innerText = result ? "Upload QR Code to Scan" : "Couldn't scan QR Code";
        if(!result) return;
        document.querySelector("textarea").innerText = result;
        form.querySelector("img").src = URL.createObjectURL(file);
        wrapper.classList.add("active");
    }).catch(() => {
        infoText.innerText = "Couldn't scan QR Code";
    });
}
fileInp.addEventListener("change", async e => {
    let file = e.target.files[0];
    if(!file) return;
    let formData = new FormData();
    formData.append('file', file);
    fetchRequest(file, formData);
});
copyBtn.addEventListener("click", () => {
    let text = document.querySelector("textarea").textContent;
    navigator.clipboard.writeText(text);
});
form.addEventListener("click", () => fileInp.click());
closeBtn.addEventListener("click", () => wrapper.classList.remove("active"));

//form modal script
function getValue(){
    var x = document.getElementById('text').value;
    var word = x.split(' ');

    let len = word.length;

    if (len == 5){
        document.getElementById('itemVal').value = (word[2]);
        document.getElementById('unitVal').value = (word[4]);
    } else if (len == 6) {
        document.getElementById('itemVal').value = (word[2] + ' ' + word[3]);
        document.getElementById('unitVal').value = (word[5]);
    } else if (len == 7) {
        document.getElementById('itemVal').value = (word[2] + ' ' + word[3] + ' ' + word[4]);
        document.getElementById('unitVal').value = (word[6]);
    } else if (len == 8) {
        document.getElementById('itemVal').value = (word[2] + ' ' + word[3] + ' ' + word[4] + ' ' + word[5]);
        document.getElementById('unitVal').value = (word[7]);
    } else if (len == 9) {
        document.getElementById('itemVal').value = (word[2] + ' ' + word[3] + ' ' + word[4] + ' ' + word[5] + ' ' + word[6]);
        document.getElementById('unitVal').value = (word[8]);
    } else if (len == 10) {
        document.getElementById('itemVal').value = (word[2] + ' ' + word[3] + ' ' + word[4] + ' ' + word[5] + ' ' + word[6] + ' ' + word[7]);
        document.getElementById('unitVal').value = (word[9]);
    } else if (len == 11) {
        document.getElementById('itemVal').value = (word[2] + ' ' + word[3] + ' ' + word[4] + ' ' + word[5] + ' ' + word[6] + ' ' + word[7] + ' ' + word[8]);
        document.getElementById('unitVal').value = (word[10]);
    } else if (len == 12) {
        document.getElementById('itemVal').value = (word[2] + ' ' + word[3] + ' ' + word[4] + ' ' + word[5] + ' ' + word[6] + ' ' + word[7] + ' ' + word[8] + ' ' + word[9]);
        document.getElementById('unitVal').value = (word[11]);
    } 
    
} 
let video = document.querySelector("#video");
let click_button = document.querySelector("#click-photo");
let canvas = document.querySelector("#canvas");
let result = document.querySelector("#result");

async function onLoad() {
    let stream = await navigator.mediaDevices.getUserMedia({
        video: {
            facingMode: 'environment'
        }, audio: false
    });
    video.srcObject = stream;
};

click_button.addEventListener('click', function () {
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    let image_data_url = canvas.toDataURL('image/jpeg');

    calculate(image_data_url)
});

async function calculate(strIm) {
    let data = new FormData();
    data.append("image", strIm);

    try {
        let response = await fetch("/calculate", { method: "post", body: data })
        if (response.statusText != "OK")
            throw response.statusText;

        let jsonResult = await response.text();
        jsonResult = JSON.parse(jsonResult);

        result.textContent = jsonResult.result;
    }
    catch (error) {
        alert("Error processing the image: " + error);
    }
}

window.addEventListener('load', onLoad);
document.addEventListener("DOMContentLoaded", function() {

    const host = '127.0.0.1';

    const socketFramesenderInfocen = new WebSocket('ws://'+host+':8000/framesender/infocen/');
    const demoInfocen = document.getElementById("DemoInfocen")

    const socketFramesenderUnet = new WebSocket('ws://'+host+':8000/framesender/unet/');
    const demoUnet = document.getElementById("DemoUnet")

    const socketFramesenderASR = new WebSocket('ws://'+host+':8000/framesender/asr/');
    const demoASR = document.getElementById("DemoASR")


    // let currentFrameInfocen = null;
    //Infocen
    socketFramesenderInfocen.onmessage = function(event) {
        const imageUrl = URL.createObjectURL(event.data);
        demoInfocen.src = imageUrl;
    };
    //Unet
    socketFramesenderUnet.onmessage = function(event) {
        const imageUrl = URL.createObjectURL(event.data);
        demoUnet.src = imageUrl;
    };
    //ASR
    socketFramesenderASR.onmessage = function(event) {
        const imageUrl = URL.createObjectURL(event.data);
        demoASR.src = imageUrl;
    };
});
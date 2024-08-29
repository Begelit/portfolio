document.addEventListener("DOMContentLoaded", function() {

    const host = '127.0.0.1';
    const socketFramesenderInfocen = new WebSocket('ws://'+host+':8001/framesender/infocen/');
    const demoInfocen = document.getElementById("DemoInfocen")


    let currentFrameInfocen = null;
    socketFramesenderInfocen.onmessage = function(event) {
        // console.log(event.data)
        const imageUrl = URL.createObjectURL(event.data);
        // console.log(imageUrl)
        demoInfocen.src = imageUrl;
    };
});
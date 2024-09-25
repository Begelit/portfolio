// document.addEventListener("DOMContentLoaded", function() {

//     // const host = '192.168.9.207';
//     const host = '127.0.0.1';


//     const socketFramesenderInfocen = new WebSocket('ws://'+host+':8000/framesender/infocen/');
//     const demoInfocen = document.getElementById("DemoInfocen")

//     const socketFramesenderUnet = new WebSocket('ws://'+host+':8000/framesender/unet/');
//     const demoUnet = document.getElementById("DemoUnet")

//     const socketFramesenderASR = new WebSocket('ws://'+host+':8000/framesender/asr/');
//     const demoASR = document.getElementById("DemoASR")

//     const socketFramesenderCV = new WebSocket('ws://'+host+':8000/framesender/cv/');
//     const demoCV = document.getElementById("DemoCV")

//     const socketFramesenderLLM = new WebSocket('ws://'+host+':8000/framesender/llm/');
//     const DemoLLM = document.getElementById("DemoLLM")

//     //Infocen
//     socketFramesenderInfocen.onmessage = function(event) {
//         const imageUrl = URL.createObjectURL(event.data);
//         demoInfocen.src = imageUrl;
//     };
//     //Unet
//     socketFramesenderUnet.onmessage = function(event) {
//         const imageUrl = URL.createObjectURL(event.data);
//         demoUnet.src = imageUrl;
//     };
//     //ASR
//     socketFramesenderASR.onmessage = function(event) {
//         const imageUrl = URL.createObjectURL(event.data);
//         demoASR.src = imageUrl;
//     };
//     CV
//     socketFramesenderCV.onmessage = function(event) {
//         const imageUrl = URL.createObjectURL(event.data);
//         demoCV.src = imageUrl;
//     };
//     LLM
//     socketFramesenderLLM.onmessage = function(event) {
//         const imageUrl = URL.createObjectURL(event.data);
//         DemoLLM.src = imageUrl;
//     };
// });
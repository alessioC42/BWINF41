var socket = io();
        
const SVG = document.getElementById("svg");
const LEN = document.getElementById("lenght");
const TOTALPATHS = document.getElementById("paths_total")

const SVG_LIVE = document.getElementById("svg_live")


socket.on('newBestSVG', (data) => {
    SVG.innerHTML = data.data;
    LEN.innerText = data.lenght;
});

socket.on('pathCoundUpdate', (data) => {
    SVG_LIVE.innerHTML = data.data;
    TOTALPATHS.innerText = data.paths_total;
})

socket.on('finished', (data) => {
    alert(data.message)
})
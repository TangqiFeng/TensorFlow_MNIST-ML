function saveImage() {
    var canvas = document.getElementById('canvas');
    // Convert canvas image to URL format (base64)
    var dataURL = canvas.toDataURL();
    
    $.ajax({
      type: "POST",
      url: "http://localhost:5000/",
      data:{
        imageBase64: dataURL
      },
      dataType:"json",
      success: (data) => {
        var label=document.getElementById("guessNum"); 
        label.innerText=data;
        console.log(data);
      }
    });  
}

// draw image 
context = document.getElementById('canvas').getContext("2d");
var flag = true;
// Mouse Down Event
$('#canvas').mousedown(function(e){
var mouseX = e.pageX - this.offsetLeft;
var mouseY = e.pageY - this.offsetTop;        
paint = true;
if(flag){
    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
    redraw();
}

});
// Mouse Move Event
$('#canvas').mousemove(function(e){
    if(paint){
        addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
        redraw();
    }
});
// Mouse Up Event
$('#canvas').mouseup(function(e){
    paint = false;
});
// Mouse Leave Event
$('#canvas').mouseleave(function(e){
    paint = false;
});

var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint;
// save the mouse click position
function addClick(x, y, dragging)
{
    clickX.push(x);
    clickY.push(y);
    clickDrag.push(dragging);
}
// Each time the function is called the canvas is cleared and everything is redrawn.
function redraw(){
    context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas
    
    context.strokeStyle = "blue";
    context.lineJoin = "round";
    context.lineWidth = 30;
                
    for(var i=0; i < clickX.length; i++) {		
        context.beginPath();
        if(clickDrag[i] && i){
        context.moveTo(clickX[i-1], clickY[i-1]);
        }else{
        context.moveTo(clickX[i]-1, clickY[i]);
        }
        context.lineTo(clickX[i], clickY[i]);
        context.closePath();
        context.stroke();
    }
}

// clear the canvas
$("#clear").on('click', function () {
    context.clearRect(0, 0, canvas.width, canvas.height);
    clickX = new Array();
    clickY = new Array();
    clickDrag = new Array();
    var label=document.getElementById("guessNum"); 
    label.innerText="";
});
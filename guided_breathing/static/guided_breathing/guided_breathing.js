// Get dimensions for animation
headerHeight = document.getElementById("header").clientHeight
promptHeight = document.getElementById("prompt").clientHeight
divWidth = document.getElementById("canvas").clientWidth
w = divWidth;
h = window.innerHeight - headerHeight - promptHeight;
maxR = 0.2 * Math.min(w, h);
minR = 0.3 * maxR;
var canvas = SVG('canvas').size(w, h);

var cycleLength = 4000;
var finalCycleLength = 4400;
var numCycles = 4;
var fullColor = '#30aa60';
var emptyColor =  '#d0d0d0';
var breathingCircle = canvas.circle(minR).attr({fill: emptyColor, cx: w/2, cy: h/3})

function startBreathCycle()
{
  cycleLength = 4000;
  finalCycleLength = 4400;
  numCycles = 2;
  hideButtons();
  breathCycle();
}

function breathCycle()
{
  if(finalCycleLength - cycleLength > 50)
  {
    cycleLength += 50;
  }
  if(numCycles > 0)
  {
    breathingCircle.animate(cycleLength / 2, '<>').attr({r: maxR, fill: fullColor}).animate(cycleLength / 2, '<>').attr({r: minR, fill: emptyColor});
    numCycles -= 1;
    breathCycle();
  }
  else {
    breathingCircle.animate(cycleLength / 2, '<>').attr({r: maxR, fill: fullColor}).animate(cycleLength / 2, '<>').attr({r: minR, fill: emptyColor}).after(showButtons);
  }
}


function showButtons()
{
  var buttonDiv = document.getElementById("buttons");
  buttonDiv.style.visibility = "visible";
}

function hideButtons()
{
  var buttonDiv = document.getElementById("buttons");
  buttonDiv.style.visibility = "hidden";
}

startBreathCycle();

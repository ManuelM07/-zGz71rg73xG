function setup() {
  createCanvas(1360, 750, WEBGL);
}

// coordenadas
let x = 120
let y = 280
let z = 0 // Dejar en 0 en caso de querer dibujar un vector en R2

// En R1 solo se maneja un vector a la vez 
let vectorsR2 = [[100, 200], [50, 70], [-200, -70]] // Agregue o elimine los vectores en R3 que desee probar
let vectorsR3 = [[100, 200, 300], [50, 70, 45], [-200, -70, -120]] // Agregue o elimine los vectores en R3 que desee probar

function draw() {
  background(200, 200, 200);
  r2() // Invocar la función que se desea ejecutar r1, r2 o r3
}

function r1(x) {
  //X - positive
  stroke(192,0,0);
  line(0,0,0,-680,0,0);
  //X - negative
  stroke(192,0,0);
  line(0,0,0,680,0,0);

  circle(0, 0, 10);

  //vector
  push();
  stroke(0,0,0);
  strokeWeight(4);
  line(0,0,x,0);
  pop();

  triangle(x, 7, x*1.1, 0, x, -7)
}

function r2(x, y) {
  //X - positive
  stroke(192,0,0);
  line(0,0,0,-680,0,0);
  //X - negative
  stroke(192,0,0);
  line(0,0,0,680,0,0);

  //Y - green - positive
  stroke(0,192,0);
  line(0,0,0,0,-375,0);
  //Y - green - negative
  stroke(0,192,0);
  line(0,0,0,0,375,0);

    //vectors
    vectorsR2.forEach(l => makeVector(l[0], -l[1]))
}

function r3(){
  rotateX(map(mouseY,0,height,-PI,PI));
  rotateY(map(mouseX,0,width,PI,-PI));

  //X - positive
  stroke(192,0,0);
  line(0,0,0,-680,0,0);
  //X - negative
  stroke(192,0,0);
  line(0,0,0,680,0,0);

  //Y - green - positive
  stroke(0,192,0);
  line(0,0,0,0,-375,0);
  //Y - green - negative
  stroke(0,192,0);
  line(0,0,0,0,375,0);

  //Z - blue - positive
  stroke(0,0,192);
  line(0,0,0,0,0,-400);
  //Z - blue - negative
  stroke(0,0,192);
  line(0,0,0,0,0,400);

  //vectors
  vectorsR3.forEach(l => makeVector(-l[0], l[1], l[2])) 
}

function makeVector(x, y=0, z=0) {
  push();
  stroke(0,0,0);
  strokeWeight(4);
  line(0,0,0,x,y,z);
  pop();
}
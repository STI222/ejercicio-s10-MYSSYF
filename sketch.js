function preload() {
  tabla = loadTable('../inf.csv', 'csv')
}

function setup() {
  createCanvas(1500, 1100);
  sel = createSelect();
  sel.position(10, 10);
  sel.option('fernan');
  sel.option('bloku');
  sel.option('plokun');
  sel.option('ayleen');
  sel.selected('fernan');
  sel.changed(mySelectEvent);

  t = ""
  fernan = tabla.getColumn(1)
  bloku = tabla.getColumn(2)
  plokun = tabla.getColumn(3)
  ayleen = tabla.getColumn(4)


    s1 = createSlider(1, 100, 1);
    s1.position(130, 10);
    s1.style('width', '100px');

    s2 = createSlider(1, 100, 1);
    s2.position(260, 10);
    s2.style('width', '100px');

    s3 = createSlider(1, 100, 1);
    s3.position(390, 10);
    s3.style('width', '100px');

    s4 = createSlider(1, 100, 1);
    s4.position(510, 10);
    s4.style('width', '100px');
  
    piedra=0
    papel=0
    tijera=0
    pistol=0

  textAlign(CENTER);
  textSize(50);


}

function draw() {
  background(220);
  background(120,230,130)

  textSize(20)

piedra=s1.value()
text("piedra",170,40)

papel=s2.value()
text("papel",290,40)

tiejra=s3.value()
text("tijera",410,40)

pistol=s4.value()
text("pistola",530,40)



  switch (t) {
    case "fernan":
      x = 100
      y = 100
      r = 100
      circle(x, y, r)
      text(t, x, y + 80)
      color(255)

      circle(x + comparar(fernan, bloku), y + 100, r)
      text("bloku", x + comparar(fernan, bloku), y + 180)
      circle(x + comparar(fernan, plokun), y + 300, r)
      text("plokun", x + comparar(fernan, plokun), y + 380)
      circle(x + comparar(fernan, ayleen), y + 500, r)
      text("ayleen", x + comparar(fernan, ayleen), y + 580)
      color(0)

      break;
    case "bloku":
      x = 100
      y = 100
      r = 100
      circle(x, y, r)
      text(t, x, y + 80)
      color(255)

      circle(x +comparar(bloku, fernan), y + 100, r)
      text("fernan", x +comparar(bloku, fernan), y + 180)
      circle(x +  comparar(bloku, plokun), y + 300, r)
      text("plokun", x + comparar(bloku, plokun), y + 380)
      circle(x +  comparar(bloku, ayleen) , y + 500, r)
      text("ayleen", x +  comparar(bloku, ayleen), y + 580)
      
     
    
      break;
    case "plokun":
      x = 100
      y = 100
      r = 100
      circle(x, y, r)
      text(t, x, y + 80)
      color(255)

      circle(x + comparar(plokun, fernan), y + 100, r)
      text("fernan", x +comparar(plokun, fernan), y + 180)
      circle(x +    comparar(plokun, bloku), y + 300, r)
      text("bloku", x +   comparar(plokun, bloku), y + 380)
      circle(x +    comparar(plokun, ayleen), y + 500, r)
      text("ayleen", x +   comparar(plokun, ayleen),y + 580)
      
   
   
      break;
    case "ayleen":
      x = 100
      y = 100
      r = 100
      circle(x, y, r)
      text(t, x, y + 80)
      color(255)

      circle(x + comparar(ayleen, fernan), y + 100, r)
      text("fernan", x +comparar(ayleen, fernan), y + 180)
      circle(x +comparar(ayleen, bloku) , y + 300, r)
      text("bloku", x +comparar(ayleen, bloku), y + 380)
      circle(x + comparar(ayleen, plokun), y + 500, r)
      text("plokun", x +comparar(ayleen, plokun), y + 580)
      
      
      
      break;

    default:
      break;
  }

}

function comparar(z, y) {

  ab = int(((z[1]*piedra) * (y[1]*piedra)) + ((z[2]*papel) * (y[2]*papel)) + ((z[3]*tiejra) * (y[3]*tijera)) + ((z[4]*pistol) * (y[4]*pistol)))
  af = int(sqrt(((z[1]*piedra) ** 2) + ((z[2]*papel) ** 2) + ((z[3]*tiejra) ** 2) + ((z[4]*pistol) ** 2)))
  bf = int(sqrt(((y[1]*piedra )** 2) + ((y[2]*papel) ** 2) + ((y[3]*tijera) ** 2) + ((y[4]*pistol) ** 2)))

  zi = (ab / (af * bf)) * 700
console.log(zi)
  return zi


}

function mostrar(t) {




}

function mySelectEvent() {
  let item = sel.value();
  t = item

}



// participantes de esta iteracion rara del sprint 2
// jose gabriel gonzalez lucumi
// Estiven Reyes Rodriguez
// Natalia Martinez
// Nicolas Sánchez

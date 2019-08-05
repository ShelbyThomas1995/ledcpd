<?php
   $rackID = $_GET['id'];
   $mode = $_GET['mode'];

   $fecha = date("d/m/Y");
   $hora = date("h:i:sa");
   $info = $rackID . "*ha*sido*modificado*desde*la*aplicacion*web*al*estado:*" . $mode;
   echo shell_exec("sudo python /var/www/html/prueba.py $rackID $mode $fecha $hora $info");
   echo "<br>";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Control Led CPD</title>
        <meta charset="UTF-8">
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="./style.css" type="text/css" media="all">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
    </head>

<style>
.cajaRack {
  border: 5px solid black;
  border-radius: 5px 5px 5px 5px;
  margin-left: 20px;
  background-image: url('servidores.png');
  width: 60px;
  height: 130px;
  background-repeat: no-repeat;
  background-size: cover;
}

.divCenter {
   width:  400px;
   height: 130px;
   margin: 0 auto;
   text-align: center;
}

.divCajaRack {
   width: 100px;
   height: 130px;
   float: left;
}

span{
 line-height:normal;
 font-size:11px;
 display:table-caption;
 margin:0;
 margin-top: 77px;
 background:#646464;
 color:white;
 font-style:italic;
 padding:5px;
 text-align:center;
 width: 49.8px;
}

.boton {
  width: 20px;
  height: 20px;
  background:#646464;
  color:white;
}

textarea {
  margin-top: 10px;
  resize: none;
}

</style>
   <body>
     <div class="container-fluid">
      <h2 align="center"> <strong>  Control LED CPD </strong> </h2>

       <div class="row">
	<div align="center"  class="col-lg-12">

	<div class="divCenter">

	 <div class="divCajaRack">
	  <div class="cajaRack" id="rack0">
           <span>Rack 0</span>
            <select class="boton" onchange="window['seleccion'](this.value);">
             <option></option>
             <option value="rack0 on">Encender/OK</option>
             <option value="rack0 off">Apagar</option>
             <option value="rack0 error">Notificar Error</option>
             <option value="rack0 tecnico">Notificar Técnico</option>
             <option value="rack0 log">Mostrar Log</option>
	    </select>
          </div>
	 </div>

         <div class="divCajaRack">
          <div class="cajaRack" id="rack1">
           <span>Rack 1</span>
            <select class="boton" onchange="window['seleccion'](this.value);">
             <option></option>
             <option value="rack1 on">Encender/OK</option>
             <option value="rack1 off">Apagar</option>
             <option value="rack1 error">Notificar Error</option>
             <option value="rack1 tecnico">Notificar Técnico</option>
             <option value="rack1 log">Mostrar Log</option>
            </select>
          </div>
         </div>

         <div class="divCajaRack">
          <div class="cajaRack" id="rack2">
           <span>Rack 2</span>
            <select class="boton" onchange="window['seleccion'](this.value);">
             <option></option>
             <option value="rack2 on">Encender/OK</option>
             <option value="rack2 off">Apagar</option>
             <option value="rack2 error">Notificar Error</option>
             <option value="rack2 tecnico">Notificar Técnico</option>
             <option value="rack2 log">Mostrar Log</option>
            </select>
          </div>
         </div>

         <div class="divCajaRack">
          <div class="cajaRack" id="rack3">
           <span>Rack 3</span>
            <select class="boton" onchange="window['seleccion'](this.value);">
             <option></option>
             <option value="rack3 on">Encender/OK</option>
             <option value="rack3 off">Apagar</option>
             <option value="rack3 error">Notificar Error</option>
             <option value="rack3 tecnico">Notificar Técnico</option>
             <option value="rack3 log">Mostrar Log</option>
            </select>
          </div>
         </div>
	</div>

        <div class="row">
         <div class="col-lg-12">

	 <div class="divCenter" style="margin-top: 10px;">

         <div class="divCajaRack">
          <div class="cajaRack" id="rack4">
           <span>Rack 4</span>
            <select class="boton" onchange="window['seleccion'](this.value);">
             <option></option>
             <option value="rack4 on">Encender/OK</option>
             <option value="rack4 off">Apagar</option>
             <option value="rack4 error">Notificar Error</option>
             <option value="rack4 tecnico">Notificar Técnico</option>
             <option value="rack4 log">Mostrar Log</option>
            </select>
          </div>
         </div>

         <div class="divCajaRack">
          <div class="cajaRack" id="rack5">
           <span>Rack 5</span>
            <select class="boton" onchange="window['seleccion'](this.value);">
             <option></option>
             <option value="rack5 on">Encender/OK</option>
             <option value="rack5 off">Apagar</option>
             <option value="rack5 error">Notificar Error</option>
             <option value="rack5 tecnico">Notificar Técnico</option>
             <option value="rack5 log">Mostrar Log</option>
            </select>
          </div>
         </div>

         <div class="divCajaRack">
          <div class="cajaRack" id="rack6">
           <span>Rack 6</span>
            <select class="boton" onchange="window['seleccion'](this.value);">
             <option></option>
             <option value="rack6 on">Encender/OK</option>
             <option value="rack6 off">Apagar</option>
             <option value="rack6 error">Notificar Error</option>
             <option value="rack6 tecnico">Notificar Técnico</option>
             <option value="rack6 log">Mostrar Log</option>
            </select>
          </div>
         </div>

         <div class="divCajaRack">
          <div class="cajaRack" id="rack7">
           <span>Rack 7</span>
            <select class="boton" onchange="window['seleccion'](this.value);">
             <option></option>
             <option value="rack7 on">Encender/OK</option>
             <option value="rack7 off">Apagar</option>
             <option value="rack7 error">Notificar Error</option>
             <option value="rack7 tecnico">Notificar Técnico</option>
             <option value="rack7 log">Mostrar Log</option>
            </select>
          </div>
         </div>

	 </div>
	 </div>
	</div>


        <div class="row">
         <div class="col-lg-12">
          <textarea id="logHistorico" readonly  rows="9" cols="65"></textarea>
         </div>
        </div>

	</div>
	</div>
     </div>

<?php
$lista = shell_exec("sudo python /var/www/html/getEstados.py");
$replace = array("[","]","'",",");
$new = array("","","","");
$newphrase = str_replace($replace, $new, $lista);
$newLista = preg_split("/[s,]+/", $newphrase);
$racks = explode(" ", $newLista[0]);

$longitud = count($racks);
for($i=0; $i < $longitud; $i=$i+2) {

  if ($racks[$i+1] == 'off') {
    echo '<script type="text/javascript">'
       , 'document.getElementById("'
       , $racks[$i]
       , '").style.border = "5px solid #3A3A39";'
       , '</script>';
  }elseif ($racks[$i+1] == 'on') {
    echo '<script type="text/javascript">'
       , 'document.getElementById("'
       , $racks[$i]
       , '").style.border = "5px solid #399BF1";'
       , '</script>';
  }elseif ($racks[$i+1] == 'error') {
    echo '<script type="text/javascript">'
       , 'document.getElementById("'
       , $racks[$i]
       , '").style.border = "5px solid #D22525";'
       , '</script>';
  }elseif ($racks[$i+1] == 'tecnico') {
    echo '<script type="text/javascript">'
       , 'document.getElementById("'
       , $racks[$i]
       , '").style.border = "5px solid #D3D3CE";'
       , '</script>';
  }
}

   $rackIDLog = $_GET['getlog'];
   if(!is_null($rackIDLog)) {
      $log = shell_exec("sudo python /var/www/html/getHistorico.py $rackIDLog");

      $replace = array("[","]","'");
      $new = array("","","");
      $newlistalog = str_replace($replace, $new, $log);
      $newlog = preg_split("/[\n]+/", $newlistalog);
      $listlog = preg_split("/[,]+/", $newlog[0]);

      $long = count($listlog);
      for ($j=0; $j<$long; $j=$j+1) {
        if($j%5 == 0 && $j != 0) {
	 echo '<script type="text/javascript">'
         , 'document.getElementById("logHistorico").value +="'
         , $listlog[$j]
         , '\n";'
	 , 'document.getElementById("logHistorico").scrollTop = document.getElementById("logHistorico").scrollHeight;</script>';
	}
       echo '<script type="text/javascript">'
         , 'document.getElementById("logHistorico").value +="\n '
	 , $listlog[$j]
         , '";'
	 , 'document.getElementById("logHistorico").scrollTop = document.getElementById("logHistorico").scrollHeight;</script>';
       }
   } else {
      echo '<script type="text/javascript">'
         , 'document.getElementById("logHistorico").value = "";'
         , '</script>';
   }

?>

<script type="text/javascript">
function seleccion(mode) {
    res = mode.split(" ");

    if (res[1] == "log") {
      window.location.href='?getlog=' + res[0];
    } else {
      window.location.href='?id=' + res[0] + '&mode=' + res[1];
    }
}
</script>

 </body>
</html>

<!doctype html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="estilo.css" />
        <script>
            function ajaxRequest()
            {
                try //no es IE
                {
                    var request = new XMLHttpRequest();
                }
                catch (e1)
                {
                    try // IE 6+?
                    {
                        request = new ActiveXObject("Msxml2.XMLHTTP");
                    }
                    catch (e2)
                    {
                        try // IE 5?
                        {
                            request = new ActiveXObject("Microsoft.XMLHTTP");
                        }
                        catch (e3) // No soporta Ajax
                        {
                            request = false;
                        }
                    }
                }
                return request;
            }

            function consultar(dato) {
                if (dato == 1) {
                    request = new ajaxRequest();
                    request.open("GET", "consulta.php?dato=temp", true);
                    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                    request.setRequestHeader("Connection", "close");
                    request.send();

                    request.onreadystatechange = function ()
                    {
                        if (this.readyState == 4) // 4: completo
                        {
                            if (this.status == 200) // 200: resultado ok
                            {
                                if (this.responseText != null)
                                {
                                    document.getElementById('temp').innerHTML =
                                            this.responseText.substr(6, 9) + this.responseText.substr(34, 14)  ;

                                    setTimeout('consultar( 2 )', 5000);
                                }
                                else
                                    alert("Hubo un error actualizando datos");
                            }
                            else
                                alert("No se pudo acceder a los datos: " + this.statusText);
                        }
                    }
                } else {

                    request = new ajaxRequest();
                    request.open("GET", "consulta.php?dato=cant", true);
                    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                    request.setRequestHeader("Connection", "close");
                    request.send();

                    request.onreadystatechange = function ()
                    {
                        if (this.readyState == 4) // 4: completo
                        {
                            if (this.status == 200) // 200: resultado ok
                            {
                                if (this.responseText != null)
                                {
                                    if (this.responseText >= 200)
                                        col = 'red';
                                    else 
					if (this.responseText <= 100)
					  col = 'green';
					else
					  col = 'yellow';
//                                     document.getElementById('barra').style.backgroundColor = col;
//                                     document.getElementById('barra').style.width = this.responseText.slice(0, -2) + 'px';
//                                     document.getElementById('barra').innerHTML = this.responseText;

                                    //document.getElementById('bola').style.marginLeft = this.responseText.slice(0, -2) + 'px';
                                    
                                    setTimeout('consultar( 1 )', 5000);
                                }
                                else
                                    alert("Hubo un error actualizando datos");
                            }
                            else
                                alert("No se pudo acceder a los datos: " + this.statusText);
                        }
                    }
                }
            }



            function segundos( ) {


                request = new ajaxRequest();
                request.open("GET", "consulta.php?dato=seg", true);
                request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                request.setRequestHeader("Connection", "close");
                request.send();

                request.onreadystatechange = function ()
                {
                    if (this.readyState == 4) // 4: completo
                    {
                        if (this.status == 200) // 200: resultado ok
                        {
                            if (this.responseText != null)
                            {
                                document.getElementById('seg').innerHTML = this.responseText;
                                setTimeout('segundos( 500 )', 500);
                            }
                            else
                                alert("Hubo un error actualizando datos");
                        }
                        else
                            alert("No se pudo acceder a los datos: " + this.statusText);
                    }
                }
            }

        </script>

    </head>
    <body>
        <div id="header">
            <!--<div id="bola"></div>-->
        </div>
        <div id="todo">
            <div id="titulo">
                <br /><br />
                <!--temperatura 1:<br /><br />
                temperatura 2:<br /><br />
                temperatura 3:<br /><br />-->
            </div> 
            <div id="temp">

            </div>
            <div id="seg">

            </div>
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
             <div id="barra"></div>  

        </div>

        <script>
            consultar(1);
            segundos();

        </script>



    </body>
</html>

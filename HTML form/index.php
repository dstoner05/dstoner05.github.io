<!DOCTYPE html>
<html lang = "en"></html>

<script type="type/javascript" src="index.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<?php
$action = $_GET["action"];
$myText = $_POST["mytext"];

if($action = "save") {
  $targetFolder = "./text.txt";
  file_put_contents($targetFolder."text.txt", $myText);
}
?>   
	
<head>
    <title>Pre Trip Inspection</title>
    <link rel="stylesheet" type="text/css" href="./styles.css">
</head>

<body>
    <div class="wrapper">
        <div class="page_header">
            <div class="Title">
                <div class="words">    
                    <h1>Pre-Trip Inspection</h1>
                </div>
            </div>
            <div class="img">
                <img src = "itcurves.jpg" width = 350 height = "84"></img>
            </div>
        </div>
        <div class="container1">
            <div class="header">
                <h2>Item</h2>
            </div>
            <div class="Pass">
                <h2>Pass</h2>
            </div>
            <div class="Fail">
                <h2>Fail</h2>
            </div>
                
            
        </div>
        <form action="?action=save" name="myform" method="post">
            <script>
                $(document).ready(function(){
                    $('.True').click(function() {
                        $('.True').not(this).prop('checked', false);
                    });
                });
            </script>
            <div class="container">
                <div class="header">
                    <h3>Master Switch On</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q1" name="q1" style="height:20px; width:20px;" onclick="selectOnlyThis(this.pass)">
                    <label for="q1"></label><br>
                </div>
                <div class="Fail">
                    <input type = "checkbox" id = "q1.1" name= "q1.1" style="height:20px; width:20px;" onclick="selectOnlyThis(this.fail)">
                    <label for="q1.1"></label>
                </div> 
            </div>
            <div class="container">
                <div class="header">
                    <h3>Headlights(High & Low Beams)</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q2" name="q2" style="height:20px; width:20px;">
                    <label for="q2"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q2.1" name="q2.1" style="height:20px; width:20px;">
                    <label for="q2"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Turn Signals</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q3" name="q3" style="height:20px; width:20px;">
                    <label for="q3"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q3.1" name="q3.1" style="height:20px; width:20px;">
                    <label for="q3.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Brake Lights</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q4" name="q4" style="height:20px; width:20px;">
                    <label for="q4"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q4.1" name="q4.1" style="height:20px; width:20px;">
                    <label for="q4.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Reverse Lights</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q5" name="q5" style="height:20px; width:20px;">
                    <label for="q5"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q5.1" name="q5.1" style="height:20px; width:20px;">
                    <label for="q5.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Back Up Alarm</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q6" name="q6" style="height:20px; width:20px;">
                    <label for="q6"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q6.1" name="q6.1" style="height:20px; width:20px;">
                    <label for="q6.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Four-Way Flashers</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q7" name="q7" style="height:20px; width:20px;">
                    <label for="q7"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q7.1" name="q7.1" style="height:20px; width:20px;">
                    <label for="q7.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Fluid Leaks</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q8" name="q8" style="height:20px; width:20px;">
                    <label for="q8"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q8.1" name="q8.1" style="height:20px; width:20px;">
                    <label for="q8.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Tire Conditions</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q9" name="q9" style="height:20px; width:20px;">
                    <label for="q9"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q9.1" name="q9.1" style="height:20px; width:20px;">
                    <label for="q9.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Windshield (Clean, no chips or cracks)</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q10" name="q10" style="height:20px; width:20px;">
                    <label for="q10"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q10.1" name="q10.1" style="height:20px; width:20px;">
                    <label for="q10.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Windows (Clean, no chips or cracks)</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q11" name="q11" style="height:20px; width:20px;">
                    <label for="q11"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q11.1" name="q11.1" style="height:20px; width:20px;">
                    <label for="q11.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Mirrors (No visible damage)</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q12" name="q12" style="height:20px; width:20px;">
                    <label for="q12"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q12.1" name="q12.1" style="height:20px; width:20px;">
                    <label for="q12.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Body Damage Assessment</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q13" name="q13" style="height:20px; width:20px;">
                    <label for="q13"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q13.1" name="q13.1" style="height:20px; width:20px;">
                    <label for="q13.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Body Exterior Clean</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q14" name="q14" style="height:20px; width:20px;">
                    <label for="q14"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q14.1" name="q14.1" style="height:20px; width:20px;">
                    <label for="q14.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Door Operation</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q15" name="q15" style="height:20px; width:20px;">
                    <label for="q15"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q15.1" name="q15.1" style="height:20px; width:20px;">
                    <label for="q15.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Fuel Gauge Reads Full</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q16" name="q16" style="height:20px; width:20px;">
                    <label for="q16"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q16.1" name="q16.1" style="height:20px; width:20px;">
                    <label for="q16.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Horn</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q17" name="q17" style="height:20px; width:20px;">
                    <label for="q17"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q17.1" name="q17.1" style="height:20px; width:20px;">
                    <label for="q17.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Driver Seat Belt</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q18" name="q18" style="height:20px; width:20px;">
                    <label for="q18"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q18.1" name="q18.1" style="height:20px; width:20px;">
                    <label for="q18.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Steering Wheel Mechanism</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q19" name="q19" style="height:20px; width:20px;">
                    <label for="q19"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q19.1" name="q19.1" style="height:20px; width:20px;">
                    <label for="q19.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Brake Pedal</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q20" name="q20" style="height:20px; width:20px;">
                    <label for="q20"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q20.1" name="q20.1" style="height:20px; width:20px;">
                    <label for="q20.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Interior Lights</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q21" name="q21" style="height:20px; width:20px;">
                    <label for="q21"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q21.1" name="q21.1" style="height:20px; width:20px;">
                    <label for="q21.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Current Insurance Card</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q22" name="q22" style="height:20px; width:20px;">
                    <label for="q22"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q22.1" name="q22.1" style="height:20px; width:20px;">
                    <label for="q22.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>Map Book</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q23" name="q23" style="height:20px; width:20px;">
                    <label for="q23"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q23.1" name="q23.1" style="height:20px; width:20px;">
                    <label for="q23.1"></label><br>
                </div>
            </div>
            <div class="container">
                <div class="header">
                    <h3>EZPass</h3>
                </div>
                <div class="Pass">
                    <input type="checkbox" id="q24" name="q24"style="height:20px; width:20px;">
                    <label for="q24"></label><br>
                </div>
                <div class="Fail">
                    <input type="checkbox" id="q24.1" name="q24.1" style="height:20px; width:20px;">
                    <label for="q24.1"></label><br>
                </div>
            </div>
            <div class="container1">
                <div class="header">
                    <h2>Notes</h2>
                </div>
            </div>
            <div class="notesbox">
                <input type="text" id="notes" name="notes" size="80" style="height:45px; word-wrap: normal;">
                <label for="notes"></label><br>
            </div>
            
            <div class="container1">
                <div class="header">
                    <h2>Signature</h2>
                </div>
            </div>
            <div class="canvas">
                <script src="jSignature.min.js"></script>
                <div id="signature"></div>
                <script>
                    $(document).ready(function() {
                        $("#signature").jSignature()
                    })
                </script>
            </div>
            <div class="button">
                <input type="submit" value="save">
            </div>
        
        </form>
        

        </div>
    </div>
</body>
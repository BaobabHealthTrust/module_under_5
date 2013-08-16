/*
 * Custom javascript code goes in here.
 *
 **/

var mother_status = "";
var timedEvent = "";
var temp = ""
var lmp = "";
var name = '';
var bpOn = '';
var currentConcept = "";
var artData = {};

function checkTimeForStoppingBreastFeeding(){
    if(__$("touchscreenInput" + tstCurrentPage).value == "Breastfeeding stopped over 6 weeks ago"){
        showCategory("Confirm HIV status!")
    } else if(__$("touchscreenInput" + tstCurrentPage).value == "Breastfeeding stopped in last 6 weeks"){
        showCategory("Book HIV test!")
    }
    setTimeout("checkTimeForStoppingBreastFeeding()", 100)
}

function checkConfirmationStatus(status){
    if(__$("touchscreenInput" + tstCurrentPage).value == status){
        showCategory("START ART!")
    } else {
        hideCategory();
    }
    setTimeout("checkConfirmationStatus()", 100)
}

function checkBCGDate(session_date){
    try{
        var today = new Date(session_date);
   
        var date = (__$("1.1.2.1").value.trim() != "Unknown" ? __$("1.1.2.1").value.trim() : today);
        var bcgDate = new Date(date)
    
        var diff = today - bcgDate;
        return Math.round(diff / (7 * 24 * 60 * 60 * 1000))
    }catch(ex){}
}

function findDates(){
    getDayOfMonthPicker(__$("1.1.2.1").value, __$("1.1.2.2").value);
}

function populateMonth(id){

    __$(id).innerHTML = "";

    var months = [
    [1,"January"],
    [2,"February"],
    [3,"March"],
    [4,"April"],
    [5,"May"],
    [6,"June"],
    [7,"July"],
    [8,"August"],
    [9,"September"],
    [10,"October"],
    [11,"November"],
    [12,"December"],
    ["Unknown","Unknown"]
    ]

    for(var i = 0; i < months.length; i++){
        var opt = document.createElement("option");
        opt.value = months[i][0];
        opt.innerHTML = months[i][1];

        __$(id).appendChild(opt);
    }

}

function skipFlow(val){
    str = document.getElementsByTagName("form")[0].action
    if (str.match(/\?/))
        document.getElementsByTagName("form")[0].action += "&skip_flow=" + val;
    else{
        document.getElementsByTagName("form")[0].action += "?skip_flow=" + val;
    }
}

function drop(result){
    var link = document.location.toString();
    if (!result.match(/unknown|none/i) && (result.toLowerCase().trim() == "yes" || currentConcept.match(/birth length|birth weight|head circumference|observation on/i)) ){
        $("touchscreenInput" + tstCurrentPage).value = result;
        if ($("touchscreenInput" + tstCurrentPage).getAttribute("tt_requirenextclick").toString().trim() == "false"){
       
            if (($("nextButton").style.display.match(/none/i) && !currentConcept.match(/observation on/i)) && link.match(/reason\_for\_special\medical\_history|initial\_new\_born\_record|surgical\_history/)){
                setTimeout("gotoNextPage()", 1500);
            }
        
        }
   
    }
}
function ajaxPull(concept, user, patient){

    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {

        if ((!httpRequest) || (!concept) || (!patient)) return;
        if (httpRequest.readyState == 4 && (httpRequest.status == 200 ||
            httpRequest.status == 304)) {

            var result = JSON.parse(httpRequest.responseText);
            if (result.toString().length > 0){

                var helpText = __$("touchscreenInput" + tstCurrentPage).getAttribute("helpText")
                try{
                    var link = document.location.toString();                  
                    if (helpText.match(/\?/) || helpText.match(/birth length|birth weight|head circumference/i) || link.match(/reason\_for\_special\care|medical\_history|initial\_new\_born\_record/)){
                        drop(result)
                    }
                }catch(exc){}
                
                $('inputFrame' + tstCurrentPage).onclick = function(){
                    if ($("touchscreenInput" + tstCurrentPage).value.length == 0){
                        __$("touchscreenInput" + tstCurrentPage).value = result.trim();
                    }
                }
                
                try{
                    $('page' + tstCurrentPage).appendChild(flag)
                }catch(ex){}
                
            }
        }
    };

    try {
        var aUrl = "/encounters/probe_values?concept_name=" + concept + "&patient_id=" + patient + "&user_id=" + user;
        httpRequest.open('GET', aUrl, true);
        httpRequest.send(null);
    } catch(e){
    }
}

function probeValues(){

    if (document.location.toString().match(/protocol\_patients/)){
        try{
            var pageConcept = $("touchscreenInput" + tstCurrentPage).name.replace(/concept\[|]/g, "");
            if (pageConcept != currentConcept){
                currentConcept =  pageConcept;

                var user = "";
                var patient = "";

                var inputNodes = document.getElementsByTagName("input")
                for (var i = 0; i < inputNodes.length; i ++){
                    if (inputNodes[i].name == "patient_id"){
                        patient = inputNodes[i].value
                    }else if (inputNodes[i].name == "user_id"){
                        user = inputNodes[i].value
                    }
                }

                ajaxPull(currentConcept, user, patient);
            }
        }catch(ex){

        }
        setTimeout("probeValues()", 300);
    }
}

setTimeout("probeValues()", 20);

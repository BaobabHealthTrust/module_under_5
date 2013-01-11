/*
 * Custom javascript code goes in here.
 *
 **/

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
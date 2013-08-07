P.1. SURGICAL HISTORY [program: UNDER 5 PROGRAM, scope: RECENT, concept: Ever had any surgical procedure?]
Q.1.1. Ever had any surgical procedure? [pos: 0, tt_onLoad: tt_cancel_destination += "&skip_flow=true"; showCategory("Surgical History"); __$("category").style.fontSize = "30px"; skipFlow("<%= params["skip_flow"]%>")]
O.1.1.1. No
O.1.1.2. Yes

Q.1.1.3. Reason for Procedure [name: concept[Diagnosis][], tt_onLoad: showCategory("Surgical History"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes", ajaxURL: /encounters/diagnoses?search_string=, pos: 1]

Q.1.1.5. Next Reason For Procedure (Optional) [name: concept[Diagnosis][], tt_onLoad: showCategory("Surgical History"); __$("category").style.fontSize = "30px";, condition: __$("1.1").value.trim() == "Yes" && __$("1.1.3").value.trim().length > 0, optional: true, ajaxURL: /encounters/diagnoses?search_string=, pos: 3]

Q.1.1.7. Next Reason For Procedure (Optional) [name: concept[Diagnosis][], tt_onLoad: showCategory("Surgical History"); __$("category").style.fontSize = "30px";, condition: __$("1.1").value.trim() == "Yes" && __$("1.1.5").value.trim().length > 0, optional: true, ajaxURL: /encounters/diagnoses?search_string=, pos: 5]

Q.1.1.9. Next Reason For Procedure (Optional) [name: concept[Diagnosis][], tt_onLoad: showCategory("Surgical History"); __$("category").style.fontSize = "30px";, condition: __$("1.1").value.trim() == "Yes" && __$("1.1.7").value.trim().length > 0, optional: true, ajaxURL: /encounters/diagnoses?search_string=, pos: 7]

Q.1.1.11. Next Reason For Procedure (Optional) [name: concept[Diagnosis][], tt_onLoad: showCategory("Surgical History"); __$("category").style.fontSize = "30px";, condition: __$("1.1").value.trim() == "Yes" && __$("1.1.9").value.trim().length > 0, optional: true, ajaxURL: /encounters/diagnoses?search_string=, pos: 9]

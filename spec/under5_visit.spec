P.1. UNDER 5 VISIT [program: UNDER 5 PROGRAM, includejs: dispense;generics, includecss: dispense;drug-style, concept: Weight, scope: TODAY]
C.1. On each regular child under 5 visit, capture the following details:
Q.1.1. Are there any diagnoses to be captured? [pos: 0, disabled: disabled, tt_requirenextclick: false, tt_onLoad: tt_cancel_destination += "&skip_flow=true"; __$("nextButton").style.display = "none"; skipFlow("<%= params["skip_flow"]%>"); showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px";]
O.1.1.1. No
O.1.1.2. Yes

Q.1.1.3. Diagnosis [name: concept[Diagnosis][], condition: __$("1.1").value.trim() == "Yes", ajaxUrl: /encounters/diagnoses?search=, pos: 1, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px";]

Q.1.1.4. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.3").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 2]

Q.1.1.5. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.4").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 3]

Q.1.1.6. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.5").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 4]

Q.1.1.7. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.6").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 5]

Q.1.1.8. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.7").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 6]

Q.1.1.9. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.8").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 7]

Q.1.1.10. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.9").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 8]

Q.1.1.11. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.10").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 9]

Q.1.1.12. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.11").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 10, tt_onLoad: __$("nextButton").style.display = "block"]

Q.1.3. Treatment [tt_onLoad: generateGenerics(<%= @patient.id %>); showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px"; __$("nextButton").style.display = "block", tt_onUnLoad: removeGenerics(), tt_pageStyleClass: NoControls, optional: true, pos: 31]

Q.1.4. Height (cm) [pos: 32, min: 20, max: 130, tt_pageStyleClass: NumbersWithUnknownAndDecimal, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", field_type: number]

Q.1.5. Weight (grams) [pos: 33, concept: Weight, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", min: 2500, max: 34000, tt_pageStyleClass: NumbersOnly, field_type: number]

Q.1.6. Notes [pos: 34, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", field_type: textarea, optional: true]








